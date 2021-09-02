# Sedona

[![PyPI][pypi-badge]][pypi-link]
[![PyPI - Downloads][install-badge]][install-link]
[![PyPI - License][license-badge]][license-link]
[![PyPI - Status][status-badge]][status-link]

Sedona is a free youtube mp3 downloader made with Python.

It's been made with Python 3.8 and tested on Linux and Windows 10.

# Features

- Best YouTube to MP3 Converter with 256kbps high quality audio!
- Free and unlimited conversions and downloads!
- Support YouTube Video, YouTube Playlist and a text file with many links as you wish!
- Most platforms supported including Windows, Mac and Linux!

# Usage
In order to use Sedona, go to your command line and type:
```bash
sedona [youtube_url]
```

# Example
As an example, you can run:

* For bash, cmd/Powershell (Windows) and alike:
```bash
sedona "https://www.youtube.com/watch?v=ifGUT86tGz4"
```

* For zshell and alike:
```
sedona https://www.youtube.com/watch?v=ifGUT86tGz4
```

If you'd like to know more information about Sedona, run:
```bash
sedona --help
```

# Dependencies
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
sudo zypper in opi
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

# How to install
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

# Contribute
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
