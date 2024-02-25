import pybullet as p
import time
import pybullet_data
from robot import ROBOT
from world import WORLD 
import pyrosim.pyrosim as pyrosim
class SIMULATION:


    def __init__(self):
        
        #create the physics client object 
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())


        #import gravity
        p.setGravity(0,0,-9.8)

        #create instances of world and robot
        self.world = WORLD()
        self.robot = ROBOT()
        


