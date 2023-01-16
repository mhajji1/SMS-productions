from code.algorithms.randomize import RandomAlgorithm
from code.classes.car import Car, RedCar
import pandas as pd


def open_file(input):
    data = pd.read_csv(input)
    _list = []

    for key, line in data.iterrows():
        if line['car'] != 'X':
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            _list.append(key)
        else:
            key = RedCar(line['orientation'], line['col'], line['row'], line['length'], key + 1)
            _list.append(key)

    return _list


if __name__ == '__main__':




    # --------------------------- Random movement --------------------------
    for i in range(20):
        car_list_1 = open_file('data/Rushhour6x6_2.csv')
        test = RandomAlgorithm(car_list_1, 6)
        test.main_random(100000)
    print(test.made_moves)
