import numpy as np
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)

    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    
    def Save_Values(self):
        np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/sensor_values", self.values)