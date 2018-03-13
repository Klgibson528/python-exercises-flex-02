class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
   
    def attack(self, opponent):
        print("{} delt {} damage to the {}".format(self.name, self.dmg, opponent))
        return opponent.hp - self.dmg 
        
        
class Hero(Character):
    
        
    
class Goblin(Character):
    
    
hero = Hero(input("What's your name? "))
goblin =Goblin('Goblin')

def main():
    while goblin.hp > 0 and hero.hp > 0:
        print("You have {} health and {} power.".format(hero.hp, hero.dmg))
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