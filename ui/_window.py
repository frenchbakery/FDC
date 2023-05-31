"""
_window.py
31. May 2023

<description>

Author:
Nilusink
"""
from ._batteries_frame import BatteriesFrame
from ._robots_frame import RobotsFrame
from pginter import PgRoot, widgets
from PIL import Image


class Window(PgRoot):
    def __init__(self) -> None:
        super().__init__("French Data Center")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._bg_frame = widgets.Frame(self, border_radius=0)
        self._bg_frame.grid(0, 0, sticky="nsew")

        self._bg_frame.grid_rowconfigure(0, weight=2)
        self._bg_frame.grid_columnconfigure(0, weight=2)

        self._bg_frame.grid_rowconfigure(1, weight=1)
        self._bg_frame.grid_columnconfigure(1, weight=1)

        # image frame
        self._img = widgets.Frame(
            self._bg_frame,
            image=Image.open("./ui/assets/bled_pastries.webp").resize(
                (720 * 2, 720)
            ),
        )
        self._img.grid(row=0, column=0, sticky="nsew", margin=30)

        # bot reserved
        self._bots_frame = RobotsFrame(self._bg_frame)
        self._bots_frame.grid(
            row=0,
            column=1,
            rowspan=2,
            sticky="nsew",
            margin=20
        )

        # battery manager reserved
        self._batteries_frame = BatteriesFrame(self._bg_frame)
        self._batteries_frame.grid(row=1, column=0, sticky="nsew", margin=20)
