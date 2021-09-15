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

monitor_period = argv[1] # duration of test (s)
scan_frequency = argv[2] # time between scans (s)
scan_period = argv[3] # duration of each scan (s)

timestamps = []
hrs = []
mins = []
secs = []
time = []
num_devices = []


svc = DiscoveryService()
t0 = time.time()

# get data
while time.time() < t0 + monitor_period:
    print(f"Scanning BLE devices for {scan_period} seconds")
    timestamp = time.localtime()
    ble_devs = svc.discover(scan_period)
    count = len(ble_devs.items()) # number of devices
    print(time.asctime(timestamp))
    print('# of devices: ' + str(count))
    timestamps.append(timestamp)
    hrs.append(timestamp.tm_hour)
    mins.append(timestamp.tm_min)
    sec.append(timestamp.tm_sec)
    time.append(hrs[i] + mins[i]/60 + sec[i]/3600)
    num_devices.append(count)
    time.sleep(scan_frequency)

# plot data
plt.plot(time,num_devices)
plt.xlabel('time (hr)')
plt.ylabel('# of devices')
pylab.show()




