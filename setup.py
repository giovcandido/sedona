from setuptools import setup, find_packages

from os.path import join

# Load version
exec(open(join('sedona', 'version.py')).read())

# Load author
exec(open(join('sedona', 'author.py')).read())

# Load author email
exec(open(join('sedona', 'author_email.py')).read())

# Load description
exec(open(join('sedona', 'description.py')).read())

# Load long description 
with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

# Load requirements
with open("requirements.txt", encoding='utf-8') as f:
    requirements = f.read()

# Configure setup 
setup(
    name = 'sedona',
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    license = 'GNU General Public License v3.0',
    description = __description__,
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
