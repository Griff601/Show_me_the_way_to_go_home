import csv

def load(file): 
    with open(file, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
        town = []
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            
            town.append(rowlist)
    return town
