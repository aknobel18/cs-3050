#import packages
import pybullet as p
import time

#create the physics client object 
physicsClient = p.connect(p.GUI)


#for loop to perform simulation
for x in range(1,1001):
    p.stepSimulation()
    print(x)
    time.sleep(1/50)

#disconnect from the physics object
p.disconnect()
