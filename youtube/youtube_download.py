import os
from pytube import YouTube

# Object Oriented JavaScript Tutorial #1 - Introduction. (7.5 mins)
# link = "https://www.youtube.com/watch?v=4l3bTDlT6ZI&list=PLQyna87O3r-U_JyJGkiM6rKIfO1VLKmlp&index=11"
link = "https://www.youtube.com/watch?v=CnfitL4Rl0o"

yt = YouTube(link)
OUTPUT_PATH = "youtube_downloads"
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
# FILENAME = "Object Oriented JavaScript Tutorial #1 - Introduction" + ".mp4"
FILENAME = "bully juice workout" + ".mp4"

try:
    yt.streams.filter(progressive=True,
                      file_extension="mp4").first().download(output_path=OUTPUT_PATH,
                                                             filename=FILENAME)
except Exception as e:
    print(f"Some Error!: {e}")
print('Task Completed!')
