import logging
from tkinter.messagebox import showinfo
from webbrowser import open_new

from preferences import Preferences


def open_preferences():
    logging.info('Opened Preferences.')
    preferences_window = Preferences('Preferences', 240, 230)
    preferences_window.run()


def show_app_info():
    message = '''
        SaveTube - YouTube Video Downloader

        SaveTube is a simple and user-friendly YouTube video downloader that empowers you to save YouTube videos hassle-free.

        Steps to Use SaveTube:
        1. Paste the YouTube URL: Copy the URL of the YouTube video you want to download.
        2. Specify the File Name: Enter a meaningful name for your downloaded file.
        3. Choose Download Type:
            - Video: Download the complete video.
            - Audio: Download only the audio.
        4. Click the Appropriate Button: SaveTube will handle the download process for you.

        Copyright Notice:
        - SaveTube respects the copyrights and intellectual property rights of content creators on YouTube.
        - Ensure that you possess the necessary permissions to download and use the content.
        - SaveTube is intended for personal use only.

        Note: 
        - If the video contains multiple audio tracks and you choose to download the audio, SaveTube will fetch the first audio track.
        - If you opt to download the video, SaveTube will retrieve the original audio.

        Version: 1.6
        Developer: CrazyFlyKite
        Copyright ©, CrazyFlyKite, All Rights Reserved
        '''

    logging.info('Opened More Info.')
    showinfo('Info', message)


def open_youtube():
    logging.info('Opened YouTube.')
    open_new('https://www.youtube.com/')
