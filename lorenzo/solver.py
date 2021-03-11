import time

from classes import *
from judge import judge
from read import read
from write import write

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

path = './input/'


def solver(task):

    start = time.time()

    output = []

    buildings, antennas, reward = read(path + task)

    antennas.sort(key=lambda x: x.speed, reverse=True)
    buildings.sort(key=lambda x: x.speed_weight, reverse=True)

    for i in range(min(len(buildings), len(antennas))):

        antennas[i].x = buildings[i].x
        antennas[i].y = buildings[i].y
        output.append(antennas[i])

    write('output/' + str(task.split('.')[0]) + '.txt', output)

    print(task, str(time.time() - start))


def kmeans(task):

    start = time.time()

    output = []

    buildings, antennas, reward = read(path + task)

    X = np.array([[int(building.x), (building.y)] for building in buildings])

    kmeans = KMeans(n_clusters=len(antennas), max_iter=1)
    kmeans.fit(X)

    centroids_x = [int(value[0]) for value in kmeans.cluster_centers_]
    centroids_y = [int(value[1]) for value in kmeans.cluster_centers_]

    antennas.sort(key=lambda antenna: antenna.speed, reverse=True)

    for i in range(len(centroids_x)):
        antennas[i].x = centroids_x[i]
        antennas[i].y = centroids_y[i]
        output.append(antennas[i])

    write('output/' + str(task.split('.')[0]) + '.txt', output)

    print(task, str(time.time() - start))


