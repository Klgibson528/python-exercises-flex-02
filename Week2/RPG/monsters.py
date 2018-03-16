class Monster(Character):
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
        
#Monsters - how should i set this up?
goblin = Monster('Goblin', 6, 2)
zombie = Monster('Zombie', 8, 3)
ogre = Monster('Ogre', 15, 5)
dragon = Monster('Dragon', 1000000, 10)