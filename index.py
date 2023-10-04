import pytube
import os
from pathlib import Path
from pytube.cli import on_progress

# Developer Muhammad Haris Maqsood
#  
"""  
 * 
 * This Downloader helps to download youtube video. 
 * 
 * @class       YouTubeDownloader 
 * @Developer   Muhammad Haris Maqsood 
 * @author      Haris-Technical-Solutions
 * @Whatsapp    +92-3105786021
"""

def complete_func(stream, path):
    """Prints a message when the download is complete."""
    print("\nDownload complete!")

def download_video(url, output_path):
    """Downloads a YouTube video."""
    try:
        # Get a YouTube object for the video we want to download.
        yt = pytube.YouTube(url, on_progress_callback=on_progress, on_complete_callback=complete_func, use_oauth=True, allow_oauth_cache=True)

        # Get the highest resolution stream of the video.
        stream = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()

        # Download the video.
        stream.download(output_path=output_path)
    except:
        print("An exception occurred")

def download_audio(url, output_path):
    """Downloads a YouTube audio."""
    try:
        # Get a YouTube object for the video we want to download.
        yt = pytube.YouTube(url, on_progress_callback=on_progress, on_complete_callback=complete_func, use_oauth=True, allow_oauth_cache=True)

        # Get the highest resolution stream of the video.
        stream = yt.streams.filter(only_audio=True).first()
        # Download the video.
        stream.download(output_path=output_path)
    except:
        print("\nAn exception occurred")

if __name__ == '__main__':

    download_url = input("Enter the download URL: ")
    while (download_url == ""):
       download_url = input("Enter the download URL: ")
    print("\n1. For Video Download")
    print("2. For Audio Download")
    format = input("\nEnter Selected option number: ")
    while (format != "1" and format != "2"):
        format = input("Enter Selected option number: ")
    # Get the output path from the user.
    path_to_download = str(os.path.join(Path.home(), 'Downloads\\Youtube'))
    path_to_download_audio = str(os.path.join(Path.home(), 'Downloads\\Youtube\\Audio'))
    path_to_download_video = str(os.path.join(Path.home(), 'Downloads\\Youtube\\Video'))
    if(format == "1"):
        format_type = "Video"
    elif(format == "2"):
        format_type = "Audio"

    output_path = input(f"Enter the output path (Default: {path_to_download}\\{format_type}): ")

    # Download the video.
    if(format == "1"):
        if(output_path == ""):
            output_path = path_to_download_video
        download_video(download_url, output_path)
    elif(format == "2"):
        if(output_path == ""):
            output_path = path_to_download_audio
        download_audio(download_url, output_path)