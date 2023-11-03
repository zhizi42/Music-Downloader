# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-f48f265)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame_main
###########################################################################

class frame_main ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Music Downloader 2.6， by AI丿质子。", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer1.SetMinSize( wx.Size( 500,220 ) )

        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"请在下方输入或粘贴音乐或歌单的链接", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_staticText1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.link_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
        self.link_input.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer18.Add( self.link_input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Button_download = wx.Button( self, wx.ID_ANY, u"下载", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer18.Add( self.Button_download, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )

        self.Button_download_list = wx.Button( self, wx.ID_ANY, u"下载列表", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer1.Add( self.Button_download_list, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.Button_about = wx.Button( self, wx.ID_ANY, u"关于", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer2.Add( self.Button_about, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Button_open_ncm = wx.Button( self, wx.ID_ANY, u"ncm格式转换", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
        bSizer2.Add( self.Button_open_ncm, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Button_setting = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer2.Add( self.Button_setting, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.link_input.Bind( wx.EVT_TEXT_ENTER, self.download_main )
        self.Button_download.Bind( wx.EVT_BUTTON, self.download_main )
        self.Button_download_list.Bind( wx.EVT_BUTTON, self.show_download_list )
        self.Button_about.Bind( wx.EVT_BUTTON, self.show_about )
        self.Button_open_ncm.Bind( wx.EVT_BUTTON, self.show_ncm )
        self.Button_setting.Bind( wx.EVT_BUTTON, self.show_setting )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def download_main( self, event ):
        event.Skip()


    def show_download_list( self, event ):
        event.Skip()

    def show_about( self, event ):
        event.Skip()

    def show_ncm( self, event ):
        event.Skip()

    def show_setting( self, event ):
        event.Skip()


###########################################################################
## Class frame_setting
###########################################################################

class frame_setting ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer3.SetMinSize( wx.Size( 400,250 ) )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"下载路径：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.dirPicker_path = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"请选择一个文件夹", wx.DefaultPosition, wx.Size( 250,-1 ), wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
        bSizer4.Add( self.dirPicker_path, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"命名格式：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText4.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.radiobutton_pc_name = wx.RadioButton( self, wx.ID_ANY, u"歌手 - 歌曲名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.radiobutton_pc_name.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.radiobutton_pc_name.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer6.Add( self.radiobutton_pc_name, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.radiobutton_uwp_name = wx.RadioButton( self, wx.ID_ANY, u"歌曲名 - 歌手", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.radiobutton_uwp_name.SetValue( True )
        self.radiobutton_uwp_name.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.radiobutton_uwp_name.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer6.Add( self.radiobutton_uwp_name, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )


        bSizer5.Add( bSizer6, 0, 0, 5 )


        bSizer3.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"下载选项：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText5.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.music_checkbox = wx.CheckBox( self, wx.ID_ANY, u"下载音乐", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.music_checkbox.SetValue(True)
        self.music_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.music_checkbox.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer8.Add( self.music_checkbox, 0, wx.ALL, 5 )

        self.lyric_checkbox = wx.CheckBox( self, wx.ID_ANY, u"同时下载lrc格式的歌词", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lyric_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.lyric_checkbox.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer8.Add( self.lyric_checkbox, 0, wx.ALL, 5 )

        self.image_checkbox = wx.CheckBox( self, wx.ID_ANY, u"同时下载音乐专辑封面图片", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.image_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.image_checkbox.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer8.Add( self.image_checkbox, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, 0, 5 )


        bSizer3.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"同时下载线程数量", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer15.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.text_download_thread = wx.TextCtrl( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.text_download_thread.SetMaxLength( 2 )
        bSizer15.Add( self.text_download_thread, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"保存设置", wx.DefaultPosition, wx.Size( 95,30 ), 0 )
        bSizer3.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()
        bSizer3.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.setting_close )
        self.radiobutton_uwp_name.Bind( wx.EVT_RADIOBUTTON, self.save_name_version )
        self.text_download_thread.Bind( wx.EVT_TEXT, self.on_download_thread_text )
        self.m_button6.Bind( wx.EVT_BUTTON, self.save_setting )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def setting_close( self, event ):
        event.Skip()

    def save_name_version( self, event ):
        event.Skip()

    def on_download_thread_text( self, event ):
        event.Skip()

    def save_setting( self, event ):
        event.Skip()


###########################################################################
## Class frame_about
###########################################################################

class frame_about ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"关于本程序", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer9.SetMinSize( wx.Size( 500,-1 ) )
        self.text_about = wx.StaticText( self, wx.ID_ANY, u"Music Downloader 2.6， by AI丿质子。\n特别感谢 kurisu，luern0313，lzj。\n感谢rpONE为本程序制作了图标。\n感谢rpONE，莳昇，双霖等所有为本程序做出贡献的人。\n本程序非商业使用，仅因兴趣所作，\n网易云音乐不要起诉我啊，要是起诉我，\n我就…我就…我就哭给你看……\n有什么事情咱们商量着来好不好……\n如果您发现了程序的bug，或对程序有任何建议，\n（或者只是单纯的想来水群，）欢迎加入我们的QQ群！\n群号：820056900\n本程序使用GPL-3在GitHub开源，欢迎star和pr，\n有问题可提issue。\n点页面最下方按钮打开本项目GitHub地址。\n如果有能力，可投喂开发者以激励开发者肝代码。\n可使用付款二维码或直接转账给开发者的QQ。\n在此感谢所有投喂过开发者的人。\n投喂时推荐备注一下自己的昵称，\n否则使用付款账号的昵称。\n（每投喂一分钱开发者就会嘤嘤嘤一次哦！\n若需要，请私聊开发者领取）\n投喂名单：\n（按投喂时间排序，每次更新应用时这个名单也会更新）\nWindowsMEMZ、kurisu、今日龙王就是我、阿易、\n双霖、温馨小聚、邦邦、lamJustDast、doctor、\n中微子、Linux-Miga、污妖王、真寻\n特别感谢 墨一 的大额捐赠", wx.DefaultPosition, wx.Size( 500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.text_about.Wrap( -1 )

        self.text_about.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.text_about.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer9.Add( self.text_about, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"点我进行投喂", wx.DefaultPosition, wx.Size( 110,35 ), 0 )
        bSizer9.Add( self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"点我加入Q群", wx.DefaultPosition, wx.Size( 110,35 ), 0 )
        bSizer9.Add( self.m_button6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button12 = wx.Button( self, wx.ID_ANY, u"打开本项目GitHub", wx.DefaultPosition, wx.Size( 130,35 ), 0 )
        bSizer9.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()
        bSizer9.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button7.Bind( wx.EVT_BUTTON, self.show_give )
        self.m_button6.Bind( wx.EVT_BUTTON, self.join_group )
        self.m_button12.Bind( wx.EVT_BUTTON, self.open_github )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def show_give( self, event ):
        event.Skip()

    def join_group( self, event ):
        event.Skip()

    def open_github( self, event ):
        event.Skip()


###########################################################################
## Class frame_give
###########################################################################

class frame_give ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"投喂", pos = wx.DefaultPosition, size = wx.Size( 720,530 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.give_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.give_bitmap, 0, wx.ALL, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class frame_list
###########################################################################

class frame_list ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 421,292 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizer12.SetMinSize( wx.Size( 500,250 ) )
        self.listCtrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
        self.listCtrl.SetMinSize( wx.Size( 500,200 ) )

        bSizer12.Add( self.listCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer19.SetMinSize( wx.Size( -1,30 ) )
        self.Button_start = wx.Button( self, wx.ID_ANY, u"开始转换", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer19.Add( self.Button_start, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.gauge_all = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,20 ), wx.GA_HORIZONTAL )
        self.gauge_all.SetValue( 0 )
        bSizer19.Add( self.gauge_all, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Button_add_files = wx.Button( self, wx.ID_ANY, u"添加文件", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer19.Add( self.Button_add_files, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer12.Add( bSizer19, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer12 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Button_start.Bind( wx.EVT_BUTTON, self.start_convert )
        self.Button_add_files.Bind( wx.EVT_BUTTON, self.add_files )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def start_convert( self, event ):
        event.Skip()

    def add_files( self, event ):
        event.Skip()


