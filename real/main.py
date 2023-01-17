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


    number_of_moves = []

    # --------------------------- Random movement --------------------------
    for i in range(1000):
        car_list_1 = open_file('data/Rushhour6x6_2.csv')
        test = RandomAlgorithm(car_list_1, 6)
        test.main_random(100000)
        number_of_moves.append(len(test.made_moves))
    print(test.made_moves)

    #perform analysis
    import matplotlib.pyplot as plt
    #make the average
    average = sum(number_of_moves)/len(number_of_moves)
    max = max(number_of_moves)
    min = min(number_of_moves)
    print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")

    # plot the values on a graph
    plt.hist(number_of_moves)
    plt.title("distribution of means")
    plt.xlabel("the number of moves until it's in the winning position")
    plt.ylabel("the number of simuilations at a given position")

    plt.show()
