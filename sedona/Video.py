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
    def duration(self):
        m, s = divmod(self.__youtube.length, 60)
        h, m = divmod(m, 60)

        if(h > 0):
            time = str(h) + ':' + str(m) + ':' + str(s)
        else:
            time = str(m) + ':' + str(s)

        return time
    
    @property
    def channel(self):
        return self.__youtube.author
    
    @property
    def filename(self):
        basename = self.__audio_stream.default_filename

        return path.splitext(basename)[0]
    
    def __create_audio_stream(self):
        self.__youtube = YouTube(self.__url)

        self.__youtube.register_on_progress_callback(on_download_progress)
        self.__youtube.register_on_complete_callback(on_download_complete)

        self.__audio_stream = self.__youtube.streams.get_audio_only()

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
