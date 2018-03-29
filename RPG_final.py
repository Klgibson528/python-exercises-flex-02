import random


class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self, opponent):
        roll = random.randint(1, 20)
        print('{} rolled a {}'.format(self.name, roll))
        if roll > opponent.ac and roll < 17:
            print("{} delt {} damage to the {}".format(
                self.name, str(self.dmg - opponent.defense), opponent.name))
            opponent.hp -= (self.dmg - opponent.defense)
        elif roll > opponent.ac and roll >= 17:
            print('{} crits and deals double damage!'.format(self.name))
            opponent.hp -= (self.dmg * 2 - opponent.defense)
        else:
            print('You missed!')

    def alive(self):
        return self.hp > 0

    def print_status(self):
        print("{} has {} hit points left!".format(self.name, self.hp))


class Monster(Character):
    def __init__(self, name, hp, ac, dmg, defense, bounty):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.defense = defense
        self.bounty = bounty


class Hero(Character):
    def __init__(self, name, hp, ac, dmg, defense, coins):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.defense = defense
        self.coins = coins


class Healing_Potion(object):
    cost = 5
    name = 'healing potion'

    def apply(self, hero):
        hero.hp += 2
        print("{}'s health increased to {}.".format(hero.name, hero.hp))


class Defense_Potion(object):
    cost = 5
    name = 'defense potion'

    def apply(self, hero):
        hero.defense = 2
        print("{}'s will now take 2 less damage from opponents!".format(
            hero.name))


class Great_Sword(object):
    cost = 10
    name = 'sword'

    def apply(self, hero):
        hero.dmg += 2
        print("{}'s power increased to {}.".format(hero.name, hero.dmg))


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
            print("What would you like to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("5. leave")
            inp = int(input("> "))
            if inp == 1:
                heal = Healing_Potion()
                heal.apply(hero)
                hero.coins -= heal.cost
            elif inp == 2:
                defense = Defense_Potion()
                defense.apply(hero)
                hero.coins -= defense.cost
            elif inp == 3:
                sword = Great_Sword()
                sword.apply(hero)
                hero.coins -= sword.cost
            elif inp == 4:
                armor = Armor()
                armor.apply(hero)
                hero.coins -= armor.cost
            else:
                print("Come again!")
                cont()


def setup():
    print("""
Welcome, Adventurer!  
Thank you for coming to rescue our town.    
There are many monsters to fight, so let's begin!""")
    spec = input('Are your a Fighter, Cleric, Wizard or a Rogue? ')
    spec = spec.lower()

    if spec == 'fighter':
        hero = Hero('Fighter', 15, 10, 8, 0, 20)
    elif spec == 'cleric':
        hero = Hero('Cleric', 10, 10, 8, 0, 10)
    elif spec == 'wizard':
        hero = Hero('Wizard', 15, 10, 8, 0, 20)
    elif spec == 'rouge':
        hero = Hero('Rogue', 10, 16, 8, 0, 10)
    else:
        print("That's not an option!")
        setup()
    print("You have chosen {}.".format(spec))
    return hero


def dm_roll():
    roll = random.randint(1, 20)

    if roll > 0 and roll <= 10:
        opponent = Monster('Goblin', 9, 10, 2, 0, 1)
    elif roll > 10 and roll <= 16:
        opponent = Monster('Zombie', 13, 12, 3, 0, 3)
    elif roll > 16 and roll <= 19:
        opponent = Monster('Ogre', 15, 15, 5, 0, 5)
    else:
        opponent = Monster('Dragon', 1000000, 20, 10, 0, 100)
    print("You have run into a {}!".format(opponent.name))
    return opponent


def fight():
    opponent = dm_roll()
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
                print("You collect the bounty for the {}, which is {} coins.".
                      format(opponent.name, opponent.bounty))
                hero.coins += opponent.bounty
                print("You now have {} coins!".format(hero.coins))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Run awaaaaaaaayyyy")
            loss = random.randint(1, 5)
            print("As you run away you drop {} coins.".format(loss))
            hero.coins -= loss
            if hero.coins <= 0:
                print("You have no more coins")
            else:
                print("You now have {} coins.".format(hero.coins))
            break
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.alive():
            # opponent attacks hero
            opponent.attack(hero)
            if hero.alive() == False:
                print("You are dead.")


def cont():
    ans = int(
        input("""Would you like to: 
1. Continue adventuring
2. Go to the store
3. Go home
> """))
    if ans == 1:
        fight()
    elif ans == 2:
        store = Store()
        store.do_shopping(hero)
        return store
    else:
        print("Thank you for your help!")


if __name__ == "__main__":
    hero = setup()
    opponent = dm_roll()
    fight()
    store = cont()
    cont()
