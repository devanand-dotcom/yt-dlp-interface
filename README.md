# yt-dlp-interface 🎥🎵

A simple Python-based CLI for downloading YouTube videos and music using `yt-dlp`, with support for subtitles, playlists, and audio extraction.

## ✨ Features
- 📺 Download videos at custom resolution
- 🎵 Extract audio as MP3
- 📃 Subtitle download and embedding
- 📂 Playlist support
- ⚙️ Optional FFmpeg support

## ▶️ How to Use
1. Install Python, [yt-dlp](https://github.com/yt-dlp/yt-dlp), [FFmpeg](https://ffmpeg.org/) (for advanced features like audio extraction, subtitle embedding, merging)
2. Run `python ytdlp-interface.py`
3. Follow the terminal instructions!

---

## 🛠️ Building the App

### 🪟 Windows (.exe)
```bash
# Step 1: Install PyInstaller
pip install pyinstaller

# Step 2: (Optional) Add ffmpeg to PATH
# Example:
set PATH=%PATH%;C:\path\to\ffmpeg\bin

# Step 3: Build executable
pyinstaller --onefile ytdlp-interface.py
```

### 🪟  🍎 macOS (.exe)
```bash
# Step 1: Install PyInstaller
pip install pyinstaller

# Step 2: (Optional) Install ffmpeg if needed
brew install ffmpeg

# Step 3: Build the binary
pyinstaller --onefile ytdlp-interface.py

```

### 🪟  🐧 Linux (.exe)
```bash
# Step 1: Install PyInstaller
pip install pyinstaller

# Step 2: (Optional) Install ffmpeg if needed
sudo apt install ffmpeg

# Step 3: Build the binary
pyinstaller --onefile ytdlp-interface.py

```

📥 Download the App
https://github.com/devanand-dotcom/yt-dlp-interface/releases
```
# Just double-click the .exe after downloading
⚠️ If Windows warns you, click “More info” → “Run anyway”

Let me know if you also want a badge (like “Made with Python” or “MIT License”), or if you’d like to add screenshots, FAQs, or contributors section.


