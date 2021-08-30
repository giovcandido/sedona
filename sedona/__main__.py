from argparse import ArgumentParser

from sys import exit

from pyfiglet import Figlet

from .version import __version__
from .description import __description__

from .Downloader import Downloader
from .Converter import Converter

def parse_arguments():
    figlet = Figlet(font='standard')
    print(figlet.renderText('Sedona'))

    parser = ArgumentParser(description=__description__)
    
    # Set version text
    version_text = '%(prog)s {version}'.format(version=__version__)
    
    parser.add_argument('-v', '--version', action='version', version=version_text, help='show program version')

    parser.add_argument('url', metavar='URL', type=str, help='Video URL')

    return parser.parse_args()

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

        converter.convert_audio_stream(downloader.title)

        print('Done! File saved to your home directory.')
    except ValueError as err:
        print(err)
        
        exit(1)
