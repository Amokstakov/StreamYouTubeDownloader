import pytube

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download('/home/sasha/Downloads')
