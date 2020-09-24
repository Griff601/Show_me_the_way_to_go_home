import csv
import random

class Location:
    def __init__(self, address):
        self.address = address
        self.points = []

class Town:
    def __init__(self, locations, environment):
        self.locations = locations
        self.drunks = []
        self.environment = environment
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
            self.drunks.append(Drunk(x, y, location, environment))
    def think(self):
        for drunk in self.drunks:
            drunk.wander()
        

class Drunk:
    def __init__(self, x, y, home, environment):
        self.home = home
        self.x = x
        self.y = y
        self.environment = environment
    # setting up the wandering of drunks
    def wander(self):
        # stopping the drunks from wandering when they reach their home
        imHome = (self.x, self.y) in self.home.points
        if imHome:
            return
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = random.choice(directions)
        # these checks will stop the drunks leaving the boundary of the town
        # but drunks will get stuck on the outer edge and 1 in 3 times will
        # not be able to move away. 
        nextX = self.x + x
        nextY = self.y + y
        if nextY < 0 or nextY >= len(self.environment):
            return
        if nextX < 0 or nextX >= len(self.environment[nextY]):
            return
        self.x += x
        self.y += y
        # changing the environment to show individual cells that have been 
        # passed
        self.environment[y][x] += 1
        
        

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


        