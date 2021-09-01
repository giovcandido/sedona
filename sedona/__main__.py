from sys import exit as sys_exit

from .cli import parse_arguments

from .Video import Video
from .Playlist import Playlist
from .Converter import Converter

from pytube.helpers import safe_filename

def main():
    # Getting proper arguments from the terminal
    args = parse_arguments()

    # Creating a list with multiples urls (if exists)
    urls = list()

    # Checking if the URL is text file or not
    if args.url.endswith('.txt'):
        try:
            # If its a text file, save all URL's in the variable for later download and conversion
            text_file = args.url

            with open(text_file) as f:
                urls = f.readlines()
        except FileNotFoundError as err:
            print(err)

            sys_exit(1)
    else:
        # If isn't a text file, save all URL's present in the arguments from terminal
        urls.append(args.url)
    
    # Downloading multiple url's
    for url in urls:
        # Checking if the URL is a video or a playlist
        if "playlist" not in url:
            # Video downloader
            try:
                # Download youtube video to temp directory
                video = Video(url)
            
                print('Downloading "%s"...' % (video.title))

                # Download the song in video format and return the correct path for conversion
                video_path = video.download_audio_stream()
                
                # Get video path and convert it to mp3 to "sedonaMP3" directory in home
                converter = Converter(video_path)

                print('Converting downloaded video to mp3...')

                # Convert the song to MP3, with a default bitrate of 256kbps
                converter.convert_audio_stream(video.filename)

                print('Done! File saved to your home directory.\n')
            except Exception as err:
                print(err)

                sys_exit(1)
        else:
            try:
                # Playlist downloader
                playlist = Playlist(url)
                
                print('Downloading and Converting Playlist "%s"...\n' % (playlist.title))

                # Every object "video_url" of a Playlist is a URL of Youtube
                for position, video_url in enumerate(playlist):
                    # Download youtube video to temp directory
                    video = Video(video_url)

                    track_number = str((position + 1)) + "." + " "

                    # Showing the track position and his title
                    print("Position: " + str((position + 1)))
                    print("Title: " + video.filename)
                    
                    # Download the song in video format, with the track number in playlist, and return the correct path for conversion
                    video_path = video.download_audio_stream(track_number)

                    # Update the playlist name to one allowed by the OS ("safe_filename"), upon creation of the specific directory
                    playlist_dir = safe_filename(playlist.title)

                    # Remove whitespaces from init and end of string
                    playlist_dir = playlist_dir.lstrip()
                    playlist_dir = playlist_dir.rstrip()

                    # Get video path and convert it to mp3 to playlist directory, in "sedonaMP3" directory
                    converter = Converter(video_path)

                    print('Converting downloaded video to mp3...')

                    # Convert the song to MP3, with his track number and a default bitrate of 256kbps
                    converter.convert_audio_stream(track_number + video.filename, playlist_dir)

                    print('Done! File saved to your home directory.\n')

                print('Playlist "%s" downloaded and converted with success!\n' % (playlist.title))
            except Exception as err:
                print(err)

                sys_exit(1)
            
