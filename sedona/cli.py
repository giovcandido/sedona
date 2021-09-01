from argparse import ArgumentParser

from pyfiglet import Figlet

from shutil import get_terminal_size

from .version import __version__
from .description import __description__

def parse_arguments():
    figlet = Figlet(font='standard')
    print(figlet.renderText('Sedona'))

    parser = ArgumentParser(description=__description__)
    
    # Set version text
    version_text = '%(prog)s {version}'.format(version=__version__)
    
    parser.add_argument('-v', '--version', action='version', version=version_text, help='show program version')

    parser.add_argument('url', metavar='URL', type=str, help='Video URL')

    return parser.parse_args()

def on_download_progress(stream, chunk, bytes_remaining):
    # Get total size of the file
    file_size = stream.filesize
    
    # Calculate bytes downloaded so far
    bytes_received = file_size - bytes_remaining
    
    # Calculate progress bar width
    width = int(get_terminal_size().columns * 0.55)

    # Calculate how much of the bar is filled
    filled = int(round(width * bytes_received / float(file_size)))
    
    # Set progress bar text
    progress_bar = '=' * filled + '.' * (width - filled)

    # Calculte downloaded percentage
    percentage = round(100.0 * bytes_received / float(file_size), 1)
    
    print('[%s] %.2f%%' % (progress_bar, percentage))
