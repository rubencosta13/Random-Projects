from tkinter import filedialog
from tkinter import *
from pytube import YouTube
import os
import time 



window = Tk()
window.geometry('500x350')
window.resizable(0,0)
window.iconbitmap('icons\yt.ico')


def hide():
    widget.pack_forget()


def openFolder():
    path = "C:\Music"
    path = os.path.realpath(path)
    os.startfile(path)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(r'C:\Music')
    Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 
    


Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)
Button(window,text = 'Open Folder', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = openFolder).place(x=350 ,y = 250)


window.title("Simple youtube downloader")
link = StringVar()
Label(window, text = 'INSERT VIDEO LINK:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)
window.mainloop()