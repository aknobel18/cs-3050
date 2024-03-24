import numpy as np
import sys
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        #multiply matrix to scale 
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {directOrGUI}")
        fitnessFile = open("fitness.txt", "r")
        self.fitness = fitnessFile.read()
        self.fitness = float(self.fitness)
        fitnessFile.close()

    def Create_World(self):
        #initialize pyroism
        pyrosim.Start_SDF("world.sdf")
        #create box at origin
        pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[1,1,1])
        #close pyroism
        pyrosim.End()
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        #creat the torso with absolute coordinates since it is the root
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        #create the first joint in relation to the torso
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1.0,0,1.0])
        #create the back leg
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0 ,-0.5] , size=[1,1,1])
        #create joint between the torso and the front leg
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.0,0,1.0])
        #create front leg link
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0 , -0.5] , size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range (0,3):
            for currentColumn in range(0,2):
                weight = random.uniform(-1, 1)
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName= currentColumn + 3, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,2)
        randCol = random.randint(0,1)
        self.weights[randRow,randCol] =  random.random() * 2 - 1
        