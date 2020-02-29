import board
import digitalio
import busio
import time
import adafruit_bmp280
import json
from influxdb import InfluxDBClient
from datetime import datetime

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True:
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    Temperature = [
    {
        "measurement": "Temperatures",
        "time": current_time,
        "fields": {
            "Room": "Bedroom",
            "Temp": bmp280.temperature
        }
    }]
    client = InfluxDBClient(host='InfluxServerName', port=8086, database='Temperatures')
    client.create_database('Temperatures')
    client.write_points(Temperature)
    time.sleep(1)
