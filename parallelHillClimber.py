from solution import SOLUTION
import constants as c
import copy
import os
import sys
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvaialbelID = 0
        self.parents = {}
        for index in range(0, c.populationSize):
            result = SOLUTION(self.nextAvaialbelID)
            self.nextAvaialbelID += 1
            self.parents[index] = result
        
        
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.children = {}
        for parent_index, parent in self.parents.items():
            child = copy.deepcopy(parent)
            self.Set_ID(child)
            self.children[parent_index] = child

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")
        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()
        

    def Set_ID(self, child):
        child.myID = self.nextAvaialbelID
        self.nextAvaialbelID += 1

    def Mutate(self):
        for child_index, child in self.children.items():
            child.Mutate()
    
    def Print(self):
        for parent in self.parents:
            print(f"\nParent Fitness of parent {parent}: {self.parents[parent].fitness} & Child fitness: {self.children[parent].fitness}\n")
        

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness < self.parents[parent].fitness:
               self.parents[parent] = self.children[parent]
    
    def Show_Best(self):
        lowestFitness = self.parents[0].fitness
        lowestFitnessParent = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness < lowestFitness:
                lowestFitnessParent = self.parents[parent]
                lowestFitness = self.parents[parent].fitness
        lowestFitnessParent.Start_Simulation("GUI")