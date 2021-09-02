from sys import exit as sys_exit

from .cli import parse_arguments, print_separator, print_arrow_message

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
    size_urls = len(urls)

    for position, url in enumerate(urls):
        # Check if the url is a video
        if "playlist" not in url:
            # If so, let's download and convert it
            handle_video(url, position, size_urls)
        else:
            # Otherwise, let's download and convert a playlist
            handle_playlist(url, position, size_urls)

def read_from_file(filename):
    urls = None

    try:
        with open(filename) as f:
            urls = f.read().splitlines()
    except FileNotFoundError as err:
        print(err)
        sys_exit(1)
    
    return urls

def handle_video(url, position, size_urls):
    try:
        # Create video instance with the current url
        video = Video(url)

        # Show some informations about track
        print(f'Video title: {video.title}')
        print(f'Duration: {video.duration}')
        print(f'YouTube channel: {video.channel}\n')
    
        print('Downloading audio-only video...')

        # Download audio only video to the tmp directory
        video_path = video.download_audio_stream()
        
        # Create converter instance with the video path
        converter = Converter(video_path)

        print('Converting downloaded video to mp3...')

        # Get downloaded video and convert it to mp3, store it in home/SedonaMP3
        converter.convert_audio_stream(video.filename) # default bitrate = 256kbps

        print('Done! File saved to your home directory.')

        # Don't print the separator in the last element
        if position < size_urls - 1:
            print_separator()

    except Exception as err:
        print(err)
        sys_exit(1)

def handle_playlist(url, position, size_urls):
    try:
        # Create playlist instance with current url
        playlist = Playlist(url)
        
        print_arrow_message(f'Current playlist is "{playlist.title}".\n')

        # Walk through all urls of the playlist                
        for number, video_url in enumerate(playlist):
            # Create video instance with the curl
            video = Video(video_url)
            
            # Show some informations about track
            print(f'Track number: {str((number + 1))}')
            print(f'Video title: {video.title}')
            print(f'Duration: {video.duration}')
            print(f'YouTube channel: {video.channel}\n')

            print('Downloading audio-only video...')
            
            # Download audio only video to the tmp directory
            video_path = video.download_audio_stream()

            # Create converter instance with the video path
            converter = Converter(video_path)

            print('Converting downloaded video to mp3...')
            
            # Add track number to filename
            filename = str((number + 1)) + "." + " " + video.filename

            # Get downloaded video and convert it to mp3, store it in home/SedonaMP3
            converter.convert_audio_stream(filename, playlist.directory_name) # default bitrate = 256kbps

            print('Done! File saved to your home directory.')

            # Don't print the separator in the last element
            if number < playlist.size - 1:
                print_separator()

        print_arrow_message(f'Playlist "{playlist.title}" downloaded successfully.', '\n')

        # Don't print the separator in the last element
        if position < size_urls - 1:
            print_separator()

    except Exception as err:
        print(err)
        sys_exit(1)
