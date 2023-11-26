from pathlib import Path
from tkinter import Tk, StringVar, PhotoImage
from tkinter.filedialog import askdirectory
from tkinter.font import nametofont
from tkinter.messagebox import showwarning
from tkinter.ttk import Label, Button, Entry, Frame

from tktooltip import ToolTip

from data_manager import DataManager
from downloader import Downloader
from utilities import show_app_info, open_preferences, open_youtube


class Main:
    def __init__(self, title: str, width: int, height: int, resizable: bool = False):
        # Initialize the main Tkinter window
        self._window = Tk()
        self._window.title(title)
        self._window.geometry(f'{width}x{height}')
        self._window.eval('tk::PlaceWindow . center')
        self._window.resizable(resizable, resizable)
        self._window.tk.call('wm', 'iconphoto', self._window._w, PhotoImage(file=r'images/logo.png'))

        # Initialize StringVar instances for storing input values
        self.__url_variable = StringVar()
        self.__name_variable = StringVar()

    def __setup_ui(self):
        # Bold font settings
        bold_font = nametofont('TkDefaultFont').copy()
        bold_font.configure(size=14, weight='bold')

        # Create labels and entry widgets for URL and file name input
        Label(self._window, text='YouTube URL', font=bold_font).pack(pady=(5, 0))
        url_entry = Entry(self._window, textvariable=self.__url_variable, width=20)
        ToolTip(url_entry, msg='Paste the YouTube URL here', delay=1.0, follow=False)
        url_entry.focus_set()
        url_entry.pack()

        Label(self._window, text='File Name', font=bold_font).pack(pady=(5, 0))
        name_entry = Entry(self._window, textvariable=self.__name_variable, width=20)
        ToolTip(name_entry, msg='Write the filename here with file extension or without', delay=1.0, follow=False)
        name_entry.pack(pady=(3, 0))

        # Create a frame for download options
        download_frame = Frame(self._window)
        download_frame.pack(pady=(5, 0))

        # Create buttons for downloading video and audio
        Label(download_frame, text='Download', font=bold_font).pack()
        download_video_button = Button(download_frame, text='Video', width=7, command=self.__download_video)
        ToolTip(download_video_button, msg='Download the entire video', delay=1.0, follow=False)
        download_video_button.pack(side='left', padx=5)

        download_audio_button = Button(download_frame, text='Audio', width=7, command=self.__download_audio)
        ToolTip(download_audio_button, msg='Download audio only', delay=1.0, follow=False)
        download_audio_button.pack(side='left', padx=5)

        # Create buttons for preferences, more information and YouTube
        youtube_button = Button(self._window, text='Open YouTube', command=open_youtube)
        ToolTip(youtube_button, msg='Open youtube.com in a new tab', delay=1.0, follow=False)
        youtube_button.pack(pady=(30, 0))

        preferences_button = Button(self._window, text='Preferences', width=10, command=open_preferences)
        ToolTip(preferences_button, msg='Open app preferences', delay=1.0, follow=False)
        preferences_button.pack()

        info_button = Button(self._window, text='More Info', width=10, command=show_app_info)
        ToolTip(info_button, msg='Show more info about this app', delay=1.0, follow=False)
        info_button.pack()

    def __download_video(self):
        # Initialize Data Manager
        data_manager = DataManager()

        # Get input values
        url: str = self.__url_variable.get()
        name: str = self.__name_variable.get()
        quality: str = data_manager.load_preferences().get('video-quality')

        # Check for valid input
        if not url or not name:
            showwarning('Invalid Input', 'Please, enter a valid URL and file name.')
            return

        # Ask for a directory to save the downloaded file
        directory = Path(askdirectory())

        if not directory:
            return

        # Call the download_video function with input values
        downloader = Downloader(url, name, directory, quality)
        downloader.download_video()

    def __download_audio(self):
        # Get input values
        url: str = self.__url_variable.get()
        name: str = self.__name_variable.get()

        # Check for valid input
        if not url or not name:
            showwarning('Invalid Input', 'Please, enter a valid URL and file name.')
            return

        # Ask for a directory to save the downloaded file
        directory = Path(askdirectory())

        if not directory:
            return

        # Call the download_audio function with input values
        downloader = Downloader(url, name, directory)
        downloader.download_audio()

    def __update_window(self):
        self._window.update()
        self._window.after(100, self.__update_window)

    def run(self):
        # Start updating the window, set up the UI, and run the main loop
        self.__update_window()
        self.__setup_ui()
        self._window.mainloop()
