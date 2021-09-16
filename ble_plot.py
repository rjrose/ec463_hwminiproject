
import time
import matplotlib.pyplot as plt
import pylab

file = open("test.txt","r")
text = file.read()
data = text.split()

t_axis = []
num_devices = []

is_t_entry = True
for number in data:
  if is_t_entry:
    t_axis.append(float(number))
    is_t_entry = False
  else:
    num_devices.append(float(number))
    is_t_entry = True


graph = plt.plot(t_axis,num_devices)
plt.xlabel('time (hr)')
plt.ylabel('number of devices')
plt.title('BLE Occupancy')
pylab.show()





