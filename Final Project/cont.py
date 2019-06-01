import Adafruit_BBIO.GPIO as GPIO
import datetime
import sys
from time import sleep
import struct

infile_path = "/dev/input/js0"
EVENT_SIZE = struct.calcsize("llHHI")
file = open(infile_path, "rb")
event = file.read(EVENT_SIZE)
while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack("llHHI", event)
    if value/1000000 == 302:
           print(struct.unpack("llHHI", event))

    elif value/1000000 == 268:
           print(struct.unpack("llHHI", event))

    sleep(0.01)



    event = file.read(EVENT_SIZE)
