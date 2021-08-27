from setuptools import setup, find_packages

from json import load

# Load package version
with open('version.json') as f:
    version = load(f)['version']

# Load long description 
with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open("requirements.txt", encoding='utf-8') as f:
    requirements = f.read()

# Configure setup 
setup(
    name = 'sedona',
    version = version,
    author = 'Giovani Candido',
    author_email = 'giovcandido@outlook.com',
    license = 'GNU General Public License v3.0',
    description = 'Sedona is a free youtube mp3 downloader made with Python.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/giovcandido/sedona',
    packages = find_packages(),
    install_requires = [requirements],
    python_requires = '>=3.8',
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    entry_points = '''
        [console_scripts]
        sedona=sedona.__main__:main
    '''
)
