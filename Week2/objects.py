# # Basics
# class Person:
#     def __init__(self, name, email, phone, greet_count):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.greet_count = greet_count
#         friends = []
#         self.friends = friends

#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))
#         self.greet_count += 1
#         print('You have had {} greetings!'.format(self.greet_count))
        
#     def contact(self):
#         return ('Name: {}\nEmail: {}\nPhone: {}').format(self.name, self.email, self.phone)
    
#     def add_friend(self, friend):
#         self.friends.append(friend)
        
#     def num_friends(self):
#         print (len(self.friends))
#     def __str__(self):
#         return 'Name: {}\nEmail: {}\nPhone: {}'.format(self.name, self.email, self.phone)

# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', 0)
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', 0)

# sonny.greet(jordan)
# sonny.greet(jordan)
# jordan.greet(sonny)

# print (sonny.contact())
# print (jordan.contact())

# jordan.add_friend(sonny)
# jordan.num_friends()

# print(jordan)

# # Make your own class
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def print_info(self):
#         return ('{} {} {}'.format(self.year,self.make, self.model))

# car = Vehicle('Chevy', 'Aveo', '2008')

# print(Vehicle.print_info(car))