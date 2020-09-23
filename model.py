import townframework
import matplotlib.pyplot

  
town = townframework.load('drunk.txt')


matplotlib.pyplot.imshow(town.environment)

matplotlib.pyplot.show()