from pytube import Playlist as PytubePlaylist

from pytube.helpers import safe_filename

class Playlist:

    def __init__(self, url = None):
        self.__url = url

        if self.__url is not None:
            self.__create_playlist()

    @property
    def url(self):  
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url

        if url is not None:
            self.__create_playlist()

    @property
    def title(self):
        return self.__playlist.title

    @property
    def size(self):
        return self.__playlist.length

    @property
    def directory_name(self):
        # Create safe_filename from playlist title
        directory_name = safe_filename(self.__playlist.title)

        # Remove trailing characters from beginning and end of playlist_dir
        directory_name = directory_name.lstrip().rstrip()

        return directory_name
    
    def __create_playlist(self):
        self.__playlist = PytubePlaylist(self.__url)

    def __iter__(self):
        return self.__playlist.video_urls.__iter__()

    def __next__(self):
        return self.__playlist.video_urls.__next__
