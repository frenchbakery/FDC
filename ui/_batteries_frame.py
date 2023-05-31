"""
_batteries_frame.py
31. May 2023

<description>

Author:
Nilusink
"""
from ._battery_indicator import BatteryIndicator
from ._titled_frame_frame import TitledFrame


N_BATS = 6


class BatteriesFrame(TitledFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, title="Batteries", **kwargs)

        self.content_frame.grid_columnconfigure(list(range(N_BATS)), weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # widgets.Label(
        #     self.content_frame, width=100
        # ).grid(
        #     row=0, column=0, sticky="ns"
        # )

        for b_i in range(N_BATS):
            BatteryIndicator(
                self.content_frame,
                # width=100
            ).grid(
                row=0,
                column=b_i,
                sticky="nsew",
                margin=20
            )
