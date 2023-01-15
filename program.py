from pytube import YouTube
import os
import time

url_list = []
downloaded_music_list = []

user_music_path = str(open("path.txt").read())

def checkTXTfiles():
    if open("path.txt").read() != "" and open("urls.txt").read() != "":
        pass
    else:
        print("path.txt or urls.txt is can't be null value")
        time.sleep(5)
        exit()

def getTitle(targetlink):
    youtubeLink = YouTube(targetlink)
    return youtubeLink.title

def Download(link):
    global yt
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path = user_music_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def CheckUrlsTXT():
    urls_txt = open("urls.txt", "r")
    while True:
        url = urls_txt.readline()
        if url != "":
            if getTitle(url) not in downloaded_music_list:
                try:
                    print(f"Downloading...  {getTitle(url)}")
                    Download(url)
                    print(f"Downloaded : {yt.title}")
                except:
                    print("Cant Downloaded : ", yt.title)
                    pass
            else:
                print("IT'S ALREADY DOWNLOADED : ", getTitle(url))
                pass
        else:
            break

def checkDownloadedMusics():
    musicName = os.listdir(user_music_path)

    for dosya in musicName:
        if dosya.endswith(".mp3"):
            fold = dosya.replace(".mp3", "")
            downloaded_music_list.append(fold)
    CheckUrlsTXT()

checkTXTfiles()
checkDownloadedMusics()