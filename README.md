# rpi-temperature-logging-hat
Raspberry Pi Temperature Logging HAT

## Updating your RPI

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
```
From [Adafruit CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

## Installing required dependencies

SHT31-D Library

```bash
sudo pip3 install adafruit-circuitpython-sht31d
```

LCD SPI Library

```bash
curl https://get.pimoroni.com/st7735 | bash
```

## Raspi config

```bash
sudo raspi-config
```

- Interface options
- Enable SPI

Reboot before usage.
