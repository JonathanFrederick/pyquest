class Player():
    def __init__(self, name="Brave Hero"):
        self.name = name

    def get_class(self, p_class):
        p_class = p_class.lower()
        if p_class in ['warrior', 'mage', 'archer']:
            self.p_class = p_class
            return True
        else:
            return False
