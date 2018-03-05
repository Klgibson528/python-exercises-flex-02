# Guess the Number Game
import random
answer = random.randint(1, 10)
print answer 
print "I am thinking of a number between 1 and 10."
count = 0
num_guess = 5
print "You can guess 5 times."
guess = int(input("What number am I thinking of? "))
while count < 4:
    count += 1
    if guess < answer:
        print "That's too low."
        num_guess -= 1
        print "You have " + str((num_guess)) + " guesses left."
        guess = int(input("What number am I thinking of? "))
        
    elif guess > answer:
        print "That's too high."
        num_guess -= 1
        print "You have " + str((num_guess)) + " guesses left."
        guess = int(input("What number am I thinking of? "))
    
    else:
        print "You got it!"
        break
if count == 4:
    print "You ran out of turns!"