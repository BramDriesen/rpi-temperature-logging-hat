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
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=19,
    rotation=90,
    spi_speed_hz=4000000
)

# Initialize display.
disp.begin()
disp.set_backlight(GPIO.LOW)

WIDTH = disp.width
HEIGHT = disp.height

def draw_graph(x, y, disp):
    font = {'family' : 'DejaVu Sans',
            'weight' : 'bold',
            'size'   : 25}
    
    mpl.style.use('dark_background')
    mpl.rc('font', **font)
    plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
    plt.plot(x, y, color = 'red')
    plt.savefig('chart.png', bbox_inches='tight', pad_inches = 0.0)

    # Load the image
    image = Image.open('chart.png')

    # Resize the image
    image = image.resize((WIDTH, HEIGHT))

    # Draw the image on the display.
    disp.display(image)

# Button.
Button.was_held = False

def reset_graph(button):
    button.was_held = True
    print("Reset button triggered")
    global x
    global y
    global disp
    x.clear()
    y.clear()
    draw_graph(x, y, disp)

def toggle_screen(button):
    if not button.was_held:
        print("Toggle screen button triggered")
        global display_is_on
        global disp
        global GPIO
        if display_is_on:
            disp.set_backlight(GPIO.HIGH)
            display_is_on = False
        else:
            disp.set_backlight(GPIO.LOW)
            display_is_on = True
    button.was_held = False

button = Button(17, hold_time=5)
button.when_held = reset_graph
button.when_released = toggle_screen

while True:
    now = datetime.now()
    # Todo: remove seconds
    x.append(now.strftime("%H:%M:%S"))
    y.append(sensor.temperature)

    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)

    draw_graph(x, y, disp)

    time.sleep(10)
