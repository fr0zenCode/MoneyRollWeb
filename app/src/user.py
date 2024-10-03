

class User:

    def __init__(self, name, balance=0):
        self.name = name
        self.id = 0
        self._balance = balance
