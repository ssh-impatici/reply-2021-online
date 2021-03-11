import time

from classes import *
from judge import judge
from read import read
from write import write

path = './input/'


def solver(task):
    start = time.time()

    _ = read(path + task + '.txt')

    output = []

    write('./output/' + task + '.txt', output)

    score = judge(output)

    print(task, str(time.time() - start))
