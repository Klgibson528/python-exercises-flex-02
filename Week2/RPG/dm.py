import random
def dm_roll():
    roll = random.randint(1, 20)
    print(roll)
    opponent = ""
    if roll > 0 and roll <= 10:
        opponent = 'Goblin'
    elif roll > 10 and roll <= 16:
        opponent = 'Zombie'
    elif roll > 16 and roll <= 19:
        opponent = 'Ogre'
    else:
        opponent = 'Dragon'
    
    print(opponent)

dm_roll()