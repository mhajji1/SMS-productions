import random

class Car():
    def __init__(self, orientation, col, row, length, name):
        self.orientation = orientation
        self.col = col - 1
        self.row = row - 1
        self.name = name
        self.length = length

class RedCar(Car):
    def __init__(self, orientation, col, row, length, name):
        super().__init__(orientation, col, row, length, name)
