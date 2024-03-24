from solution import SOLUTION
import constants as c
import copy
import sys
class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
    
    def Print(self):
        print(f"\nParent Fitness: {self.parent.fitness} & Child Fitness: {self.child.fitness}\n")
        

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
    
    def Show_Best(self):
        self.parent.Evaluate("GUI")