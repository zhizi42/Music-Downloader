# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Music Downloader 2.0， by AI丿质子。", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer1.SetMinSize( wx.Size( 500,220 ) )

        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"请在下方输入或粘贴音乐或歌单的链接", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.link_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
        self.link_input.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer1.Add( self.link_input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.Button_download = wx.Button( self, wx.ID_ANY, u"下载", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer1.Add( self.Button_download, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.Button_about = wx.Button( self, wx.ID_ANY, u"关于", wx.DefaultPosition, wx.Size( 80,30 ), 0 )
        bSizer2.Add( self.Button_about, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


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
        self.Button_about.Bind( wx.EVT_BUTTON, self.show_about )
        self.Button_setting.Bind( wx.EVT_BUTTON, self.show_setting )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def download_main( self, event ):
        event.Skip()


    def show_about( self, event ):
        event.Skip()

    def show_setting( self, event ):
        event.Skip()


###########################################################################
## Class frame_setting
###########################################################################

class frame_setting ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer3.SetMinSize( wx.Size( 400,250 ) )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"下载路径：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.dirPicker_path = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"请选择一个文件夹", wx.DefaultPosition, wx.Size( 250,-1 ), wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
        bSizer4.Add( self.dirPicker_path, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"命名格式：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.radiobutton_pc_name = wx.RadioButton( self, wx.ID_ANY, u"歌手 - 歌曲名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.radiobutton_pc_name.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer6.Add( self.radiobutton_pc_name, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.radiobutton_uwp_name = wx.RadioButton( self, wx.ID_ANY, u"歌曲名 - 歌手", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.radiobutton_uwp_name.SetValue( True )
        self.radiobutton_uwp_name.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer6.Add( self.radiobutton_uwp_name, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )


        bSizer5.Add( bSizer6, 0, 0, 5 )


        bSizer3.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"其他选项：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.music_checkbox = wx.CheckBox( self, wx.ID_ANY, u"下载音乐", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.music_checkbox.SetValue(True)
        self.music_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer8.Add( self.music_checkbox, 0, wx.ALL, 5 )

        self.lyric_checkbox = wx.CheckBox( self, wx.ID_ANY, u"同时下载lrc格式的歌词", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lyric_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer8.Add( self.lyric_checkbox, 0, wx.ALL, 5 )

        self.image_checkbox = wx.CheckBox( self, wx.ID_ANY, u"同时下载音乐专辑封面图片", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.image_checkbox.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer8.Add( self.image_checkbox, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, 0, 5 )


        bSizer3.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


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
        self.m_button6.Bind( wx.EVT_BUTTON, self.save_setting )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def setting_close( self, event ):
        event.Skip()

    def save_name_version( self, event ):
        event.Skip()

    def save_setting( self, event ):
        event.Skip()


###########################################################################
## Class frame_about
###########################################################################

class frame_about ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"关于本程序", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer9.SetMinSize( wx.Size( 600,560 ) )
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Music Downloader 2.0， by AI丿质子。\n特别感谢 鹿羽私，kurisu，luern0313，lzj。\n感谢rpONE为本程序制作了图标。感谢rpONE，莳昇，双霖等所有为本程序做出贡献的人。\n本程序非商业使用，仅因兴趣所作…网易云音乐不要起诉我啊，要是起诉我，我就…我就…我就哭给你看……有什么事情咱们商量着来好不好……\n如果您发现了程序的bug，或对程序有任何建议，（或者只是单纯的想来水群，）欢迎加入我们的QQ群！群号：820056900\n如果想让我们更加努力地把这个程序做得更好，可对我们进行投喂。可使用付款二维码，或直接转账给开发者的QQ。在此感谢所有投喂过开发者的人。\n投喂时推荐备注一下自己的昵称，否则使用付款账号的昵称。（每投喂一分钱开发者就会嘤嘤嘤一次哦！若需要，请私聊开发者领取）\n投喂名单：\n（按投喂时间排序，每次更新应用时这个名单也会更新）\nWindowsMEMZ\nkurisu\n今日龙王就是我\n阿易\n双霖\n温馨小聚\n邦邦\nlamJustDast", wx.DefaultPosition, wx.Size( 600,380 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer9.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"点我进行投喂", wx.DefaultPosition, wx.Size( 110,35 ), 0 )
        bSizer9.Add( self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"点我加入Q群", wx.DefaultPosition, wx.Size( 110,35 ), 0 )
        bSizer9.Add( self.m_button6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button8 = wx.Button( self, wx.ID_ANY, u"点我进行反馈", wx.DefaultPosition, wx.Size( 110,35 ), 0 )
        bSizer9.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()
        bSizer9.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button7.Bind( wx.EVT_BUTTON, self.show_give )
        self.m_button6.Bind( wx.EVT_BUTTON, self.join_group )
        self.m_button8.Bind( wx.EVT_BUTTON, self.give_feedback )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def show_give( self, event ):
        event.Skip()

    def join_group( self, event ):
        event.Skip()

    def give_feedback( self, event ):
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
## Class frame_downloading
###########################################################################

class frame_downloading ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"下载中……", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 236, 237, 232 ) )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer11.SetMinSize( wx.Size( 400,200 ) )
        self.text_downloading = wx.StaticText( self, wx.ID_ANY, u"正在加载……", wx.DefaultPosition, wx.Size( 400,200 ), 0 )
        self.text_downloading.Wrap( -1 )

        self.text_downloading.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.text_downloading.SetMaxSize( wx.Size( 400,-1 ) )

        bSizer11.Add( self.text_downloading, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.cancel_download )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def cancel_download( self, event ):
        event.Skip()


