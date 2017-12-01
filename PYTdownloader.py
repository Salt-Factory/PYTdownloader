#TODO: QUITknop, error bij lege folder

import os, sys
import time
import Tkinter
import tkMessageBox
import thread
import subprocess
import tempfile

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


def downloadplaylist(link):
    j = readamount(link)
    i = 0
    for i in range(j):
        i += 1

        echo = 'youtube-dl --playlist-items '+str(i)+' -o "'+E1.get()+'/%(title)s.%(ext)s" -x --audio-format "mp3" '
        if delvid.get() == 1:
            echo += "-k "
        echo += link
        os.system(echo)
        print 'downloading!'

    if delsong.get() == 0:  #move the mp3 file to the corrent folder
        return 1
        #convert(name)
        #thread.start_new_thread( convert, (name,))
    else:
        1;


def readamount(link):
    os.system("youtube-dl --flat-playlist "+link)


    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['echo', 'a', 'b'], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        a = tempf.read()
        print a.find("Downloading")     #Search for amount of vids in playlist
        #i = 0
        # while 1:
        #     i += 1
        #
        #     if a.find("of "+str(i)) > 0:
        #         print i

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

        if link.find("playlist") >0 :
            downloadplaylist(link)
        else:
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
