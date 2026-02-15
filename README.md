# download-youtube-video
Terminal tool for downloading YouTube video from URL  
Written purely in Python

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
...

## Installation
1. Clone the repository :
```bash
git clone https://github.com/PaulLam0907/download-youtube-video.git
```

2. Install dependencies :
- pytubefix
- moviepy

## Usage
To launch the app, simply run the `main.py`

Alternatively, using the `download.py` module :
```Python
from download import Download

dl = Download()

# change default download destination
dl.path = "location where video is downloaded"

# download the video
dl.url("youtube url here", high_quality = True)
dl.url(
    ["url1", "url2", "url3"],
    high_quality = True
)

# launch file explorer and view downloaded video
dl.view()
```

## Contributing
1. Fork the repository.
2. Create a new branch : `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch : `git push origin feature-name`.
5. Create a pull request.

## License
...

![Build Status](https://travis-ci.org/PaulLam0907/download-youtube-video.svg?branch=main)
