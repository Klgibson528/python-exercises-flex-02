# Phonebook app
book = [{'name':'Katy Gibson'  'phonenumber':'281-728-7870' 'email': 'klgibson528@gmail.com'}]

def intro():
    print ("""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Restore saved entries
7. Quit""")
#use pickle to save data 
#use pickle to call saved data
    ans = int(input("What would you like to do? Please enter a number. "))

    if ans == 1:
        ent = input("Who would you like to look up? ")
        print (book[ent])  
        
    elif ans == 2:
        name = input("Full name: ")
        num = input("Phone number: ")
        email = input("Email: ")
        website = input("Website: ")
        book[name] = num
        print ('An entry for ' + name + " was saved.")
        
    elif ans == 3:
        name = input("Who would you like to delete? ")
        del book[name]
        
    
    elif ans == 4:
        for key, value in book.items():
            print ('{}: {}'.format(key, value))
    elif ans == 5:
        
    elif ans == 6:
        
    else:
        print ("Thank you for using the phonebook!")

def save_entries:
    import pickle
    with open('data.pickle', 'wb') as fh:
        pickle.dump(book, fh)

def load_entries:
    import pickle
    with open('data.pickle', 'rb') as fh:
        book = pickle.load(fh)
        print(book)
    
intro()

