from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from matplotlib import pyplot as plt

import time
import board
import numpy as np

import adafruit_sht31d
import ST7735

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

# Plot test
x = np.linspace(-1, 1, 50)
print(x)
y = 2*x + 1

plt.plot(x, y)
#plt.show()

plt.savefig('chart.png', bbox_inches='tight')

# Load the image
image = Image.open('chart.png')

# Resize the image
image = image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')

disp.display(image)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(10)
