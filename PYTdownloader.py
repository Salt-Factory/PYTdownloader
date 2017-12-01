#TODO: QUITknop, error bij lege folder

import os, sys
import time
import Tkinter
import tkMessageBox
import thread

errorlist = []
print errorlist
def amount():
    fin = open('Adownloads.txt','r')
    x = 0
    while 1:
        if fin.readline() != "":
            x += 1
        else:
            print 'done!'
            fin.close()
            break
    x = str(x)
    return x

def showamount():
    text.config(text = 'Scanning!')
    x = amount()
    msg = "you are trying to download " + x + " file(s)"
    text.config(text = msg)
    if delvid.get() == 0:
        print 'Videos will be deleted'
    else:
        print "Videos won't be deleted"

    if delsong.get() == 1:
        print 'no conversion to .mp3'
    else:
        print 'videos will be converted'

def dl(link):
    yt = YouTube(link)
    name = yt.filename
    video = yt.get('mp4','360p')
    name += '.mp4'
    return name




def download(decoy):
    mus = E1.get()
    global dir
    global dirmus

    dir = os.getcwd()
    dirmus = dir + '/' + mus


    if not os.path.exists(dirmus):
        os.makedirs(dirmus)

    error = 0
    global video
    global DLamount
    fin = open('Adownloads.txt','r')

    while 1:
        video = ''
        print 'Downloading!'
        link = fin.readline()
        link.strip('/n')
        if link == '': break


        try:
            echo = 'youtube-dl -o "'+E1.get()+'/%(title)s.%(ext)s" -x --audio-format "mp3" '
            if delvid.get() == 1:
                echo += "-k "
            echo += link
            os.system(echo)
            print 'downloading!'
        except:
            print 'File already downloaded! Continuing with conversion'
        if delsong.get() == 0:  #move the mp3 file to the corrent folder
            return 1
            #convert(name)
            #thread.start_new_thread( convert, (name,))
        else:
            continue

        DLamount += 1
        DLtext = 'Downloaded ' + str(DLamount) + ' file(s)'
        errortext.config(text = DLtext)



def startdownload():
    if E1.get() == "":
        text.config(text = "Map mag geen lege folder zijn!")
        return 0;
    decoy = ''
    thread.start_new_thread(download, (decoy,))

def deletevideo(video):
    time.sleep(0.1)
    os.remove(video)

def stop():
    quit();
"""
def convert(name):
    global CVamount
    global ERamount
    global dir
    global dirmus
    print "dir:" + dir
    print "dirmus:" + dirmus
    import moviepy.editor as mp
    try:
        clip = mp.VideoFileClip(name)
    except:
        print 'Ascii error!'
        ERamount += 1


    video = name
    song, fame = name.split('.')

    song += '.mp3'
    try:
        clip.audio.write_audiofile(song)

        path1 = dir + '/' + song
        path2 = dirmus +'/'+ song
        print "paths:",path1,path2
        os.rename(path1,path2)

    except:
        try:
            os.remove(path1)
        except:
            print path1
        print 'Ascii error!'

        errorlist.append(name)
    CVamount += 1
    DLtext = 'Converted ' + str(CVamount) + ' file(s)'
    converttext.config(text = DLtext)
    ERtext = 'There are ' + str(ERamount) + ' errors'
    errortext.config(text = ERtext)
    decoy = 0
    if delvid.get() == 1:
        thread.start_new_thread(deletevideo, (video,))

    thread.exit()
"""













top = Tkinter.Tk()
top.geometry('300x210')
top.title('YT Downloader')
E1 = Tkinter.Entry(top, bd = 5)
L1 = Tkinter.Label(top, text="Folder:")
error = 0
status = "click a button!"
global DLamount
global CVamount
global ERamount
DLamount = 0
ERamount = 0
CVamount = 0
b1 = Tkinter.Button(top,text = "quit", command = stop)
b2 = Tkinter.Button(top,text = "download", command = startdownload)
text = Tkinter.Label(top,text = status)
errortext = Tkinter.Label(top,text = '')
converttext = Tkinter.Label(top,text = '')
delvid = Tkinter.IntVar()
delsong = Tkinter.IntVar()
box1 = Tkinter.Checkbutton(top, text="Keep the videos after conversion", variable=delvid)
box2 = Tkinter.Checkbutton(top, text="Don't convert into .mp3", variable = delsong)
L1.pack()
E1.pack()
b2.pack()
b1.pack()
text.pack()
converttext.pack()
errortext.pack()
box1.pack()
box2.pack()
top.mainloop()
