from pytube import Playlist as PytubePlaylist

from .Video import Video

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

    def download_all(self):
        
        # List of title and path to output
        title_playlist_files = list()
        output_files = list()

        # Every object in "video_urls" of a Playlist is a URL of Youtube
        for position, video_url in enumerate(self.__playlist.video_urls):
            # Download youtube video to temp directory
            video = Video(video_url)

            track_number = str((position + 1)) + "." + " "

            # Showing the track position and his title
            print("\nPosition: " + str((position + 1)))
            print("Title: " + video.filename)
            
            # Download the track
            video_path = video.download_audio_stream(track_number)

            # Save his track title (for convertion)
            title_playlist_files.append(track_number + video.filename)

            # Save his temp path to a list (for convertion)
            output_files.append(video_path)
            
        return title_playlist_files, output_files
