# #Exercise 1 - Hello, you!
# name = raw_input("What is your name? ")
# print "Hello, " + name + "!"
  
# #Exercise 2 - HELLO, YOU!
# new_string = "Hello, "+ name + "!"
# print new_string.upper()
# print "YOUR NAME HAS " + str(len(name)) + " IN IT!"

# #Exercise 3 - Madlib
# name= raw_input("Give me a name ")
# job= raw_input("Give me a job ")
# food= raw_input("Give me a food ")
# print "%s is a %s who enjoys eating %s" % (name, job, food)

# Exercise 4 - Day of the Week
day = int(input('Day (0-6)? '))
if day == 0:
  print "Sunday"
elif day == 1:
  print "Monday"
elif day == 2:
  print "Tuesday"
elif day == 3:
  print "Wednesday"
elif day == 4:
  print "Thursday"
elif day == 5:
  print "Friday"
elif day == 6:
  print "Saturday"
else:
  print "That number is not between 0 and 6"