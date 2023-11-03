import json
import multiprocessing
import os
import platform
import re
import shutil
import sys
import threading
import traceback
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from math import floor

import mutagen.id3 as mi
import requests
import wx

import MD_wx_GUI
import ncm_dump

server_host = "http://zhizi42.top:3000/"


def error(sentence, parent=None):
    wx.MessageBox(u"您在使用程序时遇到了一个错误。\n如果需要反馈bug，请联系开发者。联系方式见关于界面。\n" + sentence, u"竟然还有这种操作？！", wx.OK, parent=parent)


def download(link, downloadpath, is_music, download_list_frame=None, index=None):
    try:
        req = requests.get(link, headers=HEADERS, stream=True)
        content_length = int(req.headers['content-length'])
        now_length = 0
        with open(downloadpath, "wb") as file:
            for chunk in req.iter_content(128 * 1024):
                if chunk:
                    now_length += len(chunk)
                    file.write(chunk)
                    if is_music:
                        rate = floor(now_length / content_length * 100)
                        download_list_frame.listCtrl.SetItem(index, 2, f"{rate}%")
        if is_music:
            global num_download_done
            num_download_done += 1
            rate = floor((num_download_done / num_download_all) * 100)
            download_list_frame.gauge_all.SetValue(rate)
                    
    except:
        if is_music:
            then = "请等待一段时间后再次尝试。"
            download_list_frame.listCtrl.SetItem(index, 2, "下载失败")
        else:
            then = "程序会继续执行，但下载的音乐中会没有图片。"
        error("错误原因：下载{}失败。可能是因为短时间内下载次数过多被服务器屏蔽了IP地址。{}".format("音乐" if is_music else "图片", then))
        traceback.print_exc()
        return
    else:
        return True


def download_lyric(id, path):
    lyric_link = server_host + f"lyric?id={id}"
    lyric_dict = requests.get(lyric_link).json()
    if lyric_dict.get("nolyric"):
        error("错误原因：此歌曲没有歌词。")
    else:
        lyric = lyric_dict["lrc"]["lyric"]
        translate_lyric = lyric_dict["tlyric"]["lyric"]
        if not translate_lyric == None:
            lyric = lyric + translate_lyric
        if lyric == "":
            error("错误原因：此歌曲没有歌词。")
            return
        with open(path + ".lrc", "w", encoding="utf-8") as lyric_file:
            lyric_file.write(lyric)
            return True


def get_info_and_start(path, id, id_type, download_list_frame, pool:ThreadPoolExecutor):
    if id_type == "playlist":
        req_json = requests.get(server_host + f"playlist/detail?id={id}").json()
        id_list = []
        for i in req_json["playlist"]["trackIds"]:
            id_list.append(str(i["id"]))
        ids = ",".join(id_list)
        index_list = []
        for song_id in id_list:
            index = download_list_frame.listCtrl.InsertItem(
                download_list_frame.listCtrl.GetItemCount(), song_id)
            index_list.append(index)
    elif id_type == "song":
        ids = id
        index_list = [download_list_frame.listCtrl.InsertItem(
                download_list_frame.listCtrl.GetItemCount(), id)]
    try:
        link = server_host + f"song/detail?ids={ids}"
        req_json = requests.get(link).json()
        if req_json["code"] == 200:
            song_info_list = []
            for i in req_json["songs"]:
                id = i["id"]
                name = i["name"]
                artist_list = []
                for a in i["ar"]:
                    artist_list.append(a["name"])
                artist = " , ".join(artist_list)
                album = i["al"]["name"]
                image_link = i["al"]["picUrl"] + "?param=640y640"
                song_info_list.append([id, name, artist, album, image_link])
            for i in range(len(song_info_list)):
                download_list_frame.listCtrl.SetItem(index_list[i], 1, song_info_list[i][1])
                download_list_frame.listCtrl.SetItem(index_list[i], 2, "未开始")
                download_list_frame.listCtrl.SetItem(index_list[i], 3, song_info_list[i][2])
                download_list_frame.listCtrl.SetItem(index_list[i], 4, song_info_list[i][3])
        else:
            error("错误原因：程序在获取歌曲相关信息时返回代码错误，json内容：\n" + 
                  json.dumps(req_json, ensure_ascii=False), parent=download_list_frame)
            return
    except:
        error("错误原因：程序在获取歌曲相关信息时遇到了错误。")
        traceback.print_exc()
        return
    try:
        link = server_host + f"song/url?id={ids}"
        req_json = requests.get(link).json()
        none_url_list = []
        if req_json["code"] == 200:
            for i in range(len(req_json["data"])):
                url = req_json["data"][i]["url"]
                if url == None:
                    none_url_list.append(i)
                else:
                    song_info_list[i].append(url)
            if none_url_list:
                error(f"获取第{','.join([str(i + 1) for i in none_url_list])}首音乐下载链接失败！", download_list_frame)
                for i in none_url_list:
                    download_list_frame.listCtrl.SetItem(i, 2, "获取失败")
        #musiclink = "http://music.163.com/song/media/outer/url?id={}".format(id)
        else:
            error("错误原因：程序在获取歌曲下载链接时返回代码错误，json内容：\n" + 
                  json.dumps(req_json, ensure_ascii=False), parent=download_list_frame)
            return
    except:
        error("错误原因：程序在获取歌曲链接时遇到了错误。")
        traceback.print_exc()
        return
    for i in range(len(song_info_list)):
        if i in none_url_list:
            continue
        global num_download_all
        num_download_all += 1
        pool.submit(download_name, path, song_info_list[i], index_list[i], download_list_frame)
        


def download_name(path, song_info, index, download_list_frame):
    id, name, artist, album, image_link, music_link = song_info
    if setting_dict["name_version_pc"] == True:
        musicname = artist.replace("/", ",") + " - " +  name
    else:
        musicname = name + " - " + artist.replace("/", ",")
    musicname = musicname.replace("/", "／").replace("\\", "＼").replace(":", "：").replace("*", "＊").replace("/", "/").replace("?", "？").replace("\"", "＂").replace("<", "＜").replace(">", "＞").replace("|", "｜")
    downloadpath = path + "/" + musicname
    if setting_dict["download_music_ornot"]:
        music_success = download(music_link, downloadpath + ".mp3", True, download_list_frame, index)
        if music_success == None:
            return
    if setting_dict["download_music_ornot"] or setting_dict["download_image_ornot"]:
        image_success = download(image_link, downloadpath + ".jpg", False)
    if setting_dict["download_lyric_ornot"]:
        lyric_success = download_lyric(id, downloadpath)
    if setting_dict["download_music_ornot"] and music_success:
        music_size = float(os.path.getsize(downloadpath + ".mp3")/1024)
        if music_size < 200:
            error("错误原因：下载失败。可能是由于此歌曲受到版权保护。".format(musicname))
            return
        try:
            song = mi.ID3(downloadpath + ".mp3")
            song["TIT2"] = mi.TIT2(encoding = 3, text = [name])
            song["TPE1"] = mi.TPE1(encoding = 3, text = [artist])
            song["TALB"] = mi.TALB(encoding = 3, text = [album])
            if image_success:
                song["APIC"] = mi.APIC(encoding = 3, mime = "image/jpeg", type = 3, desc = u"Cover", data = open(downloadpath + ".jpg", "rb").read())
                if not setting_dict["download_image_ornot"]:
                    os.remove(downloadpath + ".jpg")
            song.save(v2_version = 3)
        except:
            error("错误原因：无法修改歌曲的音乐标签。")
            return
        else:
            return True


class give(MD_wx_GUI.frame_give):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        bitmap = wx.Bitmap(os.path.join(app_path, 'img/give_img.png'))
        self.give_bitmap.SetBitmap(bitmap)


class about(MD_wx_GUI.frame_about):

    def show_give(self, event):
        give_frame = give(main_frame)
        give_frame.Show()
    
    def join_group(self, event):
        webbrowser.open("https://jq.qq.com/?_wv=1027&k=5dpwpPu")
    
    def open_github(self, event):
        webbrowser.open("https://github.com/zhizi42/Music-Downloader")


class setting(MD_wx_GUI.frame_setting):
    
    
    def __init__(self, parent):
        super().__init__(parent)
        self.dirPicker_path.SetPath(setting_dict["path"])
        self.radiobutton_pc_name.SetValue(setting_dict["name_version_pc"])
        self.music_checkbox.SetValue(setting_dict["download_music_ornot"])
        self.lyric_checkbox.SetValue(setting_dict["download_lyric_ornot"])
        self.image_checkbox.SetValue(setting_dict["download_image_ornot"])
        self.text_download_thread.SetValue(str(setting_dict.get("download_thread", 4)))
    
    def get_setting(self):
        global setting_dict
        path = self.dirPicker_path.GetPath()
        name_version_pc = self.radiobutton_pc_name.GetValue()
        download_music_ornot = self.music_checkbox.GetValue()
        download_lyric_ornot = self.lyric_checkbox.GetValue()
        download_image_ornot = self.image_checkbox.GetValue()
        if not (download_music_ornot or download_lyric_ornot or download_image_ornot):
            wx.MessageBox(u"请至少选择一个下载！", u"请至少选择一个下载！", wx.OK)
            return
        try:
            download_thread = int(self.text_download_thread.GetValue())
            if not (download_thread > 0):
                raise
        except:
            error("下载线程不是正整数，已恢复为默认值。")
            download_thread = 4
        setting_dict = {"path": path, "name_version_pc": name_version_pc,
                        "download_music_ornot": download_music_ornot,
                        "download_lyric_ornot": download_lyric_ornot,
                        "download_image_ornot": download_image_ornot,
                        "download_thread": download_thread}
    
    def save_setting(self, event):
        self.get_setting()
        setting_json = json.dumps(setting_dict)
        with open(DATA_PATH + "Local State", "w") as Local_State:
            Local_State.write(setting_json)
    
    def setting_close(self, event):
        self.get_setting()
        event.Skip()
    
    def on_download_thread_text(self, event):
        download_thread = self.text_download_thread.GetValue()
        if download_thread == "":
            return
        try:
            if not (int(download_thread) > 0):
                raise
        except:
            self.text_download_thread.SetValue("4")


class main(MD_wx_GUI.frame_main):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        icon = wx.Icon(os.path.join(app_path, 'icon/icon.ico'))
        self.SetIcon(icon)
        
        self.download_list_frame = download_list(self)
        self.setting_frame = None
        self.ncm_frame = None
        self.about_frame = None
        
        download_thread = setting_dict.get("download_thread", 4)
        if not isinstance(download_thread, int):
            download_thread = 4
        self.pool = ThreadPoolExecutor(download_thread)
    
    def download_main(self, event):
        link = self.link_input.GetValue()
        if link == "":
            wx.MessageBox(u"没有输入任何东西哦~别玩啦再玩就要被玩坏啦！嘤嘤嘤！", u"别玩啦！", wx.OK)
        else:
            findid = re.search(r"song\?id=\d{4,13}" , link)
            if findid == None:
                findid = re.search(r"playlist\?id=\d{4,13}" , link)
                if findid == None:
                    error("错误原因：链接错误。请检查链接是否正确。")
                    return
                else:
                    id = findid.group()[12:]
                    id_type = "playlist"
            else:
                id = findid.group()[8:]
                id_type = "song"
            path = setting_dict["path"].replace("\\", "/")
            if os.access(path, os.F_OK):
                if os.access(path, os.R_OK):
                    self.show_download_list(None)
                    threading.Thread(target=get_info_and_start, args=(path, id, id_type, self.download_list_frame, self.pool)).start()
                else:
                    error("错误原因：没有权限访问选择的目录。请选择其他目录或关闭程序后右键选择以管理员身份运行。")
                    return
            else:
                patherror = wx.MessageDialog(None, u"输入的目录不存在。是否创建此目录？若选择取消，将取消下载。", u"目录不存在", wx.YES_NO).ShowModal()
                if patherror == wx.ID_YES:
                    try:
                        os.makedirs(path)
                    except:
                        error("错误原因：没有权限创建选择的目录。请选择其他目录或关闭程序后右键选择以管理员身份运行。")
                        return
                else:
                    return
    
    def show_download_list(self, event):
        if self.download_list_frame:
            if self.download_list_frame.Shown:
                self.download_list_frame.SetFocus()
            else:
                self.download_list_frame.Show()
        else:
            self.download_list_frame = download_list(self)
            self.download_list_frame.Show()
    
    def show_setting(self, event):
        if self.setting_frame and self.setting_frame.Shown:
            self.setting_frame.SetFocus()
        else:
            self.setting_frame = setting(main_frame)
            self.setting_frame.Show()
    
    def show_ncm(self, event):
        if self.ncm_frame and self.ncm_frame.Shown:
            self.ncm_frame.SetFocus()
        else:
            self.ncm_frame = ncm(main_frame)
            self.ncm_frame.Show()
    
    def show_about(self, event):
        if self.about_frame and self.about_frame.Shown:
            self.about_frame.SetFocus()
        else:
            self.about_frame = about(main_frame)
            self.about_frame.Show()


class ncm(MD_wx_GUI.frame_list):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetTitle("ncm格式转换")
        self.listCtrl.InsertColumn(0, "文件名")
        self.listCtrl.SetColumnWidth(0, 114)
        self.listCtrl.InsertColumn(1, "进度")
        self.listCtrl.SetColumnWidth(1, 50)
        self.listCtrl.InsertColumn(2, "名字")
        self.listCtrl.InsertColumn(3, "歌手")
        self.listCtrl.InsertColumn(4, "专辑名")
        self.ncm_info_list = []
    
    def add_files(self, event):
        dialog = wx.FileDialog(self, "选择多个ncm文件", style=wx.FD_OPEN | wx.FD_MULTIPLE, wildcard="*.ncm")
        if dialog.ShowModal() == wx.ID_OK:
            list_ncm = dialog.GetPaths()
            for i in list_ncm:
                index = self.listCtrl.InsertItem(self.listCtrl.GetItemCount(), i)
                meta, key_box, image_data, seek_after_meta = ncm_dump.get_meta(i)
                
                self.ncm_info_list.append([i, index, meta, key_box, image_data, seek_after_meta])
                name = meta["musicName"]
                artist = ", ".join([k[0] for k in meta["artist"]])
                album = meta["album"]
                self.listCtrl.SetItem(index, 1, "未开始")
                self.listCtrl.SetItem(index, 2, name)
                self.listCtrl.SetItem(index, 3, artist)
                self.listCtrl.SetItem(index, 4, album) 
    
    def recv_queue(self, queue:multiprocessing.Queue):
        done_num = 0
        total_num = len(self.ncm_info_list)
        while True:
            index, percent = queue.get()
            self.listCtrl.SetItem(index, 1, f"{percent}%")
            if percent == 100:
                done_num += 1
                total_percent = floor(done_num / total_num * 100)
                self.gauge_all.SetValue(total_percent)
                if done_num == total_num:
                    wx.MessageBox(u"全部转换成攻！我绝对不是故意打错字的喵(^･ｪ･^)", u"转换成攻！", wx.OK)
                    break
    
    def start_convert(self, event):
        if self.ncm_info_list == []:
            wx.MessageBox(u"没有添加任何歌曲哦~别玩啦再玩就要被玩坏啦！嘤嘤嘤！", u"别玩啦！", wx.OK)
            return
        pool = multiprocessing.Pool()
        queue = multiprocessing.Manager().Queue()
        for i in self.ncm_info_list:
            pool.apply_async(start_dump, args=(i, queue))
        threading.Thread(target=self.recv_queue, args=(queue, )).start()


class download_list(MD_wx_GUI.frame_list):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.SetTitle("下载列表")
        self.listCtrl.InsertColumn(0, "歌曲ID")
        #self.listCtrl.SetColumnWidth(0, 114)
        self.listCtrl.InsertColumn(1, "名字")
        self.listCtrl.InsertColumn(2, "进度")
        self.listCtrl.SetColumnWidth(2, 50)
        self.listCtrl.InsertColumn(3, "歌手")
        self.listCtrl.InsertColumn(4, "专辑名")
        self.Button_start.Hide()
        self.Button_add_files.Hide()
        global num_download_all
        global num_download_done
        num_download_all = 0
        num_download_done = 0
    
    def Close(self, force=False):
        self.Hide()
        
    
def start_dump(ncm_info, queue):
    ncm_dump.dump(setting_dict["path"].replace("\\", "/"), *ncm_info, queue)


os_name = platform.system()
match os_name:
    case "Windows":
        DATA_PATH = os.path.expanduser("~/AppData/Local/Music Downloader/User Data/").replace("\\", "/")
    case "Darwin":
        DATA_PATH = os.path.expanduser("~/Library/Application Support/Music Downloader/").replace("\\", "/")
    case "Linux":
        DATA_PATH = os.path.expanduser("~/.Music Downloader/").replace("\\", "/")

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
FIRST_DATA = {"path": os.path.expanduser("~/Desktop"), "name_version_pc": True,
              "download_music_ornot": True, "download_lyric_ornot": False,
              "download_image_ornot": False, "download_thread": 4}
if os.access(DATA_PATH + "First Run", os.F_OK):
    first_run = False
    with open(DATA_PATH + "Local State", "r") as Local_State:
        setting_dict = json.loads(Local_State.read())
else:
    if os_name == "Windows":
        OLD_DATA_PATH = "C:/Users/" + os.getlogin() + "/AppData/Local/Music Downloader/User Data/"
        if OLD_DATA_PATH != DATA_PATH:
            if os.access(OLD_DATA_PATH + "First Run", os.F_OK) :
                with open(OLD_DATA_PATH + "Local State", "r") as Local_State:
                    FIRST_DATA = json.loads(Local_State.read())
                shutil.rmtree("C:/Users/" + os.getlogin() + "/AppData/Local/Music Downloader/")
            else:
                init_data = FIRST_DATA
                first_run = True
        else:
            init_data = FIRST_DATA
            first_run = True
    else:
        init_data = FIRST_DATA
        first_run = True
    setting_dict = init_data
    os.makedirs(DATA_PATH)
    with open(DATA_PATH + "First Run", "x"):
        pass
    with open(DATA_PATH + "Local State", "w") as Local_State:
        Local_State.write(json.dumps(FIRST_DATA))

try:
    os.removedirs(DATA_PATH + "icon")
    os.removedirs(DATA_PATH + "img")
except:
    pass
try:
    app_path = sys._MEIPASS
except:
    app_path = os.getcwd()

if __name__ == "__main__":
    main_app = wx.App()
    main_frame = main(None)
    main_frame.Show()
    if first_run:
        first_str = u"""欢迎使用Music Downloader。
默认下载路径为桌面，可前往设置更改。
默认下载线程数为4，建议网速越快线程越大以提高下载速度。
本程序免费且使用GPL-3开源。
如果有能力，可以给开发者投喂以激励开发。"""
        wx.MessageBox(first_str, u"欢迎使用Music Downloader", wx.OK)
    main_app.MainLoop()