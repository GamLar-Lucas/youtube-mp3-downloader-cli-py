"""
This script provides functionality to:
1. Download YouTube videos and convert to MP3 audio format.
2. Clean video titles to create safe filenames.

Dependencies:
- yt_dlp: For downloading YouTube videos.
- ffmpeg: Required for audio processing.

Usage:
Run the script and provide a YouTube video URL when prompted.

Created by: 
GamLar-Lucas
"""

import re
import yt_dlp

def clean_filename(title):
    clean_filename = re.sub(r'[<>:"/\\|?*]', '', title)  #Remove Invalid filename Characters
    return clean_filename

def download_video(url, save_path='./Download'):
    try:
        # Extract metadata first
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Fetch metadata only
            original_title = info_dict.get('title',"Unknown Title") #Fetch Title
            filename = clean_filename(original_title) # Fix Filename
            ydl_opts = {
                'outtmpl': f'{save_path}/{filename}.%(ext)s',  # Output format
                'format': 'best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url]) # Download File
                print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

def process_video_urls_from_file(filename):
    try:
        # Open the file and read each line (URL)
        with open(filename, 'r') as file:
            video_urls = file.readlines()  
        # Remove any extra whitespace or newline characters from each URL
        video_urls = [url.strip() for url in video_urls]
        # Process each video URL
        for url in video_urls:
            download_video(url)

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_multiple_links():
    filename = input("Enter the path to the .txt file containing YouTube video URLs: ").strip()
    process_video_urls_from_file(filename)

def handle_single_link():
    while True:
        video_url = input("Enter the YouTube video URL: ").strip()
        if "youtube" in video_url.lower():
            download_video(video_url)
            break
        elif "exit" in video_url.lower():
            break
        else:
            print("Invalid YouTube URL. Please try again or type 'exit' to quit.")

def main():
    while True:
        # Prompt the user to choose whether they want multiple links or a single link
        choose_inputType = input("You have multiple links to download? [Y/N]: ").strip().lower()
        if choose_inputType == "y":
            handle_multiple_links()
        elif choose_inputType == "n":
            handle_single_link()
        elif not choose_inputType:
            # If the input is blank, ask again
            print("Input cannot be blank. Please enter 'Y' or 'N'.")
        elif "exit" in choose_inputType:
            # Allow the user to exit the program at any time
            print("Exiting program...")
            break
        else:
            # Handle invalid input
            print("Invalid input. Please enter 'Y' or 'N'.")

# Entry point of the script
if __name__ == "__main__":
    main()
