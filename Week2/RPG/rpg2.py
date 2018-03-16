import random

class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
   
    def attack(self, opponent):
        roll = random.randint(1, 20)
        print('{} rolled a {}'.format(self.name, roll))
        if roll > opponent.ac:
            print("{} delt {} damage to the {}".format(self.name, str(self.dmg * 2), opponent.name))
            opponent.hp -= self.dmg
        elif roll > opponent.ac and roll >= 17:
            print('{} crits and deals double damage!'.format(self.name))
            opponent.hp -= self.dmg * 2   
        else: 
            print('You missed!')
        
    def alive(self):
        return self.hp > 0
        
    def print_status(self):
        print("{} has {} hit points left!".format(self.name, self.hp))
        
class Monster(Character):
    def __init__(self, name, hp, ac, dmg, bounty):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.bounty = bounty

class Hero(Character):
    def __init__(self, name, hp, ac, dmg, coins):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.coins = coins

class Healing_Potion(object):
    cost = 5
    name = 'healing potion'
    def apply(self, hero):
        hero.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))
        
class Defense_Potion(object):
    cost = 5
    name = 'defense potion'
    def apply(self, hero):
        hero.defense = 2
        print("{}'s will now take 2 less damage from opponents!".format(hero.name))

class Great_Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))
class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.ac += 2
        print("{}'s AC has increased to {}!".format(hero.name, hero.ac))
        
class Store(object):
    items = [Healing_Potion, Defense_Potion, Great_Sword, Armor]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            input = int(input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)
        
def setup():
    print("""
Welcome, Adventurer!  
Thank you for coming to rescue our town.    
There are many monsters to fight, so let's begin!""")
    spec = input('Are your a Fighter, Cleric, Wizard or a Rouge? ')
    spec = spec.lower()
    
    if spec == 'fighter':
        hero = Hero('Fighter', 15, 10, 8, 20)
    elif spec == 'cleric':
        hero = Hero('Cleric', 10, 10, 8, 10)
    elif spec == 'wizard':
        hero = Hero('Wizard', 15, 10, 8, 20)
    elif spec == 'rouge':
        hero = Hero('Rouge', 10, 16, 8, 10)
    print("You have chosen {}.".format(spec))
    return hero
        
def dm_roll():
    roll = random.randint(1, 20)
   
    if roll > 0 and roll <= 10:
        opponent = Monster('Goblin', 6, 10, 2, 1)
    elif roll > 10 and roll <= 16:
        opponent = Monster('Zombie', 8, 12, 3, 3)
    elif roll > 16 and roll <= 19:
        opponent = Monster('Ogre', 15, 15, 5, 5)
    else:
        opponent = Monster('Dragon', 1000000, 20, 10, 100)
    print("You have run into a {}!".format(opponent.name))
    return opponent
    
    
def fight():
    
    while opponent.alive() and hero.alive():
        hero.print_status()
        opponent.print_status()
        print("What do you want to do?")
        print("1. Fight {}".format(opponent.name))
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks opponent
            hero.attack(opponent)
            if opponent.alive() == False:
                print("Victory!!!")
                print("You collect the bounty for the {}, which is {} coins.".format(opponent.name, opponent.bounty))
                hero.coins += opponent.bounty
                print("You now have {} coins!".format(hero.coins))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Run awaaaaaaaayyyy")
            loss = random.randint(1,5)
            print("As you run away you drop {} coins.".format(loss))
            hero.coins -= loss
            if hero.coins <= 0:
                print ("You have no more coins")
            else:
                print ("You now have {} coins.".format(hero.coins))
            break
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.alive():
            # opponent attacks hero
            opponent.attack(hero)
            if hero.alive() == False:
                print("You are dead.")

def cont():
    ans = int(input("""Would you like to: 
1. Continue adventuring
2. Go to the store
3. Go home"""))
    if ans == 1:
        fight()
    elif ans == 2:
        store()
    else:
        print("Thank you for your help!")
        

if __name__ == "__main__":
  hero = setup()
  opponent = dm_roll()
  fight()
  
  
  
