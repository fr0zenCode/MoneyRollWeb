

class User:

    def __init__(self, name, balance=0):
        self.name = name
        self.id = 0
        self._balance = balance

    def __repr__(self):
        return f'User {self.id}. Name: {self.name}'

    def get_balance(self):
        return self._balance

    def less_balance(self, count):
        if self.get_balance() - count < 0:
            raise ValueError('No enough money on the balance')
        self._balance -= count

    def increase_balance(self, count):
        self._balance += count
