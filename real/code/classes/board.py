from .car import Car
import numpy as np

class Board:

    def __init__(self, car_list, moves=[]):
        self.car_list = car_list
        self.moves = moves


    def create_value(self, number):
        '''
        When necessary add an extra score attribute
        '''
        self.value = number


    def draw_board(self, size, full_list):
        '''
        This function draws a np matrix from the board,
        where empty is zero and the cars have a number
        '''
        np_board = np.zeros((size, size), dtype=int)

        # draw all cars in car_list
        for i, car in enumerate(full_list):
            car_coords = self.car_list[i]

            if car.orientation == 'H':
                np_board[car.row, car_coords : car_coords + car.length] = car.name
            else:
                np_board[car_coords : car_coords + car.length, car.col] = car.name

        # the state returned is only the necessary digits
        return str(self.car_list).replace(',', '')[1:-1], np_board


    def update_board(self, car_number, car, difference, np_board):
        '''
        This function only redraws the appropiate car
        '''
        if car.orientation == 'H':
            # replace the old coordinates with 0
            np_board[car.row, self.car_list[car_number] : self.car_list[car_number] + car.length] = 0
            self.add_move(car_number, difference)
            # draw the new coordinates
            np_board[car.row, self.car_list[car_number] : self.car_list[car_number] + car.length] = car.name

        else:
            # replace the old coordinates with 0
            np_board[self.car_list[car_number] : self.car_list[car_number] + car.length, car.col] = 0
            self.add_move(car_number, difference)
            # draw the new coordinates
            np_board[self.car_list[car_number] : self.car_list[car_number] + car.length, car.col] = car.name

        return str(self.car_list).replace(',', '')[1:-1], np_board


    def add_move(self, car_number, difference):
        '''
        This function moves a car by the difference amount and saves the move
        '''
        self.car_list[car_number] += difference
        self.moves.append((car_number + 1, difference))


    def check_win(self, size, red_car, np_board):
        '''
        This function returns if the path for the red car is clear
        '''
        if sum(np_board[red_car.row, self.car_list[-1] + red_car.length:]) == 0:
            return True


    def check_movement(self, size, car, car_number, np_board):
        '''
        This function checks which spaces are available
        '''

        upper_range = 0
        lower_range = 0

        # change variables for H, horizontal and else vertical cars
        if car.orientation == 'H':
            line = np_board[car.row, :]
            height = self.car_list[car_number]
        else:
            line = np_board[:, car.col]
            height = self.car_list[car_number]


        # check all spaces in front of the car
        for x, i in enumerate(range(height + car.length, size)):

            # if the space is 0 the place is empty
            if line[i] != 0:
                # stop when not empty
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
        Make sure that the object is printed properly
        '''
        return f'{self.board}' + '\n'
