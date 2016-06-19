from random import choice

class Player():
    def __init__(self, name="Brave Hero"):
        self.name = name
        self.level = 1
        self.exp = 0

    def get_class(self, p_class):
        p_class = p_class.lower()
        if p_class in ['warrior', 'mage', 'archer']:
            self.p_class = p_class
            return True
        else:
            return False


class Room():
    def __init__(self):
        self.floor = choice(['chest', 'tree', 'rock'])
