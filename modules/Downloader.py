import pafy

from tempfile import gettempdir

from os import path, mkdir, remove

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
        self.__video = pafy.new(self.__url)
    
    @property
    def title(self):
        return self.__video.title

    def download_audio_stream(self):
        temp_dir = gettempdir()

        temp_dir = path.join(temp_dir, 'sedona')

        if not path.exists(temp_dir):
            mkdir(temp_dir)
        
        best_audio = self.__video.getbestaudio()
        
        output_file = path.join(temp_dir, best_audio.filename)

        if path.exists(output_file):
            remove(output_file)

        best_audio.download(filepath=temp_dir)

        return output_file
