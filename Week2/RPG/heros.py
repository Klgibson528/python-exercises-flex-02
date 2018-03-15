class Hero(Character):
    def __init__(self, name, hp, weapon, coins):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.coins = coins

#Heros
fighter = Hero('Fighter', 15, 'Sword', 20)
wizard = Hero('Wizard', 15, 'Magic Missle', 20)
cleric = Hero('Cleric', 10, 'Cure wounds', 10)
rouge = Hero('Rouge', 10, 'Dagger', 10)