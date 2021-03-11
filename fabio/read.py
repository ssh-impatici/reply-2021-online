from classes import *


def split_line(string):
    return [char for char in string]


def read(path):
    with open(path, 'r') as file:

        office = []
        developers = []
        managers = []

        width, height = [int(value) for value in file.readline().strip().split(" ")]

        for i in range(height):
            line = split_line(file.readline().strip())

            office.append([Cell(available=cell != '#', for_developer=cell == '_', symbol=cell) for cell in line])

        num_developers = int(file.readline())

        for i in range(num_developers):
            company, bonus, ns, skills = file.readline().strip().split(" ", maxsplit=3)
            skills = skills.split(" ")
            developers.append(Developer(company, int(bonus), skills))

        num_managers = int(file.readline())

        for i in range(num_managers):
            company, bonus = file.readline().strip().split()
            managers.append(Manager(company, int(bonus)))

    return office, developers, managers
