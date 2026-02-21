from PIL import ImageDraw, ImageFont, UnidentifiedImageError
import tkinter, tkinter.ttk as ttk
from datetime import datetime
from tkinter import (
    Frame, Tk, Toplevel,
    
    FLAT, CENTER, END, DISABLED, NORMAL
)
from urllib.error import URLError
from PIL import Image, ImageTk
from time import sleep
import os,sys,re
import threading, random
import pygame,keyboard
import json,socket
import phonenumbers, requests
import time
import logging


pygame.init()
fonts = {"GENERAL":('Chianti XBd BT',13),
         "GREETINGS":('Consolas',25)
}


def play(self, file) :
    pygame.mixer.Sound.play(file,loops=0)
    return



headers = []

fontA_title = ("Fruity microfont", 16)
fontB_title = ("Vudotronic", 16)

APP_WIDTH  = 1200 
APP_HEIGHT = 700
USER = os.environ["USERNAME"]

def check_com(self) :
    try :
        requests.head(url="http://www.google.com",timeout=2)
        return True
    except requests. ConnectTimeout as e :
        return None
    except requests.ConnectionError as e :
        return False
    finally :
        return

s = '''                              
                             /`            `o`                
                          ::o                sss              
                        :::/                  osys            
                     ./ :::                    syyo`s         
                    --- :::                    syy yyy        
                    ---::::                    syyyyyy        
                   -.---:::`                   syyyyyy`       
                   --:--:::::+     +o`      :sssyyys`ss       
                   `---::::////+`` `++oo  +sss.sysyyyy/       
                     -..::--/`///++ ++o-ooos`yssyyyys`        
                      -::-+-//////:/+ooyoss+ss/yssso          
                         -/://+/++++++oooooossyyy             
                             ://  ++++o+  oss                 
                                   +++o`                      
                                 ++++o+                      
                                /++++o+o`                    
                                -++++ooo                     
                                s++/+ooo                     
                                 ++ ++s                      
                                  / ++                       
                                          
                                   m` :ds`

                              RISEN FROM ASHES
'''
def slowprint2(label, s):
    for c in s + '\n':
        label.config(text=label.cget('text') + c)
        label.update()
        sleep(5. / 1000)


class MainMethod(tkinter.Tk) :
    
    def __init__(self) :
        super().__init__()

        self.count = 0
        self.SIG = None
        self.TOOGLE_TILE = False
        # self.error__  = lambda : error_disply.init(self=self)
        # self.red      = lambda : error_disply.red(self=self)
        # self.green    = lambda : error_disply.green(self=self)
        # self.no_net__ = lambda : error_disply.no_internet(self=self)
        self.build_netlinkUI()
        # self._ASK_SYSTEM_LOGIN_()

    def build_netlinkUI(self) :

        self.root = self

        width = 1200
        height = 700
        x_coordinate = int(self.root.winfo_screenwidth() / 2 - width / 2)
        y_coordinate = int(self.root.winfo_screenheight() / 2 - height / 2)


        self.root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
        self.root.title('GRACE')
        self.root.eval
        self.root.resizable(False, False)
        style = ttk.Style(self.root)
        self.root.overrideredirect(1)
        self.root.tk.call("source", "implementation\\include\\azure.tcl")
        self.root.tk.call("set_theme", "dark")
        self.root.configure(background="#060A0F")
        
        self.frame_head = Frame(self.root, height=66, width=1200, background="#060E17" )
        self.frame_head.place(x=0, y=0)#040B0F
        
        self.nav_title_head = Frame(self.root, height=60, width=1200, background="#040B0F")#040B0F
        self.nav_title_head.place(x=0,y=67)
        
        self.frame_down = Frame(self.root, height=80, width=1200 ,background="#081120", )
        self.frame_down.place(x=0, y=620)
        
        '''  LOWER LEVEL '''
#````````````````````````````````````````````````````````````````````````````````````````````
        '''Animate psuedo code according to action'''
        self.frame_down_a = Frame(self.frame_down, height=80, width=450, background="#081120" )
        
        '''Input Commands'''
        self.frame_down_b = Frame(self.frame_down, height=80 , width=300, background="#081120")
        
        '''File System'''
        self.frame_down_c = Frame(self.frame_down, height=80, width=450, background="#081120")

        self.frame_down_a.place(x=0, y=0)
        self.frame_down_b.place(x=450, y=0)
        self.frame_down_c.place(x=750, y=0)

#``````````````````````````````````````````````````````````````````````````````````````````````
        self.frame_display = Frame(self.nav_title_head, height=60, width=500, background="#040B0F")
        self.frame_display.place(x=560, y=0)

        self.img_0_0_0 = ImageTk.PhotoImage(Image.open('implementation\\resources\\0_0_0.png'))
        self.img_a_a_0 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_0.png'))
        self.img_a_a_1 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_1.png'))
        self.img_a_a_2 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_2.png'))
        self.img_a_a_3 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_3.png'))
        self.img_a_a_4 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_4.png'))
        self.img_a_a_5 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_5.png'))
        self.img_a_a_6 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_6.png'))
        self.img_a_a_7 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_7.png'))
        self.img_a_a_8 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_8.png'))
        self.img_a_a_9 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_9.png'))
        self.img_a_a_10 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_10.png'))
        self.img_a_a_11 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_11.png'))
        self.img_a_a_12 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_12.png'))
        self.img_a_a_13 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_13.png'))
        self.img_a_a_14 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_14.png'))
        self.img_a_a_15 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_15.png'))
        self.img_a_a_16 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_16.png'))
        self.img_a_a_17 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_17.png'))
        self.img_a_a_18 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_18.png'))
        self.img_a_a_19 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_19.png'))
        self.img_a_a_20 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_20.png'))
        self.img_a_a_21 = ImageTk.PhotoImage(Image.open('implementation\\resources\\a_a_21.png'))
        
        
        #060E17
        self.label_moniter = ttk.Label(self.frame_down_a,text='', foreground="#449F9D",background="#081120",font=("",7))
        self.log = f"class {USER} :: "+"{\n importing <umbrella_Mainframe.7>\n importing <umbrella_networkingProtocols.7>\n Successfully Imported ! \n"
        self.label_moniter.after(1000,self.display_log)
        

        self.label_moniter.place(x=15,y=3)
        
        
        self.lg = ttk.Label(self.frame_head ,image=self.img_0_0_0, background="#060E17")

        self.a_a_0  = ttk.Label(self.frame_head, image=self.img_a_a_0, background="#060E17")
        self.a_a_1  = ttk.Label(self.frame_head, image=self.img_a_a_1, background="#060E17")
        self.a_a_23 = ttk.Label(self.root, image=self.img_a_a_20, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_24 = ttk.Label(self.root, image=self.img_a_a_20, background="#040B0F",relief=FLAT,justify=CENTER)
        
        self.a_a_2 = ttk.Label(self.frame_head, image=self.img_a_a_2, background="#060E17")
        self.a_a_10 = ttk.Label(self.root, image=self.img_a_a_9, background="#060E17",relief=FLAT,justify=CENTER)
        self.a_a_20 = ttk.Label(self.root, image=self.img_a_a_17, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_21 = ttk.Label(self.root, image=self.img_a_a_18, background="#040B0F",relief=FLAT,justify=CENTER)
        
        self.a_a_4 = ttk.Label(self.frame_head, image=self.img_a_a_3, background="#060E17")
        self.a_a_5 = ttk.Label(self.frame_head, image=self.img_a_a_4, background="#060E17")
        self.a_a_8 = ttk.Label(self.root, image=self.img_a_a_7, background="#060E17",relief=FLAT)
        self.a_a_7 = ttk.Label(self.root, image=self.img_a_a_6, background="#060E17",relief=FLAT)
        # Relief  : flat, groove, raised, ridge, solid, or sunken
        # Justify :left, right, or center
        self.a_a_9 = ttk.Label(self.root, image=self.img_a_a_8, background="#060E17",justify=CENTER)
        self.a_a_12 = ttk.Label(self.root, image=self.img_a_a_11, background="#060E17",relief=FLAT,justify=CENTER)
        self.a_a_13 = ttk.Label(self.nav_title_head, image=self.img_a_a_12, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_14 = ttk.Label(self.nav_title_head, image=self.img_a_a_13, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_15 = ttk.Label(self.nav_title_head, image=self.img_a_a_1, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_16 = ttk.Label(self.nav_title_head, image=self.img_a_a_13, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_17 = ttk.Label(self.nav_title_head, image=self.img_a_a_14, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_18 = ttk.Label(self.nav_title_head, image=self.img_a_a_15, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_19 = ttk.Label(self.nav_title_head, image=self.img_a_a_16, background="#040B0F",relief=FLAT,justify=CENTER)
        self.a_a_22 = ttk.Label(self.root, image=self.img_a_a_19, background="#040B0F",relief=FLAT,justify=CENTER)
        
        self.a_a_25 = ttk.Label(self.root, image=self.img_a_a_21, background="#040B0F")
        self.a_a_25.place(x=860, y=200)

        self.entry  = ttk.Entry(self.frame_down_b, foreground="#449F9D", background="#040B0F",width=30)
        self.entry.place(x=35,y=10)
# Return
        self.entry.bind("<Return>",self.execute_command)
        self.entry.bind("<Button-3>",self.paste)




        self.status = ttk.Label(self.frame_down_c ,text="MANNUAL COMMAND LINE INPUT", foreground="#449F9D", background="#081120")
        self.status.place(x=40, y=5)

        self.SENSI_label_server = ttk.Label(self.nav_title_head, text="PROTOCOL SERVER", background="#040B0F",foreground="#617180",font=("Bahnschrift SemiLight",11))
        self.SENSI_label_server.place(x=20,y=5)




        self.lg.place(x=20, y=10)
        self.a_a_0.place(x=100, y=40)
        self.a_a_1.place(x=490, y=20)
        self.a_a_2.place(x=527, y=20)
        self.a_a_4.place(x=330, y=57)
        self.a_a_5.place(x=945, y=38)
        self.a_a_7.place(x=0, y=80)
        self.a_a_8.place(x=0, y=616)
        self.a_a_9.place(x=1192, y=65)
        self.a_a_10.place(x=0, y=621)
        
        self.a_a_12.place(x=0, y=672)
        self.a_a_13.place(x=8, y=53)
        self.a_a_14.place(x=0, y=30)
        self.a_a_15.place(x=190, y=11)
        self.a_a_16.place(x=225, y=11)
        self.a_a_17.place(x=445, y=7)
        self.a_a_18.place(x=460, y=17)
        self.a_a_19.place(x=460, y=7)
        self.a_a_20.place(x=-200, y=145)
        self.a_a_21.place(x=860, y=140)
        self.a_a_23.place(x=450,y=620)
        self.a_a_22.place(x=885, y=156)
        self.a_a_24.place(x=750, y=620)

        # THREAD_SIGNAL_ANIMATE = threading.Thread(target=self.thread_signal_animate)
        # THREAD_SIGNAL_ANIMATE.start()
        self.thread_signal_animate()

        self.title = ttk.Label(self.frame_head, text='G . R . A . C . E', foreground="#449F9D", background="#060E17")
        fontB_title = ("Vudotronic", 16)

        # self.heading   = ttk.Label(self.frame_head, text=os.environ['USERNAME'], background="#060E17", foreground="Black")
        # self.heading.configure(font=fontB_title)
        # self.heading.place(x=600, y=30)
        self.title.configure(font=fontA_title)
        self.title.place(x=160,y=13)
        # CommandCenter()

        self.DISPLAY_LABEL = ttk.Label(text="", background="#060A0F")
        self.DISPLAY_LABEL.place(x=30, y=150)


        # slowprint2(label=self.DISPLAY_LABEL, s=s)
        '''
        TILES FOR APPS
        
        '''
        self.TILE_APP_1 = Frame(master=self.nav_title_head, background="#040B0F", width=40, height=40)
        # self.TILE_APP_1 = Frame(master=self.nav_title_head, background="#449F9D", width=40, height=40)
        self.TILE_APP_1.place(x=500, y=10)

#040B0F        
        self._img_KLY = ImageTk.PhotoImage(Image.open("bt.png"))
        self.APP_but_KLY = ttk.Label(self.TILE_APP_1, image=self._img_KLY, background="#040B0F",relief=FLAT,justify=CENTER)
        self.APP_but_KLY.place(x=2, y=2)
        self.ACTIVE_TILE = 1

        self.TILE_APP_2 = Frame(master=self.nav_title_head, background="#040B0F", width=40, height=40)
        self.TILE_APP_2.place(x=580, y=10)
        
        self._img_GTS = ImageTk.PhotoImage(Image.open("gts.png"))
        self.APP_but_GTS = ttk.Label(self.TILE_APP_2, image=self._img_GTS, background="#040B0F",relief=FLAT,justify=CENTER)
        self.APP_but_GTS.place(x=2, y=2)

        self.TILE_APP_3 = Frame(master=self.nav_title_head, background="#040B0F", width=40, height=40)
        self.TILE_APP_3.place(x=660, y=10)
        
        self._img_DWP = ImageTk.PhotoImage(Image.open("dwp.png"))
        self.APP_but_DWP = ttk.Label(self.TILE_APP_3, image=self._img_DWP, background="#040B0F",relief=FLAT,justify=CENTER)
        self.APP_but_DWP.place(x=2, y=2)

        self.TILE_LiST = {
            1 : self.TILE_APP_1,
            2 : self.TILE_APP_2,
            3 : self.TILE_APP_3,
        }

        self.bind("<Left>",  self.move_TILE_Reverse)
        self.bind("<Right>", self.move_TILE_Front)
        self.bind("<Control-w>", self._toggle_tile)



        self.mainloop()
    
    def _toggle_tile(self, e = None) :
        
        if self.TOOGLE_TILE == None or self.TOOGLE_TILE == False :
            self.TOOGLE_TILE = True
            try :
                self.entry.configure(state=DISABLED)
                TILE = self.TILE_LiST[self.ACTIVE_TILE]
                TILE.configure(background="#449F9D")
            except : pass
        else :
            try :
                self.entry.configure(state=NORMAL)
                TILE = self.TILE_LiST[self.ACTIVE_TILE]
                TILE.configure(background="#040B0F")
                self.TOOGLE_TILE = False
            except : pass

    def move_TILE_Reverse(self, e = None) :
        if self.TOOGLE_TILE != False :
            try :    
                if self.ACTIVE_TILE in self.TILE_LiST :
                    NFrame = self.TILE_LiST[self.ACTIVE_TILE]
                    PFrame = self.TILE_LiST[self.ACTIVE_TILE-1]
                    NFrame.configure(background="#040B0F")
                    PFrame.configure(background="#449F9D")
                    self.ACTIVE_TILE = self.ACTIVE_TILE  - 1
                else : pass
                return
            except : pass

    def move_TILE_Front(self, e = None) :
        if self.TOOGLE_TILE != False :
            try :
                if self.ACTIVE_TILE in self.TILE_LiST :
                    NFrame = self.TILE_LiST[self.ACTIVE_TILE]
                    PFrame = self.TILE_LiST[self.ACTIVE_TILE+1]
                    NFrame.configure(background="#040B0F")
                    PFrame.configure(background="#449F9D")
                    self.ACTIVE_TILE = self.ACTIVE_TILE + 1
                else : pass
                return
            except : return

    def thread_signal_animate(self) :
        self.a_a_22.after(100,self.animate_signal)
        return

    def display_log(self) :
        if self.log :
                self.label_moniter.configure(text=self.log)
        return
    

        

    def set_signal(self) :
        try :
            requests.head(url="https://www.google.com",timeout=0.5)   
            self.SIG = "Green"
        except requests.ConnectTimeout as e :
            self.SIG = "None"
        except requests.ConnectionError as e :
            self.SIG = "Red"
        except requests.exceptions.ReadTimeout as e :
            self.SIG = "None"
        return
    
    

    def animate_signal(self) :
        
        UNBOUND_THREAD_PING = threading.Thread(target=self.set_signal)
        UNBOUND_THREAD_PING.start()
        if self.SIG == "Red" :
            self.SENSI_label_server.configure(text="SERVER OFFLINE")
            self.dir_anime = 'implementation/resources/animate/sig/r/'
        elif self.SIG == "Green" :
            self.SENSI_label_server.configure(text="PROTOCOL SERVER")
            self.dir_anime = 'implementation/resources/animate/sig/g/'

        else :
            self.SENSI_label_server.configure(text="SERVER BACKUP")
            self.dir_anime = 'implementation/resources/animate/sig/y/'
        self.img_b_b_1 = ImageTk.PhotoImage(Image.open(f'{self.dir_anime}\\b_b_1.png'))
        self.img_b_b_2 = ImageTk.PhotoImage(Image.open(f'{self.dir_anime}\\b_b_2.png'))
        self.img_b_b_3 = ImageTk.PhotoImage(Image.open(f'{self.dir_anime}\\b_b_3.png'))
        self.img_b_b_4 = ImageTk.PhotoImage(Image.open(f'{self.dir_anime}\\b_b_4.png'))
        
        try :
            self.b_b_1.destroy()
            self.b_b_2.destroy()
            self.b_b_3.destroy()
            self.b_b_4.destroy()
        
        except :
            pass

        def a1(self) :
            self.b_b_1 = ttk.Label(self.root, image=self.img_b_b_1, background="#040B0F",relief=FLAT,justify=CENTER)
            self.b_b_1.place(x=1090,y=117)
            self.root.after(150,func=lambda : a2(self))
            

        def a2(self) :
            self.b_b_2 = ttk.Label(self.root, image=self.img_b_b_2, background="#040B0F",relief=FLAT,justify=CENTER)
            self.b_b_2.place(x=1100,y=115)
            self.root.after(150,func=lambda : a3(self))
            
            

        def a3(self) :
            self.b_b_3 = ttk.Label(self.root, image=self.img_b_b_3, background="#040B0F",relief=FLAT,justify=CENTER)
            self.b_b_3.place(x=1110,y=113)
            self.root.after(150,func=lambda : a4(self))
            

        def a4(self) :
            self.b_b_4 = ttk.Label(self.root, image=self.img_b_b_4, background="#040B0F",relief=FLAT,justify=CENTER)
            self.b_b_4.place(x=1120,y=111)
            self.root.after(250,func=self.animate_signal)

        self.root.after(150,func=lambda : a1(self))




    def paste(self,e) :
        keyboard.press("Ctrl+v")
        keyboard.release("Ctrl+v")
        return
    
    def execute_command(self, e = None) : 
        if self.TOOGLE_TILE == False :
            xoxo = self.entry.get()
            self.xoxo = xoxo
            self.entry.delete(0,END)
            print (xoxo)
        else :
            print(self.ACTIVE_TILE)
        return

    def _ASK_SYSTEM_LOGIN_(self) :
        self.top = Toplevel()
        self.top.wm_overrideredirect()

        width = 600
        height = 300
        x_coordinate = int(self.top.winfo_screenwidth() / 2 - width / 2)
        y_coordinate = int(self.top.winfo_screenheight() / 2 - height / 2)


        self.top.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
        self.top.title('GRACE')
        self.top.resizable(False, False)
        style = ttk.Style(self.top)
        self.top.overrideredirect(1)
        self.top.tk.call("source", "implementation\\include\\azure.tcl")
        self.top.tk.call("set_theme", "dark")
        self.top.configure(background="#060A0F")

        self.withdraw()

        self.top.mainloop()

app = MainMethod()
app.mainloop()