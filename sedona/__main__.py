from sys import exit as sys_exit

from .cli import parse_arguments, print_separator

from .Video import Video
from .Playlist import Playlist
from .Converter import Converter

def main():
    # Get user arguments from sedona command
    args = parse_arguments()

    # Create a list to store the urls
    urls = list()

    # Check if it's necessary to read urls from text file
    if args.url.endswith('.txt'):
        # If it is, then read it from file
        urls = read_from_file(args.url)
    else:
        # Otherwise, it's a single url, store it in the list
        urls.append(args.url)
    
    # Walk through urls list downloading and converting the corresponding videos
    for url in urls:
        # Check if the url is a video
        if "playlist" not in url:
            # If so, let's download and convert it
            handle_video(url)
        else:
            # Otherwise, let's download and convert a playlist
            handle_playlist(url)

def read_from_file(filename):
    urls = None

    try:
        with open(filename) as f:
            urls = f.readlines()
    except FileNotFoundError as err:
        print(err)
        sys_exit(1)
    
    return urls

def handle_video(url):
    try:
        # Create video instance with the current url
        video = Video(url)

        print('Video title: %s' % (video.title))
        print('Duration: %s seconds' % (video.duration))
        print('Youtube channel: %s\n' % (video.channel))
    
        print('Downloading audio-only video...')

        # Download audio only video to the tmp directory
        video_path = video.download_audio_stream()
        
        # Create converter instance with the video path
        converter = Converter(video_path)

        print('Converting downloaded video to mp3...')

        # Get downloaded video and convert it to mp3, store it in home/SedonaMP3
        converter.convert_audio_stream(video.filename) # default bitrate = 256kbps

        print('Done! File saved to your home directory.')

        print_separator()

    except Exception as err:
        print(err)
        sys_exit(1)

def handle_playlist(url):
    try:
        # Create playlist instance with current url
        playlist = Playlist(url)
        
        print('=> Current playlist is "%s".\n' % (playlist.title))

        # Walk through all urls of the playlist                
        for number, video_url in enumerate(playlist):
            # Create video instance with the curl
            video = Video(video_url)
            
            # Show track number and its title
            print('Downloading "%s"...' % (video.title))
            
            # Download audio only video to the tmp directory
            video_path = video.download_audio_stream()

            # Create converter instance with the video path
            converter = Converter(video_path)

            print('Converting downloaded video to mp3...')
            
            # Add track number to filename
            filename = str((number + 1)) + "." + " " + video.filename

            # Get downloaded video and convert it to mp3, store it in home/SedonaMP3
            converter.convert_audio_stream(filename, playlist.directory_name) # default bitrate = 256kbps

            print('Done! File saved to your home directory.\n')

        print('=> Playlist "%s" downloaded successfully.\n' % (playlist.title))
    except Exception as err:
        print(err)
        sys_exit(1)
