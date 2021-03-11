import time

from read import read
from write import write

import numpy as np

path = './input/'
task = 'data_scenarios_f_tokyo.in'

print(task)
start = time.time()

output = []

buildings, antennas, reward, width, height = read(path + task)

antennas.sort(key=lambda x: x.antenna_range, reverse=False)
buildings.sort(key=lambda x: x.speed_weight, reverse=True)

window = 20

grid = np.zeros((height, width))


def position(antenna, grid, width, height):
    r = antenna.antenna_range

    for i in range(antenna.antenna_range + 1):
        x_min = max(antenna.x - r + i, 0)
        x_max = min(antenna.x + r + 1 - i, width - 1)

        y_min = min(antenna.y + i, height - 1)
        y_max = max(antenna.y - i, 0)

        grid[y_min, x_min:x_max] = 1
        grid[y_max, x_min:x_max] = 1

        # print(antenna.y + i, height)

    return grid


# Maggiore di window
while len(antennas) > window and len(buildings) > window:

    candidates = antennas[:window]

    print(len(antennas))

    for i in range(len(candidates)):

        building = buildings[i]
        candidates[i].x = building.x
        candidates[i].y = building.y
        output.append(candidates[i])

        grid = position(candidates[i], grid, width, height)
        # print(grid)
        # print(candidates[i].antenna_range)

    for antenna in candidates:
        antennas.remove(antenna)

    for building in buildings[:window]:
        buildings.remove(building)

    buildings = [building for building in buildings if grid[building.y, building.x] == 0]

# Minore di windows
if len(buildings) != 0 and len(antennas) != 0:
    while len(buildings) > 0 and len(antennas) > 0:
        building = buildings[0]
        antenna = antennas[0]

        antenna.x = building.x
        antenna.y = building.y
        output.append(antenna)

        buildings.remove(building)
        antennas.remove(antenna)

# Antenne rimaste
if len(antennas) != 0:
    print('Sono rimaste antenne, ragioniamoci! ' + task)

# Edifici coperti rimasti
if len(buildings) == 0:
    print('Tutti gli edifici coperti! ' + task)
else:
    print('Non tutti gli edifici coperti! ' + task)

write('output/' + str(task.split('.')[0]) + '.txt', output)

print(task, str(time.time() - start))

