# winget install Gyan.FFmpeg
#pip install yt-dlp
#Run in power shell

import yt_dlp

url = input("Enter the YouTube video URL: ")

yt_dlp.YoutubeDL(
    {"format" : "bestvideo+bestaudio"}
    ).download([url])