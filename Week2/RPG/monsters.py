class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

class Goblin:
    def __init__(self, steal): 
        self.steal = steal
class Ogre:
    def __init__(self, eat):
        self.eat = eat
class Dragon:
    def __init__(self, burn):
        self.burn = burn