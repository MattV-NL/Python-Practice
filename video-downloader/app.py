from pytube import YouTube
from sys import argv

link = argv[1]

print("the link is: ", link)

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_lowest_resolution()
yd.download("./downloads")