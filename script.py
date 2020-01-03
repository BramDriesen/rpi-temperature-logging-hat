import time
import board
import busio
import adafruit_sht31d
import RPi.GPIO as GPIO

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

try:
    while True:
        button_state = GPIO.input(17)
        if button_state == False:
            print('Button Pressed...')

        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(2)
except:
    GPIO.cleanup()