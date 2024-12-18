# 🎵 YouTube Audio Downloader

## Overview
A Python utility for downloading and converting YouTube videos to high-quality MP3 audio files. Supports single and batch downloads with robust filename sanitization.

## 🌟 Features
- Download single YouTube video
- Batch download from URL list
- High-quality 192 kbps MP3 conversion
- Filename sanitization
- User-friendly CLI interface

## 📦 Prerequisites
- Python 3.x
- `yt-dlp`
- `ffmpeg`

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/GamLar-Lucas/youtube-mp3-downloader-cli-py.git
cd youtube-audio-downloader
```

### 2. Install Dependencies
```bash
pip install yt-dlp
```

### 3. Install FFmpeg
- **Windows**: Download from [FFmpeg Official Site](https://ffmpeg.org/download.html)
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`

## 🚀 Usage

### Single Video Download
```bash
python youtube_downloader.py
# Choose 'N' when prompted
# Enter a single YouTube URL
```

### Batch Download
1. Create a text file (e.g., `urls.txt`) with YouTube URLs
2. Run the script
3. Choose 'Y' when prompted
4. Provide the path to your URLs text file

### Example `urls.txt`
```
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2
https://www.youtube.com/watch?v=example3
```

## 📝 Notes
- Downloaded audio saves in `./Download` directory
- Supports various YouTube video formats
- Extracts high-quality audio

## 🛡️ Error Handling
- Validates YouTube URLs
- Handles file not found errors
- Provides user-friendly error messages

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📌 Limitations
- Requires active internet connection
- Depends on YouTube's URL structure
- May be affected by YouTube's terms of service

## 📃 License
MIT License

## 👤 Author
GamLar-Lucas

## 🆘 Support
Open an issue in the GitHub repository for any problems or feature requests.