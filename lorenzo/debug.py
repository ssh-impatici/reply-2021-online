import time

from read import read
from write import write

path = './input/'
task = 'data_scenarios_a_example.in'

start = time.time()

output = []

buildings, antennas, reward = read(path + task)

for i in range(min(len(buildings), len(antennas))):
    antennas[i].x = buildings[i].x
    antennas[i].y = buildings[i].y
    output.append(antennas[i])

write('output/' + 'a.txt', output)

print(task, str(time.time() - start))
