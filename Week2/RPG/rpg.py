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

setup()

# greeting()
# import random 

# def main():
#     hero_health = random.randint(10, 15)
#     hero_power = random.randint(1, 6)
#     goblin_health = random.randint(7, 10)
#     goblin_power = random.randint(2, 4)

#     while goblin_health > 0 and hero_health > 0:
#         print("{} has {} health and {} power.".format(name, hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()
