import time
import board
import busio
import adafruit_sht31d
import RPi.GPIO as GPIO
import ST7735

# GPIO Pins.
BUTTON = 17
BACKLIGHT = 19


GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

MESSAGE = "Hello World! How are you today?"

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=BACKLIGHT,
    rotation=90,
    spi_speed_hz=10000000
)

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

try:
    while True:
        button_state = GPIO.input(BUTTON)
        if button_state == False:
            print('Button Pressed...')

        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(2)
except:
    GPIO.output(BACKLIGHT, 0)
    GPIO.cleanup()