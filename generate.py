#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:32:16 2024

@author: abbeyknobel
"""
#import packages
import pyrosim.pyrosim as pyrosim

def Generate_Body():
    #initialize pyroism
    pyrosim.Start_SDF("world.sdf")
    #create box at origin
    pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[1,1,1])
    #close pyroism
    pyrosim.End()
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

def Generate_Brain():
    #initialize pyroism
    pyrosim.Start_SDF("world.sdf")
    #close pyroism
    pyrosim.End()
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -2.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3, weight = 1.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4, weight = 3.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3, weight = -2.0 )


    # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3, weight = -1.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3, weight = 1.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4, weight = 1.0 )

    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3, weight = -2.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3, weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4, weight = 3.0 )

    

    pyrosim.End()

Generate_Body()
Generate_Brain()

"""     This is from the tower building activity using the google slides
     pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1.0])
     pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1.0])
     pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
     pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
     pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,0.5,-0.5])
     pyrosim.Send_Cube(name="Link5", pos=[0,0,-0.5] , size=[1,1,1])
     pyrosim.Send_Joint(name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
     pyrosim.Send_Cube(name="Link6", pos=[0,0,-0.5] , size=[1,1,1])  """
