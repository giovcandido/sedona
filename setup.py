from setuptools import setup, find_packages

from pathlib import Path
from os.path import join


# Define base path relative to setup.py
base_dir = Path(__file__).parent


# Load version
exec(open(join(base_dir, 'sedona', 'version.py')).read())

# Load long description
with open(join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open(join(base_dir, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read()

# Configure setup
setup(
    name = 'sedona',
    version = __version__, # type: ignore
    author = 'Giovani Candido, Davi Neves',
    author_email = 'giovcandido@outlook.com, davivirgula@gmail.com',
    license = 'GNU General Public License v3.0',
    description = (
        'Sedona is a free YouTube & YT Music mp3 downloader for songs.'
    ),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/giovcandido/sedona',
    packages = find_packages(),
    install_requires = [requirements],
    python_requires = '>=3.8',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.8',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    entry_points = '''
        [console_scripts]
        sedona=sedona.__main__:main
    '''
)
