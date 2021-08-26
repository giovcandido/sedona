from pytube import YouTube

class Downloader:

    def __init__(self, url = None):
        self.__url = url

        if self.__url is not None:
            self.__create_video()

    @property
    def url(self):  
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url

        if url is not None:
            self.__create_video()
    
    def __create_video(self):
        youtube = YouTube(self.__url)

        self.__video = youtube.streams.get_audio_only()
    
    @property
    def title(self):
        return self.__video.title
