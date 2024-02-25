import pybullet as p

class WORLD:

    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")        
        #load box
        p.loadSDF("world.sdf")