from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=wXTJBr9tt8Q&ab_channel=TheBeatlesVEVO')
print(yt.streams.filter(only_audio=True,file_extension='mp4'))
stream = yt.streams.filter(only_audio=True,file_extension='mp4')
stream[0].download('/Users/fernando/Downloads')
