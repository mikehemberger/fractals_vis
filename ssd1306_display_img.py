# Imports
import os
from PIL import Image
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

# Assign device
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Image to use
fp = "/home/pi/Documents/github/remote_from_vscode/"
fn = "mandelbrot_img_128x64.jpg"
img_path = os.path.join(fp, fn)

# Load image
w, h = 128, 64
img = Image.open(img_path).resize((w, h)).convert("1", dither=Image.NONE)

# Send to display
device.display(img)