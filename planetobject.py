import laws

class Object:
    def __init__(self, mass, gravity):
        self.mass = mass #kg
        self.gravity = gravity #m/s**2
    def gravitationalEnergy(self, height):
        self.gravitationalE = laws.LawsOfPhysics.gravitationalEnergyEq(self.mass, self.gravity, height)       
    def kineticEnergy(self, vel):
        self.kineticE = laws.LawsOfPhysics.kineticEnergyEq(self.mass, vel)