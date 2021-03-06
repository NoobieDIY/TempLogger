<h1>TempLogger</h1>

This is a simple script that reads the temperature from the BMP280 sensor on a raspberry pi.

Enable I2C interface
> sudo raspi-config
5 - Interfacing Options -> P5 I2C -> Enable

Just follow the following instructions to set this up:
> sudo apt-get update

> sudo apt-get upgrade

> sudo apt-get install i2c-tools

> sudo pip3 install --upgrade setuptools

If above doesn't work try
> sudo apt-get install python3-pip

> ls /dev/i2c* /dev/spi*
> This should return : 
"/dev/i2c-1  /dev/spidev0.0  /dev/spidev0.1"

> sudo pip3 install RPI.GPIO

> sudo pip3 install adafruit-blinka

> sudo pip3 install adafruit-circuitpython-bmp280

> sudo apt-get install python-influxdb

> python3 -m pip install influxdb

Check the address the BMP280 sensor is using with the following command

> i2cdetect -y 1

In my case the sensor was on i2c address 76 but the adafruit driver was configured for 77

> cd /usr/local/lib/python3.7/dist-packages/

> vim adafruit_bmp280.py

Search for the following line toward the end of the file and change the "0x77" to "0x76"
  def __init__(self, i2c, address=0x77):

Install git cli commands
> apt-get install git

pull scripts
>git pull https://github.com/NoobieDIY/TempLogger

Add this to crontab
> @reboot sudo /root/TempLogger/RunTempLogger.sh

> crontab -e

Make the sh file executable
> chmod +x RunTempLogger.sh
