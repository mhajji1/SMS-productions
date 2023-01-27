import matplotlib.pyplot as plt
import numpy as np
import random


def visualise(moves, car_list, size, speed = 0.1, save_png = True):
    '''
    This function plots the moves returned by the different Algorithms
    '''
    color_list = [[0, random.random()/2 + 0.5, random.random()/2 + 0.5] for color in car_list[:-1]]

    for i, move in enumerate(moves):

        # move is a tuple where the first value minus one is the index of the
        # parallel car_list; car.name 1 is car_list[0], car.name 2 is car_list[1] etc.

        # change the position of the car moved
        add_move(car_list[move[0] - 1], move[1])

        # create the image based on the updated car list
        image = generate_image(car_list, size, color_list)

        # draw the image
        plt.imshow(image)
        plt.draw()
        if save_png:
            plt.savefig(f'gif{i}.png', bbox_inches='tight')
        plt.pause(speed)


def add_move(car, move):
    '''
    This function adds the move (integer) to the appropriate attribute
    '''
    if car.orientation == 'H':
        car.col += move
    else:
        car.row += move


def generate_image(car_list, size, color_list):
    '''
    This function generates an image and all cars in car_list
    '''
    image = np.ones((size, size, 3))

    for i, car in enumerate(car_list[:-1]):
        if car.orientation == 'H':
            image[car.row, car.col : car.col + car.length] = color_list[i]
        else:
            image[car.row : car.row + car.length, car.col] = color_list[i]

    # the red car is always the last in the given input files
    red_car = car_list[-1]
    image[red_car.row, red_car.col : red_car.col + red_car.length] = [1, 0, 0]

    return image
