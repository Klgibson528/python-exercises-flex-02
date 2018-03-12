class Character:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg
    def attack(self, dmg):
        
class Hero(Character):
    hp = 10
    dmg = 5
class Goblin(Character):
    hp = 6
    dmg = 2

def greeting():
    global name
    name = input("Welcome Hero, what is your name? ")
    name = name.capitalize()
    print ("""
***********************
{} is such a nice name. 
Thank you for coming to our town.    
There are many monsters to fight, so let's begin!""".format(name))

greeting()
import random 

def main():
    hero_health = random.randint(10, 15)
    hero_power = random.randint(1, 6)
    goblin_health = random.randint(7, 10)
    goblin_power = random.randint(2, 4)

    while goblin_health > 0 and hero_health > 0:
        print("{} has {} health and {} power.".format(name, hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()
