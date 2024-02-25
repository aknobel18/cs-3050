import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p



class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(1000)
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        if self.jointName == "Torso_BackLeg":
            self.offset = c.offset
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            x = np.linspace(0, 2* np.pi, 1000)
            self.motorValues = self.amplitude * (np.sin(self.frequency * x + self.offset))
        else:
            self.offset = c.offset 
            self.amplitude = c.amplitude
            self.frequency = c.frequency * 1/2
            x = np.linspace(0, 2* np.pi, 1000)
            self.motorValues = self.amplitude * (np.sin(self.frequency * x + self.offset))
    
    def Set_Value(self, robotId, x):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robotId, 

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL, 

            targetPosition = self.motorValues[x],

             maxForce = c.maxforce)

    def Save_Values(self):
        np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/motor_values", self.motorValues)