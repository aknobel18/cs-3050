#import packages
import pybullet as p
import time
import pybullet_data
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

pyrosim.Prepare_To_Simulate(robotId)
#for loop to perform simulation
for x in range(1,1000):
    p.stepSimulation()
    #get sensor data
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #print time that has passed
    #print(x)
    #sleep
    time.sleep(1/50)

print(backLegSensorValues)
#disconnect from the physics object
p.disconnect()
