import urllib2
import urllib
import os
import subprocess as sp
import Tkinter as tk
import random, platform, sys
try:
    import ctypes
except:
    pass

def connected():
    while True:
        try:
            urllib2.urlopen("https://www.google.co.in/", timeout=1)
            return
        except urllib2.URLError as err:
            pass

def createdialog():

    def changewall():
        root.quit()
        SPI_SETDESKWALLPAPER = 20
        dirurl=sys.path[0]
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        category="?"+categoryoptionsvar.get()
        featured=featuredcheckbuttonvar.get()
        url="https://source.unsplash.com/"+("featured/" if(featured) else "")+str(screen_width)+"x"+str(screen_height)+"/"+ ("" if(category=="?Random") else category)
        print(url)
        urllib.urlretrieve(url,"background.jpg")
        if(osname=='linux'):
            cmd="/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+dirurl+"/background.jpg"
            os.system(cmd)
            sp.call(['notify-send','-t','5000','I\'ll code and make cash' ,'wallpaper changed from unsplash'])
        else:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, dirurl+"\\background.jpg" , 3)


    categorytext=tk.Label(root,text="Categories")
    categorytext.grid(row=1,column=1)

    categoryoptions=["Random","Nature","Waterfalls","City","Mountains","Sky","Space","Beach","Ocean"]
    categoryoptionsvar = tk.StringVar(root)
    categoryoptionsvar.set("Random")
    categoryoptionsmenu = apply(tk.OptionMenu,(root,categoryoptionsvar) + tuple(categoryoptions))
    categoryoptionsmenu.grid(row=1,column=2)

    featuredcheckbuttonvar=tk.IntVar()
    featuredcheckbutton=tk.Checkbutton(root,text="Featured",variable=featuredcheckbuttonvar)
    featuredcheckbutton.grid(row=2,column=1)

    gobutton=tk.Button(root,text="Go!",command=changewall)
    gobutton.grid(row=4,column=1,columnspan=2)


def main():
    root.title("AutoWall")
    createdialog()
    root.mainloop()

osname='linux' if platform.system().lower().find('windows')==-1 else 'windows'
if osname=='windows':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
connected()
main()
