import pytube

url = "https://www.youtube.com/watch?v=668nUCeBHyY"

youtube = pytube.YouTube(url)

video = youtube.streams.get_lowest_resolution()

video.download()