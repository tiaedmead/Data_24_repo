from Animal import *

class Reptile(Animal):

    def __init__(self):
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        super().__init__()

    def seek_heat(self):
        print("it's cold bruh")