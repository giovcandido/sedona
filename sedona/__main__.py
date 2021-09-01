from sys import exit

from .cli import parse_arguments

from .Video import Video
from .Playlist import Playlist
from .Converter import Converter

def main():
    args = parse_arguments()

    # Checking if the argument is related to a text file

    video_url = args.url

    # Checking if the URL is a video or a playlist
    if "playlist" not in video_url:
        # Video downloader
        try:
            # Download youtube video to temp directory
            video = Video(video_url)
        
            print('Downloading "%s"...' % (video.title))

            video_path = video.download_audio_stream()
        except ValueError as err:
            print(err)

            exit(1)
        
        # Video converter
        try:
            # Get video and convert it to mp3 to sedona directory
            converter = Converter(video_path)

            print('Converting downloaded video to mp3...')

            converter.convert_audio_stream(video.filename)

            print('Done! File saved to your home directory.')
        except ValueError as err:
            print(err)
            
            exit(1)
    else:
        # Playlist downloader
        try:
            playlist = Playlist(video_url)

            print('Download Playlist "%s"...' % (playlist.title))

            title_tracks, playlist_path = playlist.download_all()
        except ValueError as err:
            print(err)

            exit(1)
        
        # Playlist converter
        try:
            print('\nConverting Playlist "%s"...' % (playlist.title))
            
            # Get video from playlist and convert it to mp3 to sedona directory
            for position, video_path in enumerate(playlist_path):
                print("\nTitle: " + title_tracks[position])

                converter = Converter(video_path)

                print('Converting downloaded video to mp3...')

                converter.convert_audio_stream(title_tracks[position])

                print('Done! File saved to your home directory.')
        except ValueError as err:
            print(err)

            exit(1)

