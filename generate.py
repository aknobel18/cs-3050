#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:32:16 2024

@author: abbeyknobel
"""
#import packages
import pyrosim.pyrosim as pyrosim


#initialize pyroism
pyrosim.Start_SDF("boxes.sdf")
#create box at origin
pyrosim.Send_Cube(name="Box", pos=[0,0,0] , size=[1,1,1])

pyrosim.End()
