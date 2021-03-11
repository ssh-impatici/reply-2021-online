import time

from read import read

path = './input/'
task = 'a_solar.txt'

start = time.time()

office, developers, managers = read(path + task)

print(task, str(time.time() - start))
