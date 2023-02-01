import random

class Car():
    '''
    This class is only used in the full_list stored in the algorithms
    '''
    def __init__(self, orientation, col, row, length, name, signature):
        self.orientation = orientation
        self.col = col - 1
        self.row = row - 1
        self.name = name
        self.length = length
        self.signature = signature
