#import packages
import numpy as np
from matplotlib import pyplot as plt

#load in data
backLegSensorValues = np.load("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/backleg_sensor_values.npy")
frontLegSensorValues = np.load("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/frontleg_sensor_values.npy")
backleg_target_angles = np.load("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/backleg_target_angles.npy")
frontleg_target_angles = np.load("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/frontleg_target_angles.npy")


#plot the data
'''
plt.plot(target_angles, label = "Target Angles", color = "blue")
plt.legend()
plt.title("Target Angles")
plt.xlabel("Times Step")
plt.ylabel("Angle (radians)")
plt.show()
'''
plt.title("A5: Sensor Values for Robot")
plt.plot(backleg_target_angles, label = "Back Leg", color = 'cornflowerblue', linewidth = 4)
plt.plot(frontleg_target_angles, label = "Front Leg", color= 'black')
plt.legend()
plt.show()
