#
import townframework
import matplotlib.pyplot

#
iterations = 1000

town = townframework.load('drunk.txt')

# rendering the town environment
matplotlib.pyplot.imshow(town.environment)

# run the model
for i in range (iterations):
    town.think()

# plotting the end point of the drunks as they initialise and move
for drunk in town.drunks:
    matplotlib.pyplot.scatter(drunk.x, drunk.y)
matplotlib.pyplot.show()
