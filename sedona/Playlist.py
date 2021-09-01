from pytube import Playlist as PytubePlaylist

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
    
    def __create_playlist(self):
        self.__playlist = PytubePlaylist(self.__url)

    def __iter__(self):
        return self.__playlist.video_urls.__iter__()

    def __next__(self):
        return self.__playlist.video_urls.__next__
