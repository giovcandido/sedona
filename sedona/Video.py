from pytube import YouTube

from tempfile import gettempdir

from os import path, mkdir, remove

from .cli import on_download_progress, on_download_complete

class Video:

    def __init__(self, url = None):
        self.__url = url

        if self.__url is not None:
            self.__create_audio_stream()

    @property
    def url(self):  
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url

        if url is not None:
            self.__create_audio_stream()

    @property
    def title(self):
        return self.__audio_stream.title
    
    @property
    def filename(self):
        basename = self.__audio_stream.default_filename

        return path.splitext(basename)[0]
    
    def __create_audio_stream(self):
        youtube = YouTube(self.__url)

        youtube.register_on_progress_callback(on_download_progress)
        youtube.register_on_complete_callback(on_download_complete)

        self.__audio_stream = youtube.streams.get_audio_only()

    def download_audio_stream(self):
        temp_dir = gettempdir()

        temp_dir = path.join(temp_dir, 'Sedona')

        if not path.exists(temp_dir):
            mkdir(temp_dir)

        filename = self.__audio_stream.default_filename
        
        output_file = path.join(temp_dir, filename)
        
        if path.exists(output_file):
            remove(output_file)

        self.__audio_stream.download(output_path=temp_dir, filename=filename)

        return output_file
