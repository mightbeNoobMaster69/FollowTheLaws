import laws

class Earth_Object(laws.LawsOfPhysics):
    def __init__(self, mass):
        laws.LawsOfPhysics()
        self.mass = mass
        self.gravity = 10 #m/s**2
    def gravitationalEnergy(self, height):
        self.gravitationalEnergyEquation(self.mass, self.gravity, height)

