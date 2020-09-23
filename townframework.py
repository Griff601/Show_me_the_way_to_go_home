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
        for location in locations:
            if location == pub:
                continue
            # selecting start point within pub
            x, y = random.choice(possibleStarts)
            possibleStarts.remove((x, y))
            self.drunks.append(Drunk(x, y, location))
        

class Drunk:
    def __init__(self, x, y, home):
        self.home = home
        self.x = x
        self.y = y
    # setting up the wandering of drunks
    def wander(self):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = random.choice(directions)
        self.x += x
        self.y += y
        

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


        