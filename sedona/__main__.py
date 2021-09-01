from sys import exit

from .cli import parse_arguments

from .Video import Video
from .Converter import Converter

def main():
    args = parse_arguments()

    # Checking if the argument is related to a text file

    video_url = args.url

    # Checking if the URL is a video or a playlist


    # Download youtube video to temp directory
    try:
        video = Video(video_url)
    
        print('Downloading %s...' % (video.title))

        video_path = video.download_audio_stream()
    except ValueError as err:
        print(err)

        exit(1)
    
    # Get video and convert it to mp3 to sedona directory
    try:
        converter = Converter(video_path)

        print('Converting downloaded video to mp3...')

        converter.convert_audio_stream(video.filename)

        print('Done! File saved to your home directory.')
    except ValueError as err:
        print(err)
        
        exit(1)
