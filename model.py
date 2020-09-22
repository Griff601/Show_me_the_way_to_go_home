import townframework

class Location:
    def __init__(self, address):
        self.address = address
  
town = townframework.load('drunk.txt')
