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