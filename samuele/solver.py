import time

from analysis import analysis
from classes import *
from judge import judge
from read import read
from write import write

path = './input/'


def solver(task):

    start = time.time()

    output = []

    buildings, antennas, reward = read(path + task)

    # Analysis
    analysis(task, buildings, antennas, reward)

    for i in range(min(len(buildings), len(antennas))):
        antennas[i].x = buildings[i].x
        antennas[i].y = buildings[i].y
        output.append(antennas[i])

    write('output/' + str(task.split('.')[0]) + '.txt', output)

    print(task, str(time.time() - start))
