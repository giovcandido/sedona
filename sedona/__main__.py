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
            
            # Get video and convert it to mp3 to sedona directory
            converter = Converter(video_path)

            print('Converting downloaded video to mp3...')

            converter.convert_audio_stream(video.filename)

            print('Done! File saved to your home directory.')
        except ValueError as err:
            print(err)
            
            exit(1)
    else:
        try:
            # Playlist downloader
            playlist = Playlist(video_url)
            
            print('Downloading and Converting Playlist "%s"...' % (playlist.title))

            # Every object "video_url" of a Playlist is a URL of Youtube
            for position, video_url in enumerate(playlist):
                # Download youtube video to temp directory
                video = Video(video_url)

                track_number = str((position + 1)) + "." + " "

                # Showing the track position and his title
                print("\nPosition: " + str((position + 1)))
                print("Title: " + video.filename)
                
                # Download the track
                video_path = video.download_audio_stream(track_number)

                # Get video and convert it to mp3 to sedona directory
                converter = Converter(video_path)

                print('Converting downloaded video to mp3...')

                converter.convert_audio_stream(track_number + video.filename)

                print('Done! File saved to your home directory.')

            print('\nPlaylist "%s" downloaded and converted with success!' % (playlist.title))
        except ValueError as err:
            print(err)

            exit(1)
