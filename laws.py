class LawsOfPhysics:
    def __init__(self):
        pass
    def gravitationalEnergyEq(self, mass, gravity, height):
        self.gravitationalE = mass * gravity * height
    def kineticEnergyEq(self, mass, vel):
        self.kineticE = ( mass * (vel**2) ) / 2
