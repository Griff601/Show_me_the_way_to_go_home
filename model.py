import townframework
import matplotlib.pyplot

  
town = townframework.load('drunk.txt')
plotTown = []
for row in town:
    plotRow = []
    plotTown.append(plotRow)
    for location in row:
        plotRow.append(location.address)


matplotlib.pyplot.imshow(plotTown)

matplotlib.pyplot.show()