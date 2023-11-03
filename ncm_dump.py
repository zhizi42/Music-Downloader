# -*- coding: utf-8 -*-
__author__ = 'qyh'
__date__ = '2018/10/16 9:22'

import base64
import binascii
import json
import multiprocessing
import os
import struct
from math import floor

import mutagen.flac
import mutagen.id3 as mi
from Crypto.Cipher import AES

#核心代码来源https://github.com/QCloudHao/ncmdump，AI丿质子做部分修改

class update_text():
    
    def __init__(self, queue:multiprocessing.Queue, list_index:int, seek_after_meta:int) -> None:
        self.percent = 0
        self.queue = queue
        self.list_index = list_index
        self.seek_after_meta = seek_after_meta

    def update_text(self, current:int, end:int):
        percent = floor((current - self.seek_after_meta) / (end - self.seek_after_meta) * 100)
        if percent == self.percent:
            return
        else:
            self.percent = percent
            self.queue.put([self.list_index, percent])

def get_meta(file_path):
    #十六进制转字符串
    core_key = binascii.a2b_hex("687A4852416D736F356B496E62617857")
    meta_key = binascii.a2b_hex("2331346C6A6B5F215C5D2630553C2728")
    unpad = lambda s: s[0:-(s[-1] if type(s[-1]) == int else ord(s[-1]))]
    f = open(file_path, 'rb')
    header = f.read(8)
    #字符串转十六进制
    assert binascii.b2a_hex(header) == b'4354454e4644414d'
    f.seek(2,1)
    key_length = f.read(4)
    key_length = struct.unpack('<I', bytes(key_length))[0]
    key_data = f.read(key_length)
    key_data_array = bytearray(key_data)
    for i in range(0, len(key_data_array)):
        key_data_array[i] ^= 0x64
    key_data = bytes(key_data_array)
    cryptor = AES.new(core_key, AES.MODE_ECB)
    key_data = unpad(cryptor.decrypt(key_data))[17:]
    key_length = len(key_data)
    key_data = bytearray(key_data)
    key_box = bytearray(range(256))
    c = 0
    last_byte = 0
    key_offset = 0
    for i in range(256):
        swap = key_box[i]
        c = (swap + last_byte + key_data[key_offset]) & 0xff
        key_offset += 1
        if key_offset >= key_length:
            key_offset = 0
        key_box[i] = key_box[c]
        key_box[c] = swap
        last_byte = c
    meta_length = f.read(4)
    meta_length = struct.unpack('<I', bytes(meta_length))[0]
    meta_data = f.read(meta_length)
    meta_data_array = bytearray(meta_data)
    for i in range(0, len(meta_data_array)):
        meta_data_array[i] ^= 0x63
    meta_data = bytes(meta_data_array)
    meta_data = base64.b64decode(meta_data[22:])
    cryptor = AES.new(meta_key, AES.MODE_ECB)
    meta_data = unpad(cryptor.decrypt(meta_data)).decode('utf-8')[6:]
    meta_data = json.loads(meta_data)
    crc32 = f.read(4)
    crc32 = struct.unpack('<I', bytes(crc32))[0]
    f.seek(5, 1)
    image_size = f.read(4)
    image_size = struct.unpack('<I', bytes(image_size))[0]
    image_data = f.read(image_size)
    
    seek_after_meta = f.tell()
    f.close()
    return [meta_data, key_box, image_data, seek_after_meta]

def dump(output_path, file_path, list_index, meta_data, key_box, image_data, seek_after_meta, queue):
    f = open(file_path, 'rb')
    f.seek(0, os.SEEK_END)
    seek_end = f.tell()
    f.seek(seek_after_meta)
    
    file_name = os.path.split(file_path)[1].split(".ncm")[0] + '.' + meta_data['format']
    new_file_path = os.path.join(output_path, file_name)
    m = open(new_file_path, 'wb')
    chunk = bytearray()
    update0 = update_text(queue, list_index, seek_after_meta)
    while True:
        seek_current = f.tell()
        update0.update_text(seek_current, seek_end)
        chunk = bytearray(f.read(0x8000))
        chunk_length = len(chunk)
        if not chunk:
            break
        for i in range(1, chunk_length+1):
            j = i & 0xff
            chunk[i-1] ^= key_box[(key_box[j] + key_box[(key_box[j] + j) & 0xff]) & 0xff]
        m.write(chunk)
    m.close()
    f.close()
    
    if meta_data['format'] == "flac":
        picture = mutagen.flac.Picture()
        picture.type = 3
        picture.mime = "image/jpeg"
        picture.data = image_data
        song = mutagen.flac.FLAC(new_file_path)
        song.add_picture(picture)
        song.save()
    elif meta_data['format'] == "mp3":
        song = mi.ID3(new_file_path)
        song["APIC"] = mi.APIC(encoding = 3, mime = "image/jpeg", type = 3, desc = u"Cover", data = image_data)
        song.save(v2_version = 3)
    
    return file_name