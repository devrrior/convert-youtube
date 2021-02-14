from pytube import YouTube

class YoutubeDownload:

    def __init__(self,url):
        self.__url = url

    # Functions

    def download_audio(self):
        link = YouTube(self.__url)
        audio = link.streams.filter(only_audio=True,file_extension='mp4')
        audio[0].download('/Users/fernando/Downloads')

    def get_url(self):
        return self.__url

    def set_url(self,new_url):
        self.__url = new_url