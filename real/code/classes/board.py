from .car import Car
import numpy as np

class Board:
    '''
    This class contains all methods and attributes which apply to a state of the board
    '''

    def __init__(self, car_list, moves=[]):
        # car_list is an intger per car, to minimize memory
        self.car_list = car_list
        self.moves = moves


    def draw_board(self, size, full_list):
        '''
        This function draws a np matrix from the board,
        where empty is zero and the cars have a number
        '''
        self.board = np.zeros((size, size), dtype=int)

        # draw all cars in car_list
        for i, car in enumerate(full_list):
            car_coords = self.car_list[i]

            if car.orientation == 'H':
                self.board[car.row, car_coords : car_coords + car.length] = car.name
            else:
                self.board[car_coords : car_coords + car.length, car.col] = car.name

        # return the state to be added into an archive
        return str(self.car_list).replace(',', '')[1:-1]


    def update_board(self, car_number, car, difference):
        '''
        This function only redraws the appropiate car
        '''

        if car.orientation == 'H':
            # replace the old coordinates with 0
            self.board[car.row, self.car_list[car_number] : self.car_list[car_number] + car.length] = 0
            self.add_move(car_number, difference)
            # draw the new coordinates
            self.board[car.row, self.car_list[car_number] : self.car_list[car_number] + car.length] = car.name

        else:
            # replace the old coordinates with 0
            self.board[self.car_list[car_number] : self.car_list[car_number] + car.length, car.col] = 0
            self.add_move(car_number, difference)
            # draw the new coordinates
            self.board[self.car_list[car_number] : self.car_list[car_number] + car.length, car.col] = car.name

        # return the state to be added into an archive
        return str(self.car_list).replace(',', '')[1:-1]


    def add_move(self, car_number, difference):
        '''
        This function moves a car by the difference amount and saves the move
        '''
        self.car_list[car_number] += difference
        self.moves.append((car_number + 1, difference))


    def check_win(self, size, red_car):
        '''
        This function returns if the path for the red car is clear
        '''
        if sum(self.board[red_car.row, self.car_list[-1] + red_car.length:]) == 0:
            return True


    def check_movement(self, size, car, car_number):
        '''
        This function checks which spaces are available
        '''

        upper_range = 0
        lower_range = 0

        # change variables for H, horizontal and else vertical cars
        if car.orientation == 'H':
            line = self.board[car.row, :]
            height = self.car_list[car_number]
        else:
            line = self.board[:, car.col]
            height = self.car_list[car_number]

        # check all spaces in front of the car
        for x, i in enumerate(range(height + car.length, size)):
            # go through all spaces till a not empty one is found
            if line[i] != 0:
                break
            upper_range = x + 1
        # check all available spaces behind the car
        for y, j in enumerate(range(height - 1, -1, -1)):
            if line[j] != 0:
                break
            lower_range = -(y + 1)
        # the ranges are the max amount of steps in each direction
        return lower_range, upper_range


    def __repr__(self):
        '''
        Make sure that the object is displayed properly
        '''
        return f'{self.board}' + '\n'
