#import packages
import pybullet as p
import time
import sys
#create the physics client object 
physicsClient = p.connect(p.GUI)
#import gravity
p.setGravity(0,0,-9.8)

#load box
p.loadSDF("box.sdf")
#for loop to perform simulation
for x in range(1,1001):
    p.stepSimulation()
    print(x)
    time.sleep(1/50)

#disconnect from the physics object
p.disconnect()
sys.exit()
