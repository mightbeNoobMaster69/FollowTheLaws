import planetobject as po

ball = po.Earth_Object(mass=5)

ball.gravitationalEnergy(height=100)
ball.kineticEnergy(vel=15)

print(str(ball.gravitationalE) + 'J')
print(str(ball.kineticE) + 'J')