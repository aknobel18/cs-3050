import pybullet as p
import time
import pybullet_data
import logging
from robot import ROBOT
from world import WORLD 
import pyrosim.pyrosim as pyrosim
class SIMULATION:


    def __init__(self, directOrGUI):
        
        #create the physics client object 
        if directOrGUI == 'DIRECT':
            physicsClient = p.connect(p.DIRECT)
            logging.basicConfig(level=logging.ERROR)
        else:
            physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())


        #import gravity
        p.setGravity(0,0,-9.8)

        #create instances of world and robot
        self.world = WORLD()
        self.robot = ROBOT()
        self.Run()
    
    def Run(self):
        #for loop to perform simulation
        for x in range(1,550):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)

            time.sleep(1/80)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()
