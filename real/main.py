from code.algorithms.randomize import RandomAlgorithm
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth
from code.algorithms.Astar import Astar
from code.algorithms.iterative_deepening import ID
from code.classes.car import Car
from code.visualisation.visualize import visualise
import pandas as pd
import time
import matplotlib.pyplot as plt
import argparse


def open_file2(input):
    '''
    This function loads the csv into two list
    '''
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


def convert_output(full_list, moves, output_path):
    '''This function changes the algorithm integers back to the official car names, 1 -> A etc.'''
    car_name = []
    step = []

    for i, move in enumerate(moves):
        car_name.append(full_list[move[0]-1].signature)
        step.append(move[1])

    output = pd.DataFrame(list(zip(car_name, step)), columns =['Car', 'Move'])
    output.to_csv(f'{output_path}', index=False)
    print(f"Saved output in {output_path}")


class main():

    def __init__(self, algorithm_name, board_number):
        self.algorithm_name = algorithm_name
        self.board_number = board_number


    def run_algorithms(self):
        algorithm_list = ["RandomAlgorithm", "Greedy", "Breadth", "ID", "Astar"]
        starting_boards = {"Rushhour6x6_1.csv": 6, "Rushhour6x6_2.csv": 6
        , "Rushhour6x6_3.csv": 6, "Rushhour9x9_4.csv": 9, "Rushhour9x9_5.csv":9,
         "Rushhour9x9_6.csv":9, "Rushhour12x12_7.csv":12}


        for i, algorithm in enumerate(algorithm_list):
            if self.algorithm_name == algorithm:
                print(algorithm)
                index = i

        for i, board_file in enumerate(starting_boards.keys()):
            if self.board_number - 1 == i:
                file = board_file
                size = starting_boards[board_file]


        car_list, full_list = open_file2(f"data/{file}")

# ---------------------------------- Random ------------------------------------
        if index == 0:
            random_model = RandomAlgorithm(full_list, car_list, size)
            start = time.time()
            moves = random_model.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")


# ---------------------------------- Greedy ------------------------------------
        if index == 1:
            greedy = Greedy(full_list, car_list, size)
            start = time.time()
            moves = greedy.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")

# ---------------------------------- Breadth -----------------------------------
        if index == 2:
            breadth = Breadth(full_list, car_list, size)
            start = time.time()
            moves = breadth.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")


# ------------------------------- Iterative Deepening -------------------------------
        if index == 3:
            deepening = ID(full_list, car_list, size)
            start = time.time()
            moves = deepening.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")


# ---------------------------------- Astar -------------------------------------
        if index == 4:
            astar = Astar(full_list, car_list, size)
            start = time.time()
            moves = astar.run()
            end = time.time()
            print(f"The processing time for this board was: {end - start}")


        convert_output(open_file2(f"data/{file}")[1], moves, file)
        visualise(moves, open_file2(f"data/{file}")[1], size)


if __name__ == '__main__':

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "solve the rush hour puzzle")

    # Adding arguments
    parser.add_argument("algorithm_name", help = "algorithm name")
    parser.add_argument("-b", "--board_number",   type=int, default =1 , help="chooses board_file from 1 to 7 (default: 1)")


    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    test = main(args.algorithm_name, args.board_number)
    test.run_algorithms()
