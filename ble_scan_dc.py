#!/usr/bin/env python3
"""
Credit to https://github.com/BostonUniversitySeniorDesign/2021-hardware-miniproj/blob/main/ble_scan.py
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
"""

import matplotlib.pyplot as plt
import pylab
from bluetooth.ble import DiscoveryService
import time
import sys

monitor_period = sys.argv[1] # duration of test (s)
scan_frequency = int(sys.argv[2]) # time between scans (s)

scan_period = sys.argv[3] # duration of each scan (s)
scan_period_int = int(scan_period)

timestamps = []
hrs = []
mins = []
secs = []
timeaxis = []
num_devices = []

t0 = time.time()


# get data
while time.time() < t0 + int(monitor_period):
    msg = "Scanning BLE devices for " + scan_period + " seconds."
    print(msg)
    timestamp = time.localtime()
    svc = DiscoveryService()
    ble_devs = svc.discover(scan_period_int)
    count = len(ble_devs.items()) # number of devices
    print(time.asctime(timestamp))
    print('# of devices: ' + str(count))
    timestamps.append(timestamp)
    hrs.append(timestamp.tm_hour)
    mins.append(timestamp.tm_min)
    secs.append(timestamp.tm_sec)
    timeaxis.append(timestamp.tm_hour + timestamp.tm_min/60 + timestamp.tm_sec/3600)
    num_devices.append(count)
    time.sleep(scan_frequency)

# plot data
plt.plot(timeaxis,num_devices)
plt.xlabel('time (hr)')
plt.ylabel('# of devices')
pylab.show()




