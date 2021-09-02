from argparse import ArgumentParser

from colorama import init, Fore

from pyfiglet import Figlet

from shutil import get_terminal_size

from .version import __version__
from .description import __description__

def parse_arguments():
    init(autoreset=True)

    figlet = Figlet(font='standard')

    print(Fore.LIGHTRED_EX + figlet.renderText('Sedona'))

    parser =  ArgumentParser(description=__description__)

    # Add the URL argument, for a video/playlist (one URL) or a text file (multiple URL's)
    parser.add_argument('url', metavar='url', type=str, help='video/playlist url or text file with urls')

    # Set version text
    version_text = '%(prog)s {version}'.format(version=__version__)
    
    parser.add_argument('-v', '--version', action='version', version=version_text, help='show program version')

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
    
    # Print progress bar
    print(Fore.LIGHTGREEN_EX + '[%s] %.2f%%' % (progress_bar, percentage), end='\r')

def on_download_complete(stream, file_path):
    print()

def print_arrow_message(message, prefix = None):
    message = f'{Fore.LIGHTCYAN_EX}=> {message}'
    
    if prefix:
        message = prefix + message

    print(message)

def print_separator():
    separator = '\n' + get_terminal_size().columns * '-' + '\n'

    print(Fore.LIGHTCYAN_EX + separator)
