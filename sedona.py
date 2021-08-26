from argparse import ArgumentParser

from modules.Downloader import Downloader
from modules.Converter import Converter

def parse_arguments():
    parser = ArgumentParser(description="Sedona is a free youtube downloader and mp3 converter.")
    
    parser.add_argument('url', metavar='URL', type=str, help="Video URL")

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

    print('Done! File saved to your music directory.')
