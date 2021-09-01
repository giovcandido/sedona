from pydub import AudioSegment

from os import path, mkdir

class Converter:

    def __init__(self, path):
        self.__path = path
    
    @property
    def path(self):  
        return self.__path
    
    @path.setter
    def path(self, path):
        self.__path = path

    def convert_audio_stream(self, title, playlist_dir = None):
        audio_stream = AudioSegment.from_file(self.__path)

        sedona_dir = path.expanduser('~')
        sedona_dir = path.join(sedona_dir, 'SedonaMP3')

        if not path.exists(sedona_dir):
            mkdir(sedona_dir)

        # Creating playlist folder if exists
        if playlist_dir:
            sedona_dir = path.join(sedona_dir, playlist_dir)
            if not path.exists(sedona_dir):
                mkdir(sedona_dir)

        output_file = path.join(sedona_dir, title) + '.mp3'

        audio_stream.export(output_file, format="mp3", bitrate="256k")
