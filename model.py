# importing modules required
import townframework
import matplotlib.pyplot
import csv

# trial and error used to find a 'best fit' result. 100 resulted in little 
# movement of drunks, 500 was good, but 1000 iterations put most drunks at home
iterations = 1000

# loading txt file into townframework.py 
town = townframework.load('drunk.txt')


# run the model
for i in range (iterations):
    town.think()

# rendering the town environment
matplotlib.pyplot.imshow(town.environment)

# plotting the end point of the drunks as they initialise and move
for drunk in town.drunks:
    matplotlib.pyplot.scatter(drunk.x, drunk.y)
# matplotlib.pyplot.show()  # un-comment to view tracks on seperate plot

# rendering heat map of points used by drunks
# apha blend used to allow tracks to be seen on one plot with drunks and houses
matplotlib.pyplot.imshow(town.heatMap, alpha = 0.5)
matplotlib.pyplot.show()

for drunk in town.drunks:
    if drunk.imHome:
        message = "got home safely"
    else:
        message = "is still at large"
    print("The drunk for house", drunk.home.address, message)
  
for key, visitList in town.visits.items():
    drunkNames = list(map(lambda x: x.home.address, visitList))
    print('point', key, 'was visited by the following drunks: ', drunkNames)
    
# writing results to CSV file
with open('results.txt', 'w', newline='') as output:
     wr = csv.writer(output, quoting=csv.QUOTE_ALL)
     for row in town.heatMap:
         wr.writerow(row)