from tkinter import Toplevel, StringVar
from tkinter.font import nametofont
from tkinter.messagebox import showinfo
from tkinter.ttk import Label, Button, Radiobutton, Frame

from tktooltip import ToolTip

from data_manager import DataManager


class Preferences:
    def __init__(self, title: str, width: int, height: int, resizable: bool = False):
        # Initialize a Toplevel window for preferences
        self._window = Toplevel()
        self._window.title(title)
        self._window.geometry(f'{width}x{height}')
        self._window.resizable(resizable, resizable)

        # Initialize StringVar instances for storing preferences
        self.__quality_var = StringVar()
        self.__video_format_var = StringVar()
        self.__audio_format_var = StringVar()

    def __setup_ui(self):
        # Bold font settings
        bold_font = nametofont('TkDefaultFont').copy()
        bold_font.configure(size=14, weight='bold')

        # Video quality selection section
        Label(self._window, text='Video Quality', font=bold_font).pack(pady=(5, 0))

        quality_frame = Frame(self._window)
        quality_frame.pack(pady=(0, 10))

        high_quality_radio = Radiobutton(quality_frame, text='Highest', variable=self.__quality_var, value='High')
        high_quality_radio.pack(side='left', padx=6)

        low_quality_radio = Radiobutton(quality_frame, text='Lowest', variable=self.__quality_var, value='Low')
        low_quality_radio.pack(side='left', padx=6)

        # Default video format selection section
        Label(self._window, text='Default Video Format', font=bold_font).pack(pady=(10, 0))

        video_format_frame = Frame(self._window)
        video_format_frame.pack(pady=(0, 10))

        mp4_radio = Radiobutton(video_format_frame, text='.mp4', variable=self.__video_format_var, value='mp4')
        mp4_radio.pack(side='left', padx=4)

        mov_radio = Radiobutton(video_format_frame, text='.mov', variable=self.__video_format_var, value='mov')
        mov_radio.pack(side='left', padx=4)

        webm_radio = Radiobutton(video_format_frame, text='.webm', variable=self.__video_format_var, value='webm')
        webm_radio.pack(side='left', padx=4)

        # Default audio format selection section
        Label(self._window, text='Default Audio Format', font=bold_font).pack(pady=(10, 0))

        audio_format_frame = Frame(self._window)
        audio_format_frame.pack(pady=(0, 10))

        mp3_radio = Radiobutton(audio_format_frame, text='.mp3', variable=self.__audio_format_var, value='mp3')
        mp3_radio.pack(side='left', padx=4)

        wav_radio = Radiobutton(audio_format_frame, text='.wav', variable=self.__audio_format_var, value='wav')
        wav_radio.pack(side='left', padx=4)

        ogg_radio = Radiobutton(audio_format_frame, text='.ogg', variable=self.__audio_format_var, value='ogg')
        ogg_radio.pack(side='left', padx=4)

        # Save button
        save_button = Button(self._window, text='Save', command=self.__save_preferences)
        ToolTip(save_button, msg='Save the preferences above', delay=1.0, follow=False)
        save_button.pack(pady=(10, 0))

    def __load_preferences(self):
        data_manager = DataManager()
        data = data_manager.load_preferences()

        self.__quality_var.set(data.get('video-quality').capitalize())
        self.__video_format_var.set(data.get('default-video-format').lower())
        self.__audio_format_var.set(data.get('default-audio-format').lower())

    def __save_preferences(self):
        data_manager = DataManager()

        # Write preferences to the data file
        data_manager.write_preferences('video-quality', self.__quality_var.get().lower())
        data_manager.write_preferences('default-video-format', self.__video_format_var.get().lower())
        data_manager.write_preferences('default-audio-format', self.__audio_format_var.get().lower())

        # Show success message and close the preferences window
        showinfo('Success', 'Preferences are successfully saved!')
        self._window.destroy()

    def __update_window(self):
        self._window.update()
        self._window.after(100, self.__update_window)

    def run(self):
        # Start updating the window, load preferences, set up the UI, and run the main loop
        self.__update_window()
        self.__load_preferences()
        self.__setup_ui()
        self._window.mainloop()
