from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Enter YouTube URL: ")
output_directory = input("Enter output directory: ")
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download(output_path=output_directory)