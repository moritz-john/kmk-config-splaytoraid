from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder


class KMKKeyboard(_KMKKeyboard):
    def __init__(self, splaytoraid_keys=40, splaytoraid_rgb=False):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=self.diode_orientation,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64,
            ),
            # RotaryioEncoder(
            #     pin_a=self.encoder_a,
            #     pin_b=self.encoder_b,
            #     # optional
            #     divisor=2,
            # ),
        ]

        self.setup_rgb(splaytoraid_keys, splaytoraid_rgb)

    col_pins = (
        pins[18],
        pins[17],
        pins[16],
        pins[19],
        pins[14],
        pins[15],
        pins[13],
    )
    row_pins = (
        pins[0],
        pins[1],
        pins[4],
        pins[6],
        pins[8],
        pins[9],
        pins[10],
        pins[7],
    )
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_a = pins[12]
    encoder_b = pins[11]
    # SCL = pins[5]
    # SDA = pins[4]
    # rx = pins[6]
    # tx = pins[1]
    rgb_pixel_pin = pins[5]

    # RGB code:
    def basic_rgb(self, pixels):
        from kmk.extensions.RGB import RGB

        # --8<-- [start:rgb]
        rgb = RGB(
            pixel_pin=self.rgb_pixel_pin,
            num_pixels=pixels,
            val_limit=100,
            hue_default=30,
            sat_default=100,
            val_default=20,
        )
        # --8<-- [end:rgb]
        self.extensions.append(rgb)

    def setup_rgb(self, splaytoraid_keys, splaytoraid_rgb):
        if splaytoraid_rgb == True:
            # self.basic_rgb(int(splaytoraid_keys))

            if splaytoraid_keys == 36:
                self.basic_rgb(12)

            elif splaytoraid_keys == 40:
                self.basic_rgb(16)

    # NOQA
    # flake8: noqa
    # fmt: off
    # TODO: Get coord_mapping
    coord_mapping = [

        49,  7,  8,  2,  1,  9,     37,  4,  3, 11, 12, 54, 
        50, 21, 22, 16, 15, 10,     38, 18, 17, 25, 26, 53,
            35, 36, 30, 29, 23,     51, 32, 31, 39, 40, 
                    44, 43, 24, 48, 52, 46, 45, 
    ]
    # fmt: on
