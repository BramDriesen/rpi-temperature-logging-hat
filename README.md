# rpi-temperature-logging-hat
Raspberry Pi Temperature Logging HAT

## Functionality

TODO

## Hardware

This script is built to work with the SHT31-D Temperature & Humidity sensor from Adafruit. Furthermore I added a small LCD SPI Display from Pimoroni. 

## Configuration

###### Make sure the I2C interface is enabled in your Raspberry Pi configuration.

Verify this by executing the following command:

    sudo i2cdetect -y 1

You should not see an error message like:

    Error: Could not open file '/dev/i2c-1' or '/dev/i2c/1': No such file or directory.

Instead you should see a message like:

    
    


## Installing dependencies

    sudo pip3 install adafruit-circuitpython-sht31d
    curl https://get.pimoroni.com/st7735 | bash

