import youtube_dl

while True:
    url = input("Enter a YouTube URL: ")

    options = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]/best",
        "outtmpl": "%(title)s.%(ext)s",
    }

    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    cont = input("Do you want to continue downloading? (y/n) ")
    if cont.lower() != "y":
        break
