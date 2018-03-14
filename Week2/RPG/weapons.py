class Weapons:
    def __init__(self, name, min_dmg, max_dmg):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

sword = Weapons('Sword', 1, 8)
magic = Weapons('Magic Missle', 1, 6)
dagger = Weapons('Dagger', 1, 4)
heal = Weapons('Cure wounds', 1, 8)