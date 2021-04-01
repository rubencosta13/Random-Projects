from tkinter import *
from pytube import YouTube


window = Tk()
window.geometry('500x350')
window.iconbitmap('projects\icons\yt.ico')


def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download('Downloads')
    Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)


window.title("Simple youtube downloader")
link = StringVar()
Label(window, text = 'INSERT VIDEO LINK:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)
window.mainloop()