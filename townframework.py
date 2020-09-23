import csv

class Location:
    def __init__(self, address):
        self.address = address

class Town:
    def __init__(self, locations, environment):
        self.locations = locations
        self.drunks = []
        self.environment = environment

class Drunk:
    def __init__(self, x, y, home):
        self.home = home
        self.x = x
        self.y = y

def load(file): 
    locations = {}
    environment = []
    
    with open(file, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
                if value == '0':
                    continue
                if not value in locations:
                    locations[value] = Location(value)
                # asign points
            environment.append(rowlist)
    return Town(locations, environment)


        