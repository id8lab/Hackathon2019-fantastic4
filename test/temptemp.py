import time
import datetime
import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print 'Temp: {} C  Humidity: {} %'.format(temperature, humidity)

