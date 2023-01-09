import pandas as pd
import random

csv_file = 'Rushhour6x6_1.csv'

class Car():

    def _init_(self, orientation, col, row, length):
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

    def step(self):
        random_value = random.random()

        if random_value <= 0.50:


class Experiment():

    def _init_(self, size, input):
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

if _name_ == '_main_':
    my_experiment = Experiment(6, csv_file)
    my_experiment.open_file()
