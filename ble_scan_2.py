#!/usr/bin/env python3
"""
Credit to https://github.com/BostonUniversitySeniorDesign/2021-hardware-miniproj/blob/main/ble_scan.py
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
"""

from bluetooth.ble import DiscoveryService
import time
import sys

monitor_period = sys.argv[1] # duration of test (s)
scan_frequency = int(sys.argv[2]) # time between scans (s)

scan_period = sys.argv[3] # duration of each scan (s)
scan_period_int = int(scan_period)


timeaxis = []
num_devices = []

t0 = time.time()

data = open("ble_data.txt","a")

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
    t_i = timestamp.tm_hour + timestamp.tm_min/60 + timestamp.tm_sec/3600
    timeaxis.append(t_i)
    num_devices.append(count)
    sample = str(t_i) + " " + str(count)
    data.write(sample + "\n")
    time.sleep(scan_frequency)

