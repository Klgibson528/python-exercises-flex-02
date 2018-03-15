import random

class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
   
    def attack(self, opponent):
        roll = random.randint(1, 20)
        print('{} rolled a {}'.format(self.name, roll))
        if roll > 5 and roll < 17:
            print("{} delt {} damage to the {}".format(self.name, self.dmg, opponent.name))
            opponent.hp -= self.dmg
        elif roll >= 17:
            print('{} crits and deals double damage!'.format(self.name))
            opponent.hp -= self.dmg * 2   
        else: 
            print('You missed!')
        
        
    def alive(self):
        return self.hp > 0
        
    def print_status(self):
        print("{} has {} hit points left!".format(self.name, self.hp))
        
        
def setup():
    print("""
Welcome, Adventurer!  
Thank you for coming to rescue our town.    
There are many monsters to fight, so let's begin!""")
    spec = input('Are your a Fighter, Cleric, Wizard or a Rouge? ')
    spec = spec.lower()
    
    if spec == 'fighter':
    elif spec == 'cleric':
    elif spec == 'wizard':
    elif spec == 'rouge':
        
        
def main():
    
    while opponent.alive() and hero.alive():
        hero.print_status()
        opponent.print_status()
        print("What do you want to do?")
        print("1. Fight {}".format(opponent))
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks opponent
            hero.attack(opponent)
            if opponent.alive() == False:
                print("Victory!!!")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Run awaaaaaaaayyyy")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.alive():
            # opponent attacks hero
            opponent.attack(hero)
            if hero.alive() == False:
                print("You are dead.")
    
setup()
main()