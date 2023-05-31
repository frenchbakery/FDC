"""
_robots_frame.py
31. May 2023

<description>

Author:
Nilusink
"""
from ._titled_frame_frame import TitledFrame


class RobotsFrame(TitledFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, title="Robots", **kwargs)

