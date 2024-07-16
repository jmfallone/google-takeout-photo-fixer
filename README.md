# google-takeout-photo-fixer

Google Takeout Metadata seems to be split from the actual files when downloading. 

This is a somewhat simple tool designed to fix those. It's cross platform but mostly been tested
from WSL on Windows 11. 

It currently supports repairing the creation dates for mp4 and jpg files. Note that both the media's metadata and the file system's metadata will be updated.

**ONLY USE AT YOUR OWN RISK AND ENSURE YOU MAKE A BACKUP FIRST. I AM NOT RESPONSIBLE FOR ANY LOST DATA**

## Setup

python and ffmpeg are required.

    # recommend creating a venv to run the following commands:
    pip install -r requirements.txt
    python main.py --help


## Usage

    python main.py --help
    usage: Google Takeout Photo and Video Fixer [-h] source

    positional arguments:
    source      The unzipped directory (no subdirs please, run for each year)

    options:
    -h, --help  show this help message and exit
