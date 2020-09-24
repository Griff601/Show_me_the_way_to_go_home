# imorting required modules for code
import csv
import random
import math

# creating locations class and initialising it with: self and address and 
# creating points list. 
class Location:
    def __init__(self, address):
        self.address = address
        self.points = []

# creating town class where the 'map' is initialised 
class Town:
    def __init__(self, locations, environment):
        self.locations = locations
        self.drunks = []
        self.environment = environment
        self.heatMap = []
        for row in environment:
            self.heatMap.append([0] * len(row))
        # locate pub values
        pub = locations[1]
        possibleStarts = pub.points.copy()
        # create drunk for each location that is not the pub
        for key, location in locations.items():
            if location == pub:
                continue
            # selecting start point within pub
            x, y = random.choice(possibleStarts)
            possibleStarts.remove((x, y))
            # create drunk
            self.drunks.append(Drunk(x, y, location, self, pub))
    def think(self):
        # randomising the drunks on every iteration in order to remove 
        # artifacts
        for drunk in random.sample(self.drunks, k=25):
            drunk.wander()
        

class Drunk:
    def __init__(self, x, y, home, town, pub):
        self.home = home
        self.x = x
        self.y = y
        self.environment = town.environment
        self.drunks = town.drunks
        self.pub = pub
        self.heatMap = town.heatMap
        self.imHome = False
    # setting up the wandering of drunks
    def wander(self):
        # stopping the drunks from wandering when they reach their home
        self.imHome = (self.x, self.y) in self.home.points
        if self.imHome:
            return
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        directions.append(self.nextDirectionHome(directions))
        random.shuffle(directions)
        # for every direction randomly selected, this will check if the drunk 
        # can move here
        for x, y in directions:
            
            # finding next coordinate for drunks
            nextX = self.x + x
            nextY = self.y + y
            if self.canMoveTo(nextX, nextY):
                self.x += x
                self.y += y
                # changing the environment to show individual cells that have been 
                # passed
                
                self.heatMap[self.y][self.x] += 1
                break
    def distanceBetween(self, p1, p2):
        return abs (math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)))

    # working out the translation that gets the drunk closer to home. 
    def nextDirectionHome(self, possibleDirections):
        smallestDistance = None # None indicates that no value has been seen
        result = (0, 0)
        for point in self.home.points:
            for dx, dy in possibleDirections:
                # translate drunks position to test distance
                targetPoint = (self.x + dx, self.y + dy)
                distance = self.distanceBetween(targetPoint, point)
                if smallestDistance == None or distance < smallestDistance:
                    smallestDistance = distance
                    result = (dx, dy)
        return result 
        
    def canMoveTo(self, x, y):
        # these checks will stop the drunks leaving the boundary of the town
        # but drunks will get stuck on the outer edge and 1 in 3 times will
        # not be able to move away. 
        if y < 0 or y >= len(self.environment):
            return False
        if x < 0 or x >= len(self.environment[y]):
            return False
        
        # I tried to let the drunks move through each other whilst in the pub
        # but it proved too difficult to get them to move effectively with this
        # condition set.
        # if not (self.x, self.y) in self.pub.points:
            
        #     # checking to see if next spot is already occupied by a drunk.
        #     # this is a potential artifact because the drunks are communicating.
        #     for drunk in self.drunks:
        #         if self.x == drunk.x and self.y == drunk.y:
        #             return False 
        return True

def load(file): 
    locations = {}
    environment = []
    
    with open(file, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        y = 0
             
        for row in reader:
            rowlist = []
            x = 0
            for value in row:
                rowlist.append(value)
                if value == '0':
                    continue
                if not value in locations:
                    locations[value] = Location(value)
                    
                # asign points to locations
                l = locations[value]
                p = l.points
                p.append((x, y))
                x += 1
            environment.append(rowlist)
            y += 1
            
    return Town(locations, environment)


        