from pytube import YouTube

from tempfile import gettempdir

from os import path, mkdir

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

    def download_audio_stream(self):
        temp_dir = gettempdir()

        temp_dir = path.join(temp_dir, 'sedona')

        if not path.exists(temp_dir):
            mkdir(temp_dir)

        return self.__video.download(output_path=temp_dir)
