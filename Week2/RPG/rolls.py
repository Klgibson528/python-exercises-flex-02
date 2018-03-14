import random
def dm_roll():
    roll = random.randint(1, 20)
    print(roll)
    enemy = ""
    if roll > 0 and roll <= 10:
        enemy = 'Goblin'
    elif roll > 10 and roll <= 16:
        enemy = 'Zombie'
    elif roll > 16 and roll <= 19:
        enemy = 'Ogre'
    else:
        enemy = 'Dragon'
    
    print(enemy)

dm_roll()

def player_roll():
    roll = random.randint(1, 20)
    print(roll)
    if roll > 5 and roll < 17:
        attack()
    elif roll >= 17:
        return attack() *2
    else: 
        print('You missed!')
