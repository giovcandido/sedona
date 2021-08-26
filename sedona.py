from argparse import ArgumentParser

from modules.Downloader import Downloader

def parse_arguments():
    parser = ArgumentParser(description="Sedona is a free youtube downloader and mp3 converter.")
    
    parser.add_argument('url', metavar='URL', type=str, help="Video URL")

    return parser.parse_args()

def main():
    args = parse_arguments()

    video_url = args.url

    downloader = Downloader(video_url)

    video_path = downloader.download_audio_stream()

    print(video_path)
