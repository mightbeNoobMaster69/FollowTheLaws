class LawsOfPhysics:
    def __init__(self):
        pass
    @classmethod
    def gravitationalEnergyEq(self, mass, gravity, height):
        return (mass * gravity * height)
    @classmethod
    def kineticEnergyEq(self, mass, vel):
        return ( mass * (vel**2) ) / 2
