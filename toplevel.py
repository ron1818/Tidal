#!/user/bin/python

""" Created by ren ye 2016-06-12,
read tidal turbine water flow data,
depth data, temperature data,
generator V, I and RPM (from arduino),
save them into SD card or upload to 
thingspeak """

import time
import thingspeak
import pynmea2
import serial
from LCD_I2C import *
from SC16IS750_I2C import *

__version__ = "0.1"
__author__ = "ren ye"


# connect DST sensor via SC16IS750
try:
    DST = SC16IS750(0x4d, baud = 9600)
except:
    print "I2C not available"

# connect Arduino
try:
    VIW = serial.Serial('/dev/ttyUSB0', 9600)
except:
    print "Serial not available"

while True:
    print DST
    print VIW.readline()
    time.sleep(1)


