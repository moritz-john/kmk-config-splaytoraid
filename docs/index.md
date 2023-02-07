---
title: "Documentation"
description: Documentation for the KMK splaytoraid Firmware
hide:
# Hide navigation bar on left side
  - navigation
---

# Documentation

<figure markdown>
  ![Splaytoraid_KMK_Logo](./images/splaytoraid_kmk.svg){ width="440" }
  <figcaption></figcaption>
</figure>

## Installation

??? tip "TL;DR:"
    [Install CircuitPython](#install-circuitpython)  
    [Install KMK](#install-kmk)  
    [Copy `kb.py`, `main.py` & `lib` to your splaytoraid](#install-splaytoraid-firmware-files)

### Install CircuitPython

KMK is a keyboard focused layer that sits on top of CircuitPython.  
[**Follow these steps**](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) and then come back here.

### Install KMK

1. Get [a copy](TO_DO) of KMK from the master branch 
2. Unzip and copy the `kmk` folder and the `boot.py` file to the root of the USB drive
3. Delete `code.py` from the USB drive

![Image title](images/installation_kmk.png){ width="500"}

### Install the splaytoraid firmware

1. Download the `kb.py`, `main.py` and `lib` from the repository and copy them onto your USB drive  
You can find those files in `splaytoraid_kmk_firmware.zip` via [GitHub releases](TO_DO)
2. Reboot

![Image title](images/installation_main_kb_lib.png){ width="800"}
***
## Microcontroller Support
[`kb.py`](TO_DO) is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `kb.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```python
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```
***
## RGB Setup

!!! tip "TL;DR:"
    Add library to your keyboard drive, set `:::py klor_rgb = True` and `:::py splaytoraid_keys = 40` or `:::py 36` keys, customize your RGB code and add RGB keycodes to your keymap
### Add RGB library
In order to use RGB make sure you copied the `'lib'` onto your splaytoraid in the [installation step](#install-splaytoraid-firmware).  
The `'lib'` folder should contain the file `'neopixel.mpy'`.

![Image title](TO_DO){ width="700"}

### Activate RGB
You have to change the variable `splaytoraid_rgb` from `False` to `True` in your [`main.py`](TO_DO) file and also set `splaytoraid_keys` to your amount of keys:

```py title="main.py"
--8<-- 'firmware/main.py:config'
```
### Customize RGB 

*You can find the code in your [`kb.py`](TO_DO) file:*

```py title="kb.py"
--8<-- 'firmware/kb.py:rgb'
```

Consider changing `hue_default`, `sat_default` or `val_default`. Use a value in the range `0-255`.  
Read more about the possible configuration options [HERE](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md#configuration).


### Control RGB via keycodes
You **need** to add some [keycodes](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md#keycodes) to your keymap in order to control your RGB lighting e.g.:

| Keycode    | Description              |
| :--------- | :------------------      |
| ++rgbtog++ | Toggles RGB on or off    |
| ++rgbhui++ | Increase Hue             |
| ++rgbhud++ | Decrease Hue             |
| ++rgbsai++ | Increase Saturation      |
| ++rgbsad++ | Decrease Saturation      |
| ++rgbvai++ | Increase Value           |
| ++rgbvad++ | Decrease Value           |

***
## Hide Device Storage

Here is how to hide your microcontroller from showing up as a USB storage by default.  
I would recommend following these steps **after** you finished setting up your splaytoraid & keymap:

- Copy this specifig [`boot.py`](TO_DO) onto your `KLORL` / `KLORR` USB storage and replace the existing file.
- You can still access the device USB storage by holding a certain key on startup

!!! warning
    **After replacing the `boot.py` file you need to hold the green key on either left or right side when connecting the keyboard to your computer or rebooting it via reset button in order to see the USB storage.**

![Image title](TO_DO)

### Microcontroller support
`boot.py` is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `boot.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```py
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```

