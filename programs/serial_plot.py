import matplotlib.pyplot as plt
import numpy as np
import time
import serial 
import random
reading =[]
fig, ax = plt.subplots()
ser = serial.Serial('/dev/ttyUSB0',9600) 
counter = 0
axis_x = 50
while True:
    while (ser.inWaiting()==0):    
     pass
    data  =float( ser.readline())    
    print data
    ax.clear()
    ax.set_xlim([0,axis_x])  
    ax.set_ylim([0,1023]) 
    reading.append(data)  
   
    ax.plot(reading)
    plt.pause(.000001)     
    counter = counter + 1
    if (counter > axis_x):
	   reading.pop(0)

ser.close()
