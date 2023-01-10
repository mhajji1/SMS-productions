import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

csv_file = 'Rushhour6x6_1.csv'

class Car():

    def __init__(self, orientation, col, row, length):
        self.orientation = orientation
        self.col = col - 1
        self.row = row - 1
        self.length = length
        self.color = [0, random.random(), random.random()]


class RedCar(Car):

    def __init__(self, orientation, col, row, length):
        super().__init__(orientation, col, row, length)
        self.color = [1,0,0]


class Experiment():

    def __init__(self, size, input):
        self.size = size
        self.input = input
        self.car_list = []
        self.open_file()


    def open_file(self):
        self.data = pd.read_csv(self.input)

        for key, line in self.data.iterrows():
            if line['car'] != 'X':
                key = Car(line['orientation'], line['col'], line['row'], line['length'])
                self.car_list.append(key)
            else:
                key = RedCar(line['orientation'], line['col'], line['row'], line['length'])
                self.car_list.append(key)


    def visualize(self):
        '''
        This function visualizes the board
        '''

        # create an image of appropiate size with RGB values
        self.image = np.ones((self.size, self.size, 3))

        # color the cars
        for car in self.car_list:
            if car.orientation == 'H':
                self.image[car.row, car.col : car.col + car.length] = car.color
            else:
                self.image[car.row : car.row + car.length, car.col] = car.color

        # draw the image
        plt.imshow(self.image)
        plt.draw()
        plt.pause(0.01)


    def random_car(self):
        '''
        This function picks a random car
        '''
        random_index = random.randrange(len(self.car_list))
        car = self.car_list[random_index]

        return car


    def check_movement(self, car):
        '''
        This function checks the which spaces are available
        '''

        upper_range = 0
        lower_range = 0

        # change variables for H, horizontal and else vertical cars
        if car.orientation == 'H':
            line = self.image[car.row, :]
            height = car.col
        else:
            line = self.image[:, car.col]
            height = car.row

        # check all available spaces in the positive direction
        for x, i in enumerate(range(height + car.length, self.size)):

            # the sum of [1,1,1] is three (meaning a white space, thus available)
            if sum(line[i]) != 3:
                break
            upper_range = x + 1

        # check all available spaces in the negative direction
        for y, j in enumerate(range(height - 1, -1, -1)):

            if sum(line[j]) != 3:
                break
            lower_range = -(y + 1)

        return lower_range, upper_range



    def random_step(self, lower_range, upper_range, car):
        '''
        Take a random step within a range of free spaces
        '''

        # This while loop is to make sure the car does not stay still
        difference = 0

        while difference == 0:
            difference = random.randrange(lower_range, upper_range + 1)

        # add the difference to the car
        if car.orientation == 'H':
            car.col += difference
        else:
            car.row += difference


    def main_random(self, iterations):
        '''
        This function runs all commands in order to run the random simulation
        '''

        for i in range(iterations):

            lower_range = 0
            upper_range = 0
            my_experiment.visualize()

            while lower_range == 0 and upper_range == 0:
                car = self.random_car()
                lower_range, upper_range = self.check_movement(car)

            self.random_step(lower_range, upper_range, car)


my_experiment = Experiment(6, csv_file)
my_experiment.main_random(50)
