#import packages
import pybullet as p
import time
import pybullet_data
import math 
import sys
import numpy as np
from matplotlib import pyplot as plt
import random
import pyrosim.pyrosim as pyrosim
import constants as c
from simulation import SIMULATION
directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Get_Fitness()

