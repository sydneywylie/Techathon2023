import matplotlib.pyplot as plt
import numpy as np
import random

powerUsage = []
timeRange = int(input("How many hours would you like to see the usage for? "))
times = []

rand_list=[]
for i in range(timeRange):
    times.append(i+1)
    powerUsage.append(random.randint(1,5))

plt.ylabel('POWER USAGE IN KWH/H')
plt.xlabel('HOURS')

plt.plot(powerUsage)
plt.show()
