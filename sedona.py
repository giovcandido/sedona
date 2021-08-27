from argparse import ArgumentParser

from json import load

from modules.Downloader import Downloader
from modules.Converter import Converter

def parse_arguments():
    parser = ArgumentParser(description='Sedona is a free youtube downloader and mp3 converter.')
    
    # Load package version
    with open('version.json') as f:
        version = load(f)['version']

    # Set version text
    version_text = '%(prog)s {version}'.format(version=version)
    
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
