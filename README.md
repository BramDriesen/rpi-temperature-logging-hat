# rpi-temperature-logging-hat

Raspberry Pi Temperature Logging HAT to measure and display the temperature.

Tiny project to plot the temperature of an Adafruit SHT31-D humidity/temperature sensor on a graph which on it's turn is displayed on an SPI display by Pimoroni (ST7735)

**Features:**

- Read sensor values from a Adafruit SHT31-D humidity/temperature sensor
- Plot a chart with matplotlib and save it as PNG file
- Display chart on a Pimoroni ST7735 SPI display
- Write sensor data to a CSV for further processing if needed
- Button features:
  - Short press: Toggle on/off display
  - Long press (5 sec): Reset chart and wipe CSV

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

## Autostart

Edit your `rc.local` (or use any other method as [described here][3]) file to make the script run at boot. Edit it using the command:

```bash
sudo nano /etc/rc.local
```

Using your cursor keys scroll to the bottom and add the following line right before the `exit 0` line:

```bash
sudo python3 /home/pi/rpi-temperature-logging-hat/script.py & > /home/pi/rpi-temperature-logging-hat.log
```

Now reboot your Pi and the script should automatically start.

```bash
sudo reboot
```
