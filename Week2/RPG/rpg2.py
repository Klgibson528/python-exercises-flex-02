import random
class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
   
    def attack(self, opponent):
        print("{} delt {} damage to the {}".format(self.name, self.dmg, opponent.name))
        if opponent.name == 'Goblin':
            opponent.hp -= self.dmg*random.randint(1, 6)
        else:
            opponent.hp -= self.dmg*random.randint(1, 3)
    def alive(self):
        return self.hp > 0
        
    def print_status(self):
        print("{} has {} hit points left!".format(self.name, self.hp))
        
        
class Hero(Character):
    pass
        
    
class Goblin(Character):
    pass
    
hero = Hero('Hero', 10, 1)
goblin =Goblin('Goblin', 6, 1)

def main():
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.alive() == False:
                print("Victory!!!")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Run awaaaaaaaayyyy")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.alive() == False:
                print("You are dead.")
    
main()