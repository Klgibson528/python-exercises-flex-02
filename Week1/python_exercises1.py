# #Exercise 1 - Hello, you!
# name = raw_input("What is your name? ")
# print "Hello, " + name + "!"
  
# #Exercise 2 - HELLO, YOU!
# name = raw_input("What is your name? ")
# new_string = "Hello, "+ name + "!"
# print new_string.upper()
# print "YOUR NAME HAS " + str(len(name)) + " IN IT!"

# #Exercise 3 - Madlib
# name= raw_input("Give me a name ")
# job= raw_input("Give me a job ")
# food= raw_input("Give me a food ")
# print "%s is a %s who enjoys eating %s" % (name, job, food)

# #Exercise 4 - Day of the Week
# day = int(input('Day (0-6)? '))
# if day == 0:
#   print "Sunday"
# elif day == 1:
#   print "Monday"
# elif day == 2:
#   print "Tuesday"
# elif day == 3:
#   print "Wednesday"
# elif day == 4:
#   print "Thursday"
# elif day == 5:
#   print "Friday"
# elif day == 6:
#   print "Saturday"
# else:
#   print "That number is not between 0 and 6"

# #Exercise 5 - Work or Sleep In?
# day = int(input('Day (0-6)? '))
# if day in range(1, 5):
#   print "Go to work!"
# elif day == 0 or day == 6:
#   print "You get to sleep in!"
# else:
#   print "That number is not between 0 and 6"

# #Exercise 6 - Celsius to Fahrenheit
# cel = int(input("Temperature in Celsius? "))
# far = cel * 1.8 + 32
# print str(cel) + " degrees celsius is equal to "+ str(far) +" degrees fahrenheit."

# #Exercise 7 - Tip Calculator
# total = int(input("Total bill amount? "))
# service = raw_input("Was the service good, fair, or bad? ")
# service = service.lower()
# if service == "good":
#   tip = .20 * total
#   print "Since your service was good you should leave a 20% tip which would be " + "$" + str("%.2f"%tip)+"."
# elif service == "fair":
#   tip = .15 * total
#   print "Since your service was fair you should leave a 15% tip which would be " + "$" + str("%.2f"%tip)+"."
# elif service == "bad":
#   tip = .10 * total
#   print "Since your service was bad you should leave a 10% tip which would be " + "$" + str("%.2f"%tip)+"."
# else:
#   print "Please rate your service as 'Good', 'Fair' or 'Bad'"
# #I want to figure out how to make it loop back if they enter something other than good, bad, or fair

# # #Exercise 8 - Tip Calculator 2
# total = int(input("Total bill amount? "))
# split = int(input("How many ways would you like to split the bill? "))
# total = total/split
# service = raw_input("Was the service good, fair, or bad? ")
# service = service.lower()
# if service == "good":
#   tip = (.20 * total)+total
#   print "With a 20% tip you will each pay " + "$" + str("%.2f"%tip)+"."
# elif service == "fair":
#   tip = (.15 * total)+total
#   print "With a 15% tip you will each pay " + "$" + str("%.2f"%tip)+"."
# elif service == "bad":
#   tip = (.10 * total)+total
#   print "With a 10% tip you will each pay " + "$" + str("%.2f"%tip)+"."


# #Exercise 9 - 1 to 10
# count = 0
# while count < 10:
#   count += 1
#   print count

# #Exercise 10 - How many coins?
# coins = 0 
# more = raw_input("Would you like a coin? ")
# while more == "yes":
#     coins += 1
#     print "You have " + str(coins) + " coins."
#     more = raw_input("Would you like another coin? ")

# if coins == 0:
#     print "You have no coins!"
# elif coins > 0:
#     print "You are leaving with " + str(coins) + " coins. Goodbye."

