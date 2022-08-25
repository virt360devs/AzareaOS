
import os
os.system("pip install pytube")
import pytube
from pytube import YouTube
def downloadyt():
  yturl = input("Url")
  #gets a "list" of videos with the url
  video = YouTube(yturl).streams.filter(file_extension='mp4')
  #filters out the first video from the "list"
  video1 = video.first()
  #downloads the vid to UserFiles
  video1.download(output_path='/home/virtual/Downloads/Azarea/UserFiles')
  print("complete!")
