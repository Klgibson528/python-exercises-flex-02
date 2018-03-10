# # Exercise 1 
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# print (phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'

# print (phonebook_dict)

# # Exercise 2: Nested Dictionaries
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print (ramit['email'])
# print (ramit['interests'][0])
# print (ramit['friends'][0]['email'])
# print (ramit['friends'][1]['interests'][1])

# Letter Summary
# def letter_histogram(word):
#     summary = {}
#     for i in word:
#         if i in summary:
#             summary[i] += 1
            
#         else:
#             summary[i] = 1
            
#     print (summary)
    
# letter_histogram('Hello')

# # Word Summary
# def word_histogram(par):
#     summary = {}
#     words = par.split(' ')
#     low = []
#     for i in words:
#         low.append(i.lower())
    
#     for i in low:
#         if i in summary:
#             summary[i] += 1
            
#         else:
#             summary[i] = 1
            
#     print (summary)
    
# word_histogram('Apples eat apples but pears eat apples too. Pears are evil.')
# #curious how to remove periods at the end of sentences

