import pyrosim.pyrosim as pyrosim
import pybullet as p
import sys
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK 

class ROBOT:

    def __init__(self):
        #add robot 
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Sense(self, x):
        for sensor in self.sensors.values():
            sensor.Get_Value(x)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, x):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
    
    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
        print(f"\nFitness: {self.xCoordinateOfLinkZero}\n")
        with open("fitness.txt", "w") as file:
            file.write(str(self.xCoordinateOfLinkZero))
