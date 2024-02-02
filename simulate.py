#import packages
import pybullet as p
import time
import pybullet_data

#create the physics client object 
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#import gravity
p.setGravity(0,0,-9.8)
#add a floor
planeId = p.loadURDF("plane.urdf")
#load box
p.loadSDF("world.sdf")

#for loop to perform simulation
for x in range(1,2000):
    p.stepSimulation()
    print(x)
    time.sleep(1/50)

#disconnect from the physics object
p.disconnect()
