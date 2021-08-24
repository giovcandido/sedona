from setuptools import setup, find_packages

# Load long description 
with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open("requirements.txt", encoding='utf-8') as f:
    requirements = f.read()

# Configure setup 
setup(
    name = 'sedona',
    version = '0.1.0',
    author = 'Giovani Candido',
    author_email = 'giovcandido@outlook.com',
    license = 'GNU General Public License v3.0',
    description = 'Sedona is a free youtube mp3 downloader made with Python.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/giovcandido/sedona',
    py_modules = ['sedona', 'modules'],
    packages = find_packages(),
    include_package_data = True,
    install_requires = [requirements],
    python_requires = '>=3.8',
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    entry_points = '''
        [console_scripts]
        sedona=sedona:main
    '''
)
