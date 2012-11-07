from __future__ import division
import serial, csv, sys
import json, MySQLdb, pickle
import datetime

from django.core.management import setup_environ
from kegerator import settings

setup_environ(settings)
from django.db.models.loading import get_apps
from django.contrib.sessions.backends.db import SessionStore

get_apps()
import django.db.models
from django.contrib.sessions.models import Session
from temperature_control.models import *

for i in range(20):
    try:
        serial_port = '/dev/ttyUSB%d' % i
        break
    except ImportError:
        continue
    
ser = serial.Serial(serial_port, 9600)

reader = csv.reader(open('temperature_control/10kThermistorTable.csv'))
look_up_table = {}

for i in reader:
    look_up_table[int(i[0])] = [float(i[1]),
                                float(i[2]),
                                float(i[3]),
                                float(i[4]),]
# Store temperature as the resistance value.
# Add functions to model to get temperature in a specific unit.
try:
    while True:
        temperature = ser.readline()
        try:
            temperature = look_up_table[int(temperature)][2]
            query = TemperatureReading()
            query.temperature = temperature
            query.save()
        except ValueError:
            continue
except KeyboardInterrupt:    
    print 'Have a nice day!'
    sys.exit(0)

