import planetobject as po

earthBall = po.Object(mass=5, gravity=10) #Earth Gravity: 10m/s**2
marsBall = po.Object(mass=5, gravity=3.71) #Mars Gravity: 3.71m/s**2

earthBall.gravitationalEnergy(height=100)
earthBall.kineticEnergy(vel=15)

marsBall.gravitationalEnergy(height=100)
marsBall.kineticEnergy(vel=15)

print(str(earthBall.gravitationalE) + 'J')
print(str(earthBall.kineticE) + 'J')

print(str(marsBall.gravitationalE) + 'J')
print(str(marsBall.kineticE) + 'J')