from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from matplotlib import pyplot as plt
from gpiozero import Button
from datetime import datetime

import time
import matplotlib as mpl
import board
import numpy as np
import RPi.GPIO as GPIO
import adafruit_sht31d
import ST7735

x = []
y = []
display_is_on = True

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    rotation=90,
    spi_speed_hz=4000000
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

def reset():
    x = []
    y = []

def toggle_screen(display_is_on, disp):
    if display_is_on:
        disp.set_backlight(GPIO.HIGH)
        display_is_on = False
    else:
        disp.set_backlight(GPIO.LOW)
        display_is_on = True

# Button.
button = Button(17, hold_time=5)
button.when_held = reset(x, y)
button.when_pressed = toggle_screen(display_is_on, disp)

while True:
    now = datetime.now()
    # Todo: remove seconds
    x.append(now.strftime("%H:%M:%S"))
    y.append(sensor.temperature)

    font = {'family' : 'DejaVu Sans',
            'weight' : 'bold',
            'size'   : 24}

    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)

    mpl.style.use('dark_background')
    mpl.rc('font', **font)
    plt.plot(x, y)
    plt.savefig('chart.png', bbox_inches='tight')

    # Load the image
    image = Image.open('chart.png')

    # Resize the image
    image = image.resize((WIDTH, HEIGHT))

    # Draw the image on the display.
    disp.display(image)

    time.sleep(10)
