import matplotlib.pyplot as plt
import numpy as np

def visualise(moves, car_list, size, speed = 0.1, save_png = False):

    for i,move in enumerate(moves):

        move_car = car_list[move[0] - 1]
        if move_car.orientation == 'H':
            move_car.col += move[1]
        else:
            move_car.row += move[1]

        image = np.ones((size, size, 3))

        # color the cars
        for car in car_list:
            if car.orientation == 'H':
                image[car.row, car.col : car.col + car.length] = car.color
            else:
                image[car.row : car.row + car.length, car.col] = car.color

        # draw the image
        plt.imshow(image)
        plt.draw()
        if save_png:
            plt.savefig(f'gif{i}.png', bbox_inches='tight')
        plt.pause(speed)

    image = np.ones((size, size, 3))
    car_list[-1].col = 5

    for car in car_list:
        if car.orientation == 'H':
            image[car.row, car.col : car.col + car.length] = car.color
        else:
            image[car.row : car.row + car.length, car.col] = car.color
    plt.imshow(image)
    plt.show()
