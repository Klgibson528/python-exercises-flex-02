# Phonebook app
import pickle
def load_entries():
    global book
    with open('data.pickle', 'rb') as fh:
        book = pickle.load(fh)
load_entries()

def save_entries():
    with open('data.pickle', 'wb') as fh:
        pickle.dump(book, fh)
        
book = {}

def intro():
    while True:
        print ("""Electronic Phone Book)
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
            ent = ent.lower()
            load_entries()
            if ent in book:
                print (book[ent])
            else:
                print ("There is no listing for that person.")
        elif ans == 2:
            name = input("Full name: ")
            name = name.lower()
            num = input("Phone number: ")
            email = input("Email: ")
            book[name] = {}
            book[name]['phone'] = num
            book[name]['email'] = email
            save_entries()
            print ('An entry for ' + name + " was saved.")
            
        elif ans == 3:
            name = input("Who would you like to delete? ")
            name = name.lower()
            load_entries()
            del book[name]
            save_entries()
        elif ans == 4:
            load_entries()
            for key, value in book.items():
                print ('{}: {}'.format(key, value))
        elif ans == 5:
            save_entries()
        elif ans == 6:
            load_entries()
        elif:
            print ("Thank you for using the phonebook!")
            break
        else: 
            print ("Please enter a number 1-7")

intro()