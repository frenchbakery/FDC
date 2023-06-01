"""
_battery_indicator.py
31. May 2023

Display of one singular battery

Author:
Nilusink
"""
from pginter.types import DoubleVar, Color, StringVar, FrameBind
from pginter import widgets
from random import randint
from PIL import Image
import typing as tp
import time


# load images
IMAGES = [
    Image.open("./ui/assets/battery/0.png"),
    Image.open("./ui/assets/battery/1.png"),
    Image.open("./ui/assets/battery/2.png"),
    Image.open("./ui/assets/battery/3.png"),
    Image.open("./ui/assets/battery/4.png"),
    Image.open("./ui/assets/battery/5.png"),
    Image.open("./ui/assets/battery/6.png"),
]
IMAGE_BOLT = Image.open("./ui/assets/battery/b.png")
FRAME_WHITE = Image.open("./ui/assets/battery/frame_white.png")
FRAME_RED = Image.open("./ui/assets/battery/frame_red.png")


class BatteryIndicator(widgets.Frame):
    percentage: DoubleVar = ...
    critical: float = 20

    def __init__(self, *args, **kwargs) -> None:
        # random values since there are currently no real battery
        # monitors
        self.percentage = DoubleVar(value=randint(0, 1000) / 10)
        self.charging = not not randint(0, 1)

        # initialize parent
        super().__init__(*args, **kwargs)

        # style config
        self.hover_style.backgroundColor = Color.from_hex("#777")
        self.active_style.backgroundColor = Color.from_hex("#888")

        # bind mouse click event
        self.bind(FrameBind.active, lambda *_: print("hehe"))

        # configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=2)

        # layout
        widgets.Label(self, text="ID#0").grid(row=0, column=0, sticky="nsew")

        self._bat_icon = widgets.Frame(
            self,
            image=self._load_image(0),
            bg=Color.transparent()
        )
        self._bat_icon.grid(row=2, column=0, sticky="ns")

        percent_var = StringVar(value=f"{self.percentage.get()}%")

        self.percentage.trace_add(
            StringVar.TraceModes.write,
            lambda *_: percent_var.set(f"{self.percentage.get()}%")
        )

        widgets.Label(
            self,
            font_size=30,
            textvariable=percent_var
        ).grid(row=1, column=0, sticky="nsew")

    def _load_image(self, charge_index: tp.SupportsIndex) -> Image.Image:
        """
        get the correct image with charging symbol drawn
        """
        if self.percentage.get() <= self.critical:
            img = FRAME_RED.copy()

        else:
            img = FRAME_WHITE.copy()

        img.paste(IMAGES[charge_index], (0, 0, ), IMAGES[charge_index])

        if self.charging:
            img = img.copy()
            img.paste(IMAGE_BOLT, (0, 0), IMAGE_BOLT)

        return img

    def draw(self, surface):
        now = time.time()
        charging_index = round((self.percentage.get() / 100) * 6)

        if self.charging and charging_index < 6:
            charging_index += int(1.2 * now % 2)

        self._bat_icon._image = self._load_image(charging_index)

        super().draw(surface)
