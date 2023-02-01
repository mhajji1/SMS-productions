import random

class Car():
    def __init__(self, orientation, col, row, length, name, signature):
        self.orientation = orientation
        self.col = col - 1
        self.row = row - 1
        self.name = name
        self.length = length
        self.signature = signature
