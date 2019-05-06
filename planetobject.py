import laws

class Earth_Object():
    def __init__(self, mass):
        self.mass = mass
        self.gravity = 10 #m/s**2
    def gravitationalEnergy(self, height):
        self.gravitationalE = laws.LawsOfPhysics.gravitationalEnergyEq(self.mass, self.gravity, height)       
    def kineticEnergy(self, vel):
        self.kineticE = laws.LawsOfPhysics.kineticEnergyEq(self.mass, vel)