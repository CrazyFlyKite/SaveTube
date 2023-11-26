import logging
from functools import cache
from pathlib import Path
from tkinter.messagebox import showinfo, showwarning

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

from data_manager import DataManager


class Downloader:
    def __init__(self, url: str, filename: str, directory: Path, quality: str = 'high'):
        """
        Initialize the Downloader object.

        :param url: The URL of the YouTube video.
        :param filename: The desired filename for the downloaded video or audio.
        :param directory: The directory where the video or audio will be saved.
        :param quality: The quality of the video ('high' or 'low'). Defaults to 'high'.
        """

        self.__url = url
        self.__filename = filename
        self.__directory = directory
        self.__quality = quality

    @cache
    def download_video(self) -> None:
        """
        Download a YouTube video based on the provided URL, filename, directory and quality.
        """

        # Load default video format from preferences
        data_manager = DataManager()
        file_format = data_manager.load_preferences().get('default-video-format')

        # If the filename does not have an extension, append the default video format
        if '.' not in self.__filename:
            self.__filename = f'{self.__filename}.{file_format}'

        try:
            # Initialize YouTube object and fetch the appropriate stream based on quality
            youtube = YouTube(self.__url)
            video = None

            match self.__quality.lower():
                case 'high':
                    video = youtube.streams.get_highest_resolution()
                    logging.info('Selected high-quality video stream.')
                case 'low':
                    video = youtube.streams.get_lowest_resolution()
                    logging.info('Selected low-quality video stream.')
                case other:
                    video = youtube.streams.get_highest_resolution()
                    logging.info('Selected high-quality video stream.')
                    logging.error(f'Unexpected quality value: {other}')

            # Download the video to the specified directory with the given filename
            video.download(output_path=self.__directory, filename=self.__filename)
            logging.info('Video downloaded successfully!')

            # Show the success message to the user
            showinfo('Success', 'Video successfully downloaded!')
        except RegexMatchError:
            # Handle invalid URL
            logging.error('Invalid URL: Cannot find the YouTube URL!')
            showwarning('Invalid URL', 'Cannot find the YouTube URL!')
        except VideoUnavailable:
            # Handle unavailable video
            logging.error('Video is unavailable: You can download videos only from YouTube!')
            showwarning('Video Unavailable', 'You can download videos only from YouTube!')

    @cache
    def download_audio(self) -> None:
        """
        Download audio from a YouTube video based on the provided URL, filename and directory.
        """

        # Load default audio format from preferences
        data_manager = DataManager()
        file_format = data_manager.load_preferences().get('default-audio-format')

        # If the filename does not have an extension, append the default audio format
        if '.' not in self.__filename:
            self.__filename = f'{self.__filename}.{file_format}'

        try:
            # Initialize YouTube object and fetch the audio stream
            youtube = YouTube(self.__url)
            audio = youtube.streams.filter(only_audio=True).first()
            logging.info('Selected audio stream.')

            # Download the audio to the specified directory with the given filename
            audio.download(output_path=self.__directory, filename=self.__filename)
            logging.info('Audio downloaded successfully!')

            # Show the success message to the user
            showinfo('Success', 'Audio successfully downloaded!')
        except RegexMatchError:
            # Handle invalid URL
            logging.error('Invalid URL. Cannot find the YouTube URL!')
            showwarning('Invalid URL', 'Cannot find the YouTube URL!')
        except VideoUnavailable:
            # Handle unavailable video
            logging.error('Video is unavailable. You can download videos only from YouTube!')
            showwarning('Video Unavailable', 'You can download videos only from YouTube!')
