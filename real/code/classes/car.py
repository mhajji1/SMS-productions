import random

class Car():
    def __init__(self, orientation, col, row, length, name):
        self.orientation = orientation
        self.col = col - 1
        self.row = row - 1
        self.name = name
        self.length = length
        self.color = [0, random.random(), random.random()]


class RedCar(Car):
    def __init__(self, orientation, col, row, length, name):
        super().__init__(orientation, col, row, length, name)
        self.color = [1,0,0]
