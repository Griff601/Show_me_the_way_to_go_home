import townframework
import matplotlib.pyplot

iterations = 1000

town = townframework.load('drunk.txt')


for i in range (iterations):
    for drunk in town.drunks:
        drunk.wander()

# plotting the town and drunks as they initialise and move

matplotlib.pyplot.imshow(town.environment)
for drunk in town.drunks:
    matplotlib.pyplot.scatter(drunk.x, drunk.y)
matplotlib.pyplot.show()
