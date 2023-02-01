from code.algorithms.randomize import RandomAlgorithm
# from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.algorithms.Astar import Astar
from code.algorithms.Breadth_and_Astar import BA_star
#from code.algorithms.Astar_update import Astar
from code.classes.car import Car
from code.visualisation.visualize import visualise
from tqdm import tqdm
import pandas as pd
import time
import matplotlib.pyplot as plt

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

def open_file2(input):
    data = pd.read_csv(input)
    car_list = []
    other_list = []

    for key, line in data.iterrows():
        if line['orientation'] == 'H':
            car_list.append(line['col'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, line['car'])
            other_list.append(key)
        else:
            car_list.append(line['row'] - 1)
            key = Car(line['orientation'], line['col'], line['row'], line['length'], key + 1, line['car'])
            other_list.append(key)

    return car_list, other_list

def convert_output(full_list, moves):
    '''This function changes the algorithm integers back to the official car names, 1 -> A etc.'''
    car_name = []
    step = []
    for i, move in enumerate(moves):
        car_name.append(full_list[move[0]-1].signature)
        step.append(move[1])
    output = pd.DataFrame(list(zip(car_name, step)), columns =['Car', 'Move'])
    output.to_csv('output/output.csv', index=False)
    print("Saved output in output")

    
if __name__ == '__main__':

    number_of_moves = []
    low = 100000
    input = 'data/Rushhour6x6_2.csv'
    size = 6


    for i in range(1000):
        print(i)
        car_list, full_list = open_file2(input)
        i = RandomAlgorithm(full_list, car_list, size)
        i.run()
        moves = i.board.moves
        number_of_moves.append(len(moves))
    print(number_of_moves)


    plt.hist(number_of_moves, bins=75)
    plt.title("Distribution of random")
    plt.xlabel("")
    plt.ylabel("number of states")
    plt.legend()
    plt.show()

# ---------------------------------- Random ------------------------------------
# random_model = RandomAlgorithm(full_list, car_list, size)
# start = time.time()
# moves = random_model.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Greedy ------------------------------------
# greedy = Greedy(full_list, car_list, size)
# start = time.time()
# moves = greedy.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
#
# ---------------------------------- Breadth -----------------------------------
# breadth = Breadth(full_list, car_list, size)
# start = time.time()
# moves = breadth.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# visualise(moves, open_file2(input)[1], size)

# ------------------------------- Branch & Bound -------------------------------
# branch_and_bound = BB(full_list, car_list, size)
# start = time.time()
# moves = branch_and_bound.run()
# end = time.time()
# print(f"The processing time for this board was: {end - start}")
# visualise(moves, open_file2(input)[1], size)

# ---------------------------------- Astar -------------------------------------
astar = Breadth(full_list, car_list, size)
start = time.time()
moves = astar.run()
end = time.time()
print(f"The processing time for this board was: {end - start}")
print(convert_output(full_list, moves))

    # test = Astar(full_list, car_list, size)
    # moves = test.run()
    #
    # visualise(moves, open_file2(input)[1], size)
    #final_board = mode(endstates)
    #print(final_board)
    #print(test.made_moves)

    # test = BB(full_list, car_list, size)
    #
    # start = time.time()
    # moves = test.run()
    # end = time.time()
    # print(f"The processing time for this board was: {end - start}")
    # visualise(moves, open_file2(input)[1], size)

    #
    # import matplotlib.pyplot as plt
    # #make the average
    # average = sum(number_of_moves)/len(number_of_moves)
    # max = max(number_of_moves)
    # min = min(number_of_moves)
    # print(f"the average number of moves is {average}, the maximum total moves is {max} and the least number of moves is {min}")

    #[(11, 1), (10, 1), (8, 3), (10, -1), (13, -1), (7, 1), (3, -1), (14, -2), (15, -2), (11, 1), (12, -1), (21, 1), (22, -2), (19, 1), (11, 3), (19, -1), (22, 2)]
