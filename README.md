# Sedona
Sedona is a free youtube mp3 downloader made with Python.

It's been made with Python 3.8 and tested on Linux.

# Dependencies
Check requirements.txt to see a complete list of dependencies. But, don't worry about them. They are automatically installed for you.

The FFmpeg package is required for the MP3 conversion, you need to install it on your OS. If you're on Linux, you may not need to install it or you can do so through your package manager. If your on Windows, for example, follow some guide like [this one](https://www.wikihow.com/Install-FFmpeg-on-Windows).

# How to install
There are two ways you can install Sedona. You can either install it from source or you can get it using pip.

If you want to get it from source, download the latest release on GitHub. Then, extract the source code and run:
```
python3 setup.py install
```

If you want to install Sedona with pip, you just need to run:
```
pip3 install sedona
```

You can also run:
```
sudo pip3 install sedona
```

# How to use
In order to use Sedona, go to your command line and type:
```
sedona [youtube_url]
```

# Example
As an example, you can run:
```
sedona https://www.youtube.com/watch?v=ifGUT86tGz4
```

If you'd like to know more information about Sedona, run:
```
sedona --help
```

# Contribute
Feel free to reach out and contribute. We can add more features to Sedona and maybe implement our own backend.

You can also help me test it on Windows and MacOS.
