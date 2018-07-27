'''
Prim's algorithm for maze generation.
Code from https://en.wikipedia.org/wiki/Maze_generation_algorithm with
the matplotlib code switched for writing to a text file to be processed by Maya.
'''
import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot

def maze(width=81, height=51, complexity=.75, density=.75):
	'''
	Create a maze in a numpy array composed of units:
		True = wall unit
		False = empty unit
	Write to file.
	'''
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)

    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1]))) # number of components
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2))) # size of components
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2 # pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_

    numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)  # turn off summarization, line-wrapping
    with open('maze_results.txt', 'w') as f:
        f.write(numpy.array2string(Z, separator=','))

maze()
