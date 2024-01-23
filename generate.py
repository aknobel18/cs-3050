#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:32:16 2024

@author: abbeyknobel
"""
#import packages
import pyrosim.pyrosim as pyrosim

#initialize starting point
x = 0
y = -2.5
z = 0.5


pyrosim.Start_SDF("boxes.sdf")
for i in range (0,5): 
    x = 0
    y += 1
    z = 0.5
    
    for j in range (0,5):
        x += 1
        #initialize block size for every tower
        length = 1
        width = 1
        height = 1
    
        
        for k in range (0, 10):
            pyrosim.Send_Cube(name="Box" + str(k), pos=[x,y,z] , size=[length,width,height])
            z += 1
            length *= 0.9
            width *= 0.9
            height *= 0.9


pyrosim.End()

