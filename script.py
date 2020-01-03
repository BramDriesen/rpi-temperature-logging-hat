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

MESSAGE = "Hello World!"

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=BACKLIGHT,
    rotation=90,
    spi_speed_hz=10000000
)

# Initialize display.
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

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

try:
    while True:
        x = (time.time() - t_start) * 100
        x %= (size_x + 160)
        draw.rectangle((0, 0, 160, 80), (0, 0, 0))
        draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
        disp.display(img)

        button_state = GPIO.input(BUTTON)
        if button_state == False:
            print('Button Pressed...')

        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(2)
except:
    GPIO.cleanup()