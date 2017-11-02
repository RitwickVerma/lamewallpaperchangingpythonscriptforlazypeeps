#!/usr/bin/env python
import urllib2
import urllib
import os
import subprocess as sp
import Tkinter as tk
import random

def connected():
    while True:
        try:
            urllib2.urlopen("https://www.google.co.in/",timeout=1)
            return
        except urllib2.URLError as err:
            pass

def createdialog():

    def changewall():
        root.quit()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        category="?"+categoryoptionsvar.get()
        featured=featuredcheckbuttonvar.get()
        url="https://source.unsplash.com/"+("featured/" if(featured) else "")+str(screen_width)+"x"+str(screen_height)+"/"+ ("" if(category=="?Random") else category)
        print(url)
        urllib.urlretrieve(url,"/home/ritwick/Pictures/Wallpapers/background.jpg")
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/ritwick/Pictures/Wallpapers/background.jpg")
        musicurl="\"/home/ritwick/Music/"+random.choice(os.listdir("/home/ritwick/Music/"))+"\""
        print(musicurl)
        if(musiccheckbuttonvar.get()):
            os.system("xdg-open "+musicurl)
        sp.call(['notify-send','-t','5000','You are awesome','Wallpaper changed from unsplashed'])

    categorytext=tk.Label(root,text="Categories")
    categorytext.pack()
    categorytext.place(x=10,y=10)

    categoryoptions=["Random","Nature","Waterfalls","City","Mountains","Sky","Space","Beach","Ocean"]
    categoryoptionsvar = tk.StringVar(root)
    categoryoptionsvar.set("Random")
    categoryoptionsmenu = apply(tk.OptionMenu,(root,categoryoptionsvar) + tuple(categoryoptions))
    categoryoptionsmenu.pack()
    categoryoptionsmenu.place(x=80,y=5)

    featuredcheckbuttonvar=tk.IntVar()
    featuredcheckbutton=tk.Checkbutton(root,text="Featured",variable=featuredcheckbuttonvar)
    featuredcheckbutton.pack()
    featuredcheckbutton.place(x=10,y=50)

    musiccheckbuttonvar=tk.IntVar()
    musiccheckbutton=tk.Checkbutton(root,text="Music",variable=musiccheckbuttonvar)
    musiccheckbutton.pack()
    musiccheckbutton.place(x=10,y=80)

    gobutton=tk.Button(root,text="Go!",command=changewall)
    gobutton.pack()
    gobutton.place(x=75,y=150)


def main():
    root.title("AutoWall")
    createdialog()
    root.mainloop()
    #changewall(screen_width,screen_height)

root = tk.Tk()
connected()
main()
