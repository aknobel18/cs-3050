#import packages
import pybullet as p
import time
import pybullet_data
import math 
import numpy as np
from matplotlib import pyplot as plt
import random
import pyrosim.pyrosim as pyrosim
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
for x in range(1,1000):
    p.stepSimulation()
    time.sleep(1/240)

#create the physics client object 
#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())

#import gravity
#p.setGravity(0,0,-9.8)
#add a floor
#planeId = p.loadURDF("plane.urdf")
#add robot 
#robotId = p.loadURDF("body.urdf")
#load box
#p.loadSDF("world.sdf")
#create numpy array to store sensor values
#backLegSensorValues = np.zeros(1000)
#frontLegSensorValues = np.zeros(1000)

#pyrosim.Prepare_To_Simulate(robotId)
#create sinusoidal movement for robot
#x = np.linspace(0, 2* np.pi, 1000)
#backleg_target_angles = c.backleg_amplitude * (np.sin(c.backleg_frequency * x + c.backleg_offset))
#frontleg_target_angles = c.frontleg_amplitude * (np.sin(c.frontleg_frequency * x + c.frontleg_offset))

#np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/frontleg_target_angles", frontleg_target_angles)
#np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/backleg_target_angles", backleg_target_angles)

#for loop to perform simulation
#for x in range(1,1000):
    #p.stepSimulation()
    #get sensor data
    #backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #start motors
    #pyrosim.Set_Motor_For_Joint(

    #bodyIndex = robotId, 

    #jointName = "Torso_BackLeg",

    #controlMode = p.POSITION_CONTROL, 

    #targetPosition = backleg_target_angles[x],

    #maxForce = c.maxforce)
    #sleep
    #pyrosim.Set_Motor_For_Joint(

    #bodyIndex = robotId, 

    #jointName = "Torso_FrontLeg",

    #controlMode = p.POSITION_CONTROL, 

    #targetPosition = frontleg_target_angles[x],

    #maxForce = c.maxforce)
    #time.sleep(1/240)
#np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/backleg_sensor_values", backLegSensorValues)
#np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/frontleg_sensor_values", frontLegSensorValues)
#print(c.backLegSensorValues)
#disconnect from the physics object
#p.disconnect()
