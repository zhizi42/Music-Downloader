import json
import os
import re
import shutil
import sys
import threading
import webbrowser

import mutagen.id3 as mi
import requests
import wx

import MD_img_py
import MD_wx_GUI


def error(sentence):
    wx.MessageBox(u"您在使用程序时遇到了一个错误。\n如果需要反馈bug，请联系开发者。联系方式见关于界面。\n" + sentence, u"竟然还有这种操作？！", wx.OK)


def download(link, downloadpath, music_or_image):
    if downloading_cancel:return
    try:
        get_music_or_image_req = requests.get(link, headers=HEADERS).content
        with open(downloadpath, "wb") as music_or_image_file:
            music_or_image_file.write(get_music_or_image_req)
    except:
        if music_or_image == "音乐":
            then = "请等待一段时间后再次尝试。"
        elif music_or_image == "图片":
            then = "程序会继续执行，但下载的音乐中会没有图片。"
        error("错误原因：下载{}失败。可能是因为短时间内下载次数过多被服务器屏蔽了IP地址。{}".format(music_or_image, then))
        return
    else:
        return True


def download_lyric(id, path):
    if downloading_cancel:return
    lyric_link = "https://api.imjad.cn/cloudmusic/?type=lyric&id={}".format(id)
    lyric_dict = json.loads(requests.get(lyric_link, headers=HEADERS).text)
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
        with open(path + ".lrc", "w") as lyric_file:
            lyric_file.write(lyric)
            return True


def download_name(id, path, number_now_and_all, id_type):
    link = "https://music.163.com/song?id={}".format(id)
    if downloading_cancel:return
    try:
        htmlcode = requests.get(link).text
    except:
        error("错误原因：获取音乐信息失败。请检查网络是否正常。")
        return
    try:
        name = re.search(r'data-res-name=".+"', htmlcode)
        if name == None:
            error("错误原因：未能找到该链接对应的歌曲名字。")
            return
        name = name.group().replace("amp;", "")[15:-1]
        artist = re.search(r'data-res-author=".+"', htmlcode)
        artist = artist.group().replace("amp;", "")[17:-1]
        pattern = r"<meta property=\"og:music:album\" content=\".+\"/>"
        album = re.search(pattern, htmlcode)
        album = album.group().replace("amp;", "")[41:-3]
        pattern = r"<meta property=\"og:image\" content=\".+\" />"
        imagelink = re.search(pattern, htmlcode)
        imagelink = imagelink.group()[35:-4] + "?param=640y640"
    except:
        error("错误原因：程序在获取歌曲相关信息时遇到了错误。")
        return
    if setting_dict["name_version_pc"] == True:
        musicname = artist.replace("/", ",") + " - " +  name
    else:
        musicname = name + " - " + artist.replace("/", ",")
    musicname = musicname.replace("/", "／").replace("\\", "＼").replace(":", "：").replace("*", "＊").replace("/", "/").replace("?", "？").replace("\"", "＂").replace("<", "＜").replace(">", "＞").replace("|", "｜")
    downloadpath = path + "/" + musicname
    download_now_and_all = "第{}首，共{}首".format(number_now_and_all[0], number_now_and_all[1])
    downloading_frame.set_text("正在下载\n{}\n({})".format(musicname, download_now_and_all))
    if setting_dict["download_music_ornot"]:
        musiclink = "http://music.163.com/song/media/outer/url?id={}".format(id)
        music_success = download(musiclink, downloadpath + ".mp3", "音乐")
        if music_success == None:
            return
    if setting_dict["download_music_ornot"] or setting_dict["download_image_ornot"]:
        image_success = download(imagelink, downloadpath + ".jpg", "图片")
    if setting_dict["download_lyric_ornot"]:
        lyric_success = download_lyric(id, downloadpath)
    if setting_dict["download_music_ornot"] and music_success:
        music_size = float(os.path.getsize(downloadpath + ".mp3")/1024)
        if downloading_cancel:return
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
            if downloading_cancel:return
            error("错误原因：无法修改歌曲的音乐标签。")
            return
        else:
            if id_type == "music":
                download_done = "下载成攻！我绝对不是故意打错字的喵(^･ｪ･^)音乐已保存为\n{}.mp3\n至目录  {}\n（若发现文件不正确，请在确认操作正确后联系开发者。）".format(musicname, path.replace("/", "\\"))
                downloading_frame.set_text(download_done)


class give(MD_wx_GUI.frame_give):
    
    def set_img(self):
        self.give_bitmap.SetBitmap(wx.Bitmap(DATA_PATH + "img/give_img.png"))


class downloading(MD_wx_GUI.frame_downloading):
    
    def set_text(self, text):
        try:
            self.text_downloading.SetLabel(text)
        except:
            pass
    
    def cancel_download(self, event):
        global downloading_cancel
        downloading_cancel = True
        event.Skip()


class about(MD_wx_GUI.frame_about):

    def show_give(self, event):
        give_app = wx.App()
        give_frame = give(None)
        give_frame.set_img()
        give_frame.Show()
        give_app.MainLoop()
        sys.exit()
    
    def join_group(self, event):
        webbrowser.open("https://jq.qq.com/?_wv=1027&k=5dpwpPu")
    
    def give_feedback(self, event):
        URL_feedback = "https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAQLVARlUNTZWU1FINkVMMDZKT0VOUVVJVUdOSVNOUi4u"
        webbrowser.open(URL_feedback)


class setting(MD_wx_GUI.frame_setting):
    
    
    def set_value(self):
        self.dirPicker_path.SetPath(setting_dict["path"])
        self.radiobutton_pc_name.SetValue(setting_dict["name_version_pc"])
        self.music_checkbox.SetValue(setting_dict["download_music_ornot"])
        self.lyric_checkbox.SetValue(setting_dict["download_lyric_ornot"])
        self.image_checkbox.SetValue(setting_dict["download_image_ornot"])
    
    def get_setting(self):
        global setting_dict
        path = self.dirPicker_path.GetPath()
        name_version_pc = self.radiobutton_pc_name.GetValue()
        download_music_ornot = self.music_checkbox.GetValue()
        download_lyric_ornot = self.lyric_checkbox.GetValue()
        download_image_ornot = self.image_checkbox.GetValue()
        setting_dict = {"path": path, "name_version_pc": name_version_pc, "download_music_ornot": download_music_ornot, "download_lyric_ornot": download_lyric_ornot, "download_image_ornot": download_image_ornot}
    
    def save_setting(self, event):
        self.get_setting()
        if not (setting_dict["download_music_ornot"] or setting_dict["download_lyric_ornot"] or setting_dict["download_image_ornot"]):
            wx.MessageBox(u"请至少选择一个下载！", u"请至少选择一个下载！", wx.OK)
            return
        setting_json = json.dumps(setting_dict)
        with open(DATA_PATH + "Local State", "w") as Local_State:
            Local_State.write(setting_json)
    
    def setting_close(self, event):
        self.get_setting()
        if not (setting_dict["download_music_ornot"] or setting_dict["download_lyric_ornot"] or setting_dict["download_image_ornot"]):
            wx.MessageBox(u"请至少选择一个下载！", u"请至少选择一个下载！", wx.OK)
            return
        else:
            event.Skip()


class main(MD_wx_GUI.frame_main):
    
    def icon(self):
        icon = wx.Icon(DATA_PATH + "icon/main_icon.ico")
        self.SetIcon(icon)
    
    def download_main(self, event):
        link = self.link_input.GetValue()
        if link == "":
            wx.MessageBox(u"别玩啦再玩就要被玩坏啦！嘤嘤嘤！", u"别玩啦！", wx.OK)
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
                id_type = "music"
            path = setting_dict["path"].replace("\\", "/")
            if os.access(path, os.F_OK):
                if not os.access(path, os.R_OK):
                    error("错误原因：没有权限访问选择的目录。请选择其他目录或关闭程序后右键选择以管理员身份运行。")
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
            global downloading_cancel
            global downloading_frame
            downloading_cancel = False
            threading.Thread(target=self.start_download, args=(id, path, id_type, )).start()
            downloading_app = wx.App()
            downloading_frame = downloading(None)
            downloading_frame.Show()
            try:
                downloading_app.MainLoop()
            except:
                pass
            sys.exit()
    
    def start_download(self, id, path, id_type):
        if id_type == "music":
            number_now_and_all = [1, 1]
            download_name(id, path, number_now_and_all, id_type)
        elif id_type == "playlist":
            link_playlist = "https://api.imjad.cn/cloudmusic/?type=playlist&id={}".format(id)
            try:
                playlist_req = requests.get(link_playlist, headers=HEADERS).text
                playlist = json.loads(playlist_req)
            except:
                error("错误原因：获取音乐信息失败。请检查网络是否正常。")
            code_playlist = playlist["code"]
            if code_playlist == 200:
                name_playlist = "{} 的 {}".format(playlist["playlist"]["creator"]["nickname"], playlist["playlist"]["name"])
                id_playlist = [id["id"] for id in playlist["playlist"]["trackIds"]]
                for number_now, id in enumerate(id_playlist, 1):
                    number_now_and_all = [number_now, len(id_playlist)]
                    download_name(id, path, number_now_and_all, id_type)
                    if downloading_cancel:return
                download_done = "全部下载成攻！我绝对不是故意打错字的喵(^･ｪ･^)此歌单的音乐已保存至目录\n{}\n（若发现文件不正确，请在确认操作正确后联系开发者。）".format(path.replace("/", "\\"))
                downloading_frame.set_text(download_done)
            elif code_playlist == 404:
                error("错误原因：没有此歌单")
            else:
                error("获取歌单信息时发生未知错误，code:{}".format(code_playlist))
        else:
            error("错误！x73x68 TYPE ERROR")
        
    
    def show_setting(self, event):
        setting_app = wx.App()
        setting_frame = setting(None)
        setting_frame.set_value()
        setting_frame.Show()
        setting_app.MainLoop()
        sys.exit()
    
    def show_about(self, event):
        about_app = wx.App()
        about_frame = about(None)
        about_frame.Show()
        about_app.MainLoop()
        sys.exit()


DATA_PATH = os.path.expanduser("~/AppData/Local/Music Downloader/User Data/").replace("\\", "/")
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
if os.access(DATA_PATH + "First Run", os.F_OK):
    with open(DATA_PATH + "Local State", "r") as Local_State:
        setting_dict = json.loads(Local_State.read())
else:
    OLD_DATA_PATH = "C:/Users/" + os.getlogin() + "/AppData/Local/Music Downloader/User Data/"
    if os.access(OLD_DATA_PATH + "First Run", os.F_OK) :
        with open(OLD_DATA_PATH + "Local State", "r") as Local_State:
            FIRST_DATA = json.loads(Local_State.read())
        shutil.rmtree("C:/Users/" + os.getlogin() + "/AppData/Local/Music Downloader/")
    else:
        FIRST_DATA = {"path": os.path.expanduser("~\\Desktop"), "name_version_pc": True,
        "download_music_ornot": True, "download_lyric_ornot": False, "download_image_ornot": False}
    setting_dict = FIRST_DATA
    os.makedirs(DATA_PATH)
    with open(DATA_PATH + "First Run", "x"):
        pass
    with open(DATA_PATH + "Local State", "w") as Local_State:
        Local_State.write(json.dumps(FIRST_DATA))

exist_main_icon = os.access(DATA_PATH + "icon/main_icon.ico", os.F_OK)
if not exist_main_icon:
    os.makedirs(DATA_PATH + "icon")
    with open(DATA_PATH + "icon/main_icon.ico", "wb") as main_icon:
        main_icon.write(MD_img_py.main_icon)

exist_give_img = os.access(DATA_PATH + "img/give_img.png", os.F_OK)
if not exist_give_img:
    os.makedirs(DATA_PATH + "img")
    with open(DATA_PATH + "img/give_img.png", "wb") as main_icon:
        main_icon.write(MD_img_py.give_img)

main_app = wx.App()
main_frame = main(None)
main_frame.icon()
main_frame.Show()
main_app.MainLoop()