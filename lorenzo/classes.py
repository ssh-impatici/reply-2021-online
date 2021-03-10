class Developer:

    def __init__(self, company, bonus, skills):
        self.company = company
        self.bonus = bonus
        self.skills = skills


class Manager:

    def __init__(self, company, bonus):
        self.company = company
        self.bonus = bonus


class Cell:

    def __init__(self, available, for_developer, symbol):
        self.available = available
        self.for_developer = for_developer
        self.assigned_to = None
        self.symbol = symbol

    def __str__(self):
        return self.symbol






