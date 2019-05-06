import laws

class Earth_Object(laws.LawsOfPhysics):
    def __init__(self, mass):
        laws.LawsOfPhysics()
        self.mass = mass
        self.gravity = 10 #m/s**2
    def gravitationalEnergy(self, height):
        self.gravitationalEnergyEq(self.mass, self.gravity, height)
    def kineticEnergy(self, vel):
        self.kineticEnergyEq(self.mass, vel)