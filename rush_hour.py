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

        # three for three rgb values
        self.image = np.ones((self.size, self.size, 3))

        for car in self.car_list:

            # color the cars
            if car.orientation == 'H':
                self.image[car.row, car.col : car.col + car.length] = car.color
            else:
                self.image[car.row : car.row + car.length, car.col] = car.color

        plt.imshow(self.image)
        plt.draw()
        plt.pause(0.01)


    def random_step(self):

        upper_range = 0
        lower_range = 0

        while lower_range == 0 and upper_range == 0:


            random_index = random.randrange(len(self.car_list))
            car = self.car_list[random_index]


            if car.orientation == 'H':

                # only use the row, because that is the only information needed
                # for a random car
                col = self.image[car.row, :]

                for x, i in enumerate(range(car.col + car.length, self.size)):

                    if sum(col[i]) != 3:
                        break
                    upper_range = x + 1


                for y, j in enumerate(range(car.col - 1, -1, -1)):

                    if sum(col[j]) != 3:
                        break
                    lower_range = -(y + 1)


                if lower_range != 0 or upper_range != 0:
                    difference = 0
                    while difference == 0:

                        difference = random.randrange(lower_range, upper_range + 1)
                    car.col += difference


            else:

                row = self.image[:, car.col]

                for x, i in enumerate(range(car.row + car.length, self.size)):

                    if sum(row[i]) != 3:
                        break
                    upper_range = x + 1

                for y, j in enumerate(range(car.row - 1, -1, -1)):

                    if sum(row[j]) != 3:
                        break
                    lower_range = -(y + 1)

                if lower_range != 0 or upper_range != 0:

                    difference = 0
                    while difference == 0:

                        difference = random.randrange(lower_range, upper_range + 1)
                    car.row += difference


#if __name__ == '__main__':
my_experiment = Experiment(6, csv_file)
my_experiment.open_file()
for i in range(100):
    my_experiment.visualize()
    my_experiment.random_step()
