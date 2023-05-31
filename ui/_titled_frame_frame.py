"""
_titled_frame_frame.py
31. May 2023

<description>

Author:
Nilusink
"""
from pginter import widgets


class TitledFrame(widgets.Frame):
    def __init__(self, *args, title: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.style.backgroundColor = self.parent.style.backgroundColor

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=.1)
        self.grid_rowconfigure(1, weight=1)

        self._heading_label = widgets.Label(self, text=title)
        self._heading_label.grid(row=0, column=0, sticky="nsew", margin=10)

        self._content_frame = widgets.Frame(self)
        self._content_frame.grid(row=1, column=0, sticky="nsew")

    @property
    def content_frame(self) -> widgets.Frame:
        return self._content_frame
