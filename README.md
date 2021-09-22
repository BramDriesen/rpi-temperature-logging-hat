# rpi-temperature-logging-hat

Raspberry Pi Temperature Logging HAT.

Tiny project to plot the temperature of an Adafruit SHT31-D humidity/temperature sensor on a graph which on it's turn is displayed on an SPI display by Pimoroni (ST7735)

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

# Matplotlib and Numpy 
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

## Rsync file to local

```bash
rsync -avz pi@192.168.178.57:rpi-temperature-logging-hat/chart.png ~/Downloads/chart.png
```
