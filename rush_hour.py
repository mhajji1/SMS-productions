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
        self.color1 = random.random()
        self.color2 = random.random()

    def step(self):
        random_value = random.random()


class Experiment():

    def __init__(self, size, input):
        self.size = size
        self.input = input
        self.car_list = []

    def open_file(self):
        self.data = pd.read_csv(self.input)
        print(self.data)

        for key, line in self.data.iterrows():
            car = Car(line['orientation'], line['col'], line['row'], line['length'])
            self.car_list.append(car)
        print(self.car_list)


    def visualize(self):

        # three for three rgb values
        self.image = np.ones((self.size, self.size, 3))

        for car in self.car_list[:-1]:

            # color the cars, but keep the red value zero to make sure it is easily distingueshable from the red car
            if car.orientation == 'H':
                self.image[car.row, car.col : car.col + car.length] = [0, car.color1, car.color2]
            else:
                self.image[car.row : car.row + car.length, car.col] = [0, car.color1, car.color2]

        # the red car is always the last car in the car_list
        red_car = self.car_list[-1]
        self.image[red_car.row, red_car.col : red_car.col + red_car.length] = [1, 0, 0]


        plt.imshow(self.image)
        plt.show()


#if __name__ == '__main__':
my_experiment = Experiment(6, csv_file)
my_experiment.open_file()
my_experiment.visualize()
