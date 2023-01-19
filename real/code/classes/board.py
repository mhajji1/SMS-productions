from .car import Car, RedCar
import numpy as np

class Board:
    def __init__(self, size, car_list):
        self.size = size
        self.car_list = car_list


    def draw_board(self, return_board = False):

        self.board = np.zeros((self.size, self.size), dtype=int)

        for car in self.car_list:
            if car.orientation == 'H':
                self.board[car.row, car.col : car.col + car.length] = car.name
            else:
                self.board[car.row : car.row + car.length, car.col] = car.name
                
        if return_board:
            return self.board



    def check_win(self):

        red_car = self.car_list[-1]
        line = self.board[red_car.row, :]

        for x, i in enumerate(range(red_car.col + red_car.length, self.size)):

            if line[i] != 0:
                return False
        # if all places in front are zero, the game is won
        return True


    def check_movement(self, car, return_cars=False):
        '''
        This function checks which spaces are available
        '''

        upper_range = 0
        lower_range = 0
        blocking_cars = []

        # change variables for H, horizontal and else vertical cars
        if car.orientation == 'H':
            line = self.board[car.row, :]
            height = car.col
        else:
            line = self.board[:, car.col]
            height = car.row

        # check all available spaces in the positive direction
        for x, i in enumerate(range(height + car.length, self.size)):

            # the sum of [1,1,1] is three (meaning a white space, thus available)
            if line[i] != 0:

                if return_cars == True:
                    blocking_cars.append(self.car_list[line[i]-1])
                break
            upper_range = x + 1

        # check all available spaces in the negative direction
        for y, j in enumerate(range(height - 1, -1, -1)):


            if line[j] != 0:

                if return_cars == True:
                    blocking_cars.append(self.car_list[line[j]-1])
                break
            lower_range = -(y + 1)


        if return_cars == True:
            return blocking_cars, lower_range, upper_range
        else:
            return lower_range, upper_range
