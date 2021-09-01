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
    version = __version__, # type: ignore
    author = __author__, # type: ignore
    author_email = __author_email__, # type: ignore
    license = 'GNU General Public License v3.0',
    description = __description__, # type: ignore
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/giovcandido/sedona',
    packages = find_packages(),
    install_requires = [requirements],
    python_requires = '>=3.8',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    entry_points = '''
        [console_scripts]
        sedona=sedona.__main__:main
    '''
)
