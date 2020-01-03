from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from multiprocessing import Process
import time
import subprocess
import board
import busio
import adafruit_sht31d
import RPi.GPIO as GPIO
import ST7735

# GPIO PINS.
BUTTON = 17
BACKLIGHT = 19

# GLOBAL VAR.
disp = None

def button():
    try:
        GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
            pin = GPIO.wait_for_edge(BUTTON, GPIO.RISING, timeout=3000)
            if pin is None:
                subprocess.call('sudo shutdown -h now', shell=True)
            else:
                GPIO.output(BACKLIGHT, not GPIO.input(BACKLIGHT))
            time.sleep(0.2)
    finally:
        GPIO.cleanup()


def screen_setup():
    global disp
    disp = ST7735.ST7735(
        port=0,
        cs=ST7735.BG_SPI_CS_FRONT,
        dc=9,
        backlight=BACKLIGHT,
        rotation=90,
        spi_speed_hz=10000000
    )

def temperature_humidity_logging():
    try:
        # Create library object using our Bus I2C port
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_sht31d.SHT31D(i2c)

        while True:
            print("\nTemperature: %0.1f C" % sensor.temperature)
            print("Humidity: %0.1f %%" % sensor.relative_humidity)
            time.sleep(2)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    # Screen setup.
    screen_setup()

    # Start listening for button actions.
    button_process = Process(target=button())
    button_process.start()

    # Start the logging process.
    logging_process = Process(target=temperature_humidity_logging())
    logging_process.start()


    # TEST
    MESSAGE = "Hello World!"

    disp.begin()

    WIDTH = disp.width
    HEIGHT = disp.height
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    size_x, size_y = draw.textsize(MESSAGE, font)
    text_x = 160
    text_y = (80 - size_y) // 2
    t_start = time.time()

    try:
        while True:
            x = (time.time() - t_start) * 100
            x %= (size_x + 160)
            draw.rectangle((0, 0, 160, 80), (0, 0, 0))
            draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
            disp.display(img)
    except:
        # Turn off the backlight.
        GPIO.output(BACKLIGHT, 0)
        GPIO.cleanup()
