from pytube import YouTube

from tempfile import gettempdir

from os import path, mkdir, remove

from .cli import on_download_progress

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

    @property
    def title(self):
        return self.__video.title
    
    @property
    def filename(self):
        return path.splitext(self.__video.default_filename)[0]
    
    def __create_video(self):
        youtube = YouTube(self.__url, on_progress_callback=on_download_progress)

        self.__video = youtube.streams.get_audio_only()

    def download_audio_stream(self):
        temp_dir = gettempdir()

        temp_dir = path.join(temp_dir, 'Sedona')

        if not path.exists(temp_dir):
            mkdir(temp_dir)

        output_file = path.join(temp_dir, self.__video.default_filename)
        
        if path.exists(output_file):
            remove(output_file)

        self.__video.download(output_path=temp_dir)

        return output_file
