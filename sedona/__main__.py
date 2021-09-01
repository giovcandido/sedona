from sys import exit

from .cli import parse_arguments

from .Downloader import Downloader
from .Converter import Converter

def main():
    args = parse_arguments()

    video_url = args.url

    # Download youtube video to temp directory
    try:
        downloader = Downloader(video_url)
    
        print('Downloading %s...' % (downloader.title))

        video_path = downloader.download_audio_stream()
    except ValueError as err:
        print(err)

        exit(1)
    
    # Get video and convert it to mp3 to sedona directory
    try:
        converter = Converter(video_path)

        print('Converting downloaded video to mp3...')

        converter.convert_audio_stream(downloader.filename)

        print('Done! File saved to your home directory.')
    except ValueError as err:
        print(err)
        
        exit(1)
