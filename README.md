# Sedona - a free YouTube mp3 downloader for songs

[![PyPI][pypi-badge]][pypi-link]
[![PyPI - Downloads][install-badge]][install-link]
[![PyPI - Status][status-badge]][status-link]
[![PyPI - License][license-badge]][license-link]

<p align="center">
    <img src="https://github.com/giovcandido/sedona/blob/master/demos/playlist_download.gif?raw=true" alt="Sedona downloading a playlist">
</p>

Download all your favorite songs with an easy-to-use cli tool.

## Contents

- [About](#about)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contribute](#contribute)

## About

Sedona is cli tool that makes it easy to download YouTube videos and playlists and have them converted to mp3 format with 256kbps. You can use it directly with a video or playlist URL or you can create a text file with as many URLs as you want and have Sedona process it.

Our tool is the best YouTube to MP3 Converter. You get free and unlimited downloads with high quality audio. Not only you can use it as much as you want, but you can also use it wherever you want: Sedona is cross-plataform and supports many operating system, such as Windows, Mac and Linux!

It's been made with Python 3.8 and tested on Linux and Windows 10.

## Usage

In order to download a YouTube video with Sedona, go to your command line and execute:
```bash
sedona [video_url]
```

If you want to download a playlist, you can also do as explained above:
```bash
sedona [playlist_url]
```

If you wish to download multiple videos and playlists, you can create a text file like this one:
```
https://www.youtube.com/watch?v=MktSE45zlrI
https://www.youtube.com/watch?v=zyXmsVwZqX4
https://www.youtube.com/watch?v=3nQNiWdeH2Q
```

Now, all you have to do is:
```bash
sedona [file_path]
```

In case you need it, there's a help option available:
```bash
sedona --help
```

Moreover, you can check the program version with:
```bash
sedona --version
```

## Demos

It's important to note that the URL contains special characters and the shell may misinterpret it.

Having said that, you should use quotation marks to prevent bad processing of the URLs.

In order to download a video, you should run:
```bash
sedona "https://www.youtube.com/watch?v=MktSE45zlrI"
```

For Bash and PowerShell, the above choice is a good one. 

However, if you use ZSH, you may not need to use quotation marks, because it's smart and will automatically use 'escapes'. You paste the URL into ZSH and you will have it like this:
```
sedona https://www.youtube.com/watch\?v\=MktSE45zlrI
```

### Video download

I use ZSH, so I won't put quotation marks.

Since the URLs have 'escapes' already, you must run without quotation marks as well.

Let's execute:
```
sedona https://www.youtube.com/watch\?v\=MktSE45zlrI
```

<p align="center">
    <img src="https://github.com/giovcandido/sedona/blob/master/demos/video_download.gif?raw=true" alt="Sedona downloading a video">
</p>

### Playlist download

Now, let's download a playlist:
```
sedona https://www.youtube.com/playlist\?list\=PLGtghrm-sc-KI9pS5w6jipUCxjdUSuv1K
```

The mp3 files will be numbered according to the playlist ordering. Addionatilly, all files will be stored in a directory with the same name as the playlist. Actually, it's not always the same name, once we have to choose a safe name.

<p align="center">
    <img src="https://github.com/giovcandido/sedona/blob/master/demos/playlist_download.gif?raw=true" alt="Sedona downloading a playlist">
</p>

### Text file download

Let's use a text file to download some videos.

Create a text file 'urls.txt' as the one presented in the usage section.

Note that the text file should have one URL per line and there's no need to use quotation marks.

If you created the file in your currrent directory, execute:
```
sedona urls.txt
```

<p align="center">
    <img src="https://github.com/giovcandido/sedona/blob/master/demos/text_download.gif?raw=true" alt="Sedona downloading from a text file">
</p>

### Output directory

The default output directory of Sedona is SedonaMP3, which is created automatically in your user directory. If you're on Linux, that's your home directory.

<p align="center">
    <img src="https://github.com/giovcandido/sedona/blob/master/demos/show_output.gif?raw=true" alt="Showing output directory">
</p>

## Requirements

Check requirements.txt to see a complete list of dependencies. But, don't worry about them. They are automatically installed for you.

However, ffmpeg is required for the MP3 conversion, you need to install it on your OS. If you're on Linux, you may not need to install it or you can do so through your package manager. 

If you're using a Debian-based distro, you can run:
```bash
sudo apt install ffmpeg 
```

If you're using a Fedora-based distro, you can run:
```bash
sudo dnf install ffmpeg 
```

If you're using an OpenSUSE-based distro, you can run:
```bash
sudo zypper install opi
sudo opi codecs 
```

If you're using an Arch-based distro, you can run:
```bash
sudo pacman -S ffmpeg
```

Additionally, if you're using any another Linux OS, you can download the tar file [here](https://ffmpeg.org/download.html) and install it manually.

If you are a MacOS (or even a Linux) user, you can use [Homebrew](brew.sh) to install ffmpeg. Simply execute:
```bash
brew install ffmpeg
```

In case you are a Windows user, you can use [Chocolatey](https://chocolatey.org/install) to install it by running the command:
```bash
choco install ffmpeg
```

Remember to open CMD or PowerShell as an administrator, or you can use [gsudo](https://github.com/gerardog/gsudo) as I do.

You can also install it manually on MacOS or Windows. For Windows, [download](https://ffmpeg.org/download.html) it and follow a [guide](https://www.wikihow.com/Install-FFmpeg-on-Windows).

## Installation

There are two ways you can install Sedona. You can either install it from source or you can get it using pip.

If you want to get it from source, download the latest release on GitHub. Then, extract the source code and run:
```bash
python3 setup.py install
```

If you want to install Sedona with pip, you just need to run:
```bash
pip3 install sedona
```

You can also run:
```bash
sudo pip3 install sedona
```

## Contribute

Feel free to reach out and contribute. We can add more features to Sedona and maybe implement our own backend.

You can also help me test it on MacOS.


[pypi-badge]: https://img.shields.io/pypi/v/sedona.svg
[pypi-link]: https://pypi.org/project/sedona
[install-badge]: https://img.shields.io/pypi/dm/sedona?label=pypi%20installs
[install-link]: https://pypistats.org/packages/sedona
[license-badge]: https://img.shields.io/pypi/l/sedona.svg
[license-link]: https://pypi.python.org/pypi/sedona/
[status-badge]: https://img.shields.io/pypi/status/sedona.svg
[status-link]: https://pypi.python.org/pypi/sedona/
