from argparse import ArgumentParser

from .version import __version__

from .Downloader import Downloader
from .Converter import Converter

def parse_arguments():
    parser = ArgumentParser(description='Sedona is a free youtube downloader and mp3 converter.')
    
    # Set version text
    version_text = '%(prog)s {version}'.format(version=__version__)
    
    parser.add_argument('-v', '--version', action='version', version=version_text, help='show package version')

    parser.add_argument('url', metavar='URL', type=str, help='Video URL')

    return parser.parse_args()

def main():
    args = parse_arguments()

    video_url = args.url

    downloader = Downloader(video_url)
    
    print('Downloading %s...' % (downloader.title))

    video_path = downloader.download_audio_stream()

    converter = Converter(video_path)

    print('Converting downloaded video to mp3...')

    converter.convert_audio_stream(downloader.title)

    print('Done! File saved to your home directory.')
