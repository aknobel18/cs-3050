#import packages
import pybullet as p
import time
import pybullet_data
import math 
import numpy as np
import pyrosim.pyrosim as pyrosim

#create the physics client object 
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#import gravity
p.setGravity(0,0,-9.8)
#add a floor
planeId = p.loadURDF("plane.urdf")
#add robot 
robotId = p.loadURDF("body.urdf")
#load box
p.loadSDF("world.sdf")
#create numpy array to store sensor values
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

pyrosim.Prepare_To_Simulate(robotId)
#for loop to perform simulation
for x in range(1,1000):
    p.stepSimulation()
    #get sensor data
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #start motors
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId, 

    jointName = "Torso_BackLeg",

    controlMode = p.POSITION_CONTROL, 

    targetPosition = -1 * math.pi/5,

    maxForce = 500)
    #sleep
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId, 

    jointName = "Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL, 

    targetPosition =  math.pi/5,

    maxForce = 500)
    time.sleep(1/50)
np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/backleg_sensor_values", backLegSensorValues)
np.save("/Users/abbeyknobel/Desktop/CS3060/cs-3050/data/frontleg_sensor_values", frontLegSensorValues)
print(backLegSensorValues)
#disconnect from the physics object
p.disconnect()
