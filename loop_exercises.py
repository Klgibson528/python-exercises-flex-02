# # 1 to 10
# count = 0 
# while count in range(0,10):
#     count += 1
#     print count

# # n to m
# n = int(input("Where would you like to start? "))
# m = int(input("Where would you like to end? "))
# count = n-1
# while count in range(n-1, m):
#     count += 1
#     print count

# # Odd numbers
# count = 1 
# while count in range(1, 10):
#     print count
#     count += 2 
    
# # 5 x 5 Square
# count = 0 
# while count < 5:
#     print "*" * 5
#     count += 1

# # How big is the square?
# count = 0
# big = int(input("How big is the square? "))
# while count < big:
#     print "*" * big
#     count += 1

# Print a Box
count = 0 
h = int(input("How tall is your square? "))
w = int(input("How wide is your square?"))
print "*"*w
while count < h-2:
    print "*" + (" "*(w-2)) + "*"
    count += 1
print "*"*w

# # Print a Triangle
# count = 1
# while count < 16:
#     print ("*" * count).center(15)
#     count += 2

# # Print a Triangle - Height
# height = int(input("How tall is your triangle? "))
# count = 1
# while count < height*2:
#     print ("*" * count).center(height*2-1)
#     count += 2

# # Multiplication Table
# n = 1
# while n < 11:
#     print "1 x "+ str(n) + " = " + str(1*n)
#     n += 1
# # not sure how to move to next set