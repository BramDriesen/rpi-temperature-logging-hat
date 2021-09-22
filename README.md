# rpi-temperature-logging-hat
Raspberry Pi Temperature Logging HAT

## Updating your RPI

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip libopenjp2-7 libatlas-base-dev
sudo pip3 install --upgrade setuptools
```
From [Adafruit CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

## Installing required dependencies

```bash
# SHT31-D Library
sudo pip3 install adafruit-circuitpython-sht31d

# LCD SPI Library
curl https://get.pimoroni.com/st7735 | bash

# Matplotlib & Numpy 
sudo pip3 install matplotlib
sudo pip3 install numpy --upgrade
```

## Raspi config

```bash
sudo raspi-config
```

- Interface options
- Enable SPI

Reboot before usage.
