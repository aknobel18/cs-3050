import pyrosim.pyrosim as pyrosim
import pybullet as p


class ROBOT:

    def __init__(self):
        #create two empty dictionaries in robot
        self.sensors = {}
        self.motors = {}
        #add robot 
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
    