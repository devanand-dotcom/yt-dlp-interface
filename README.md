# yt-dlp-interface 🎥🎵

A simple Python-based CLI for downloading YouTube videos and music using `yt-dlp`, with support for subtitles, playlists, and audio extraction.

## Features
- 📺 Download videos at custom resolution
- 🎵 Extract audio as MP3
- 📃 Subtitle download and embedding
- 📂 Playlist support
- ⚙️ Optional FFmpeg support

## How to Use
1. Install Python and [yt-dlp](https://github.com/yt-dlp/yt-dlp)
2. Run `python ytdlp-interface.py`
3. Follow the terminal instructions!

## Building an EXE
```bash
pip install pyinstaller
pyinstaller --onefile ytdlp-interface.py
