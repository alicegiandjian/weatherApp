# ----------------- Section 1 ----------------- 

# Example of empty List
temp = [] 

# How to find out how many items are in a list
len(temp)

# Add Item to list
temp.append(98.4) # Adds 98.4
temp.append(22.4) # Adds 22.4 
# Inside list should now look like [98.4, 22.4]

# How to add one list to another list 
temp1 = [98.4, 22.4]
temp2 = [33.4, 52.4]
temp1.extend(temp2)
# Inside list should now look like [98.4, 22.4, 33.4, 52.4]
# This changes temp1 though

# How to add one list to another, without altering current lists and creating new one
primary_care_doctors = ["Dr. Stuff", "Dr. Things"]
er_doctors = ["Dr. Pepper", "Dr. IDK"]
all_doctors = primary_care_doctors + er_doctors
# Inside list should now look like all_doctors = ["Dr. Stuff", "Dr. Things", "Dr. Pepper", "Dr. IDK"]

# You can have multiple data types in the same area like a string and int 

# Books example list
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis", # - Wes McKinney
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

# How to access first item
books[0]

# How to access and change second item
books[1] = "Python for Data Analysis - Wes McKinney"

# How to access the last item in list
books[-1]

# How to access the 2nd to last item in list
books[-2]

# Can use in formating as following example
print("Suggested gift: {}".format(books[0]))
# Prints "Suggested gift: Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart"

# Insert item into list at first spot
books.insert(0, "Learning Python: Powerful Object-Oriented Programming")
# Should now look like below: 
books = [
    "Learning Python: Powerful Object-Oriented Programming",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney", 
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

# Add more to the string (forgot the author)
books[0] += " - Mark Lutz"
# Should now look like: "Learning Python: Powerful Object-Oriented Programming - Mark Lutz"

# Strings are immutable (you can't change them)
Lyrics = "Books check em out"
# lyrics[0] is 'B' 
# lyrics[0] = "C" will not work, will give error 

# New Books Array 
books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

# Delete something from list 
del books[0]
# Learning Python is now gone, Automate the Boring stuff is now first 

# delete the last thing added to list
books.pop() # rid hello web apps
# or if you wanna delete the first one
books.pop(0) # auto mate the boring stuff now gone

# or you can actually use it to save
fav_book = books.pop() 

# ----------------- Section 2 ----------------- 

# How to itterate through books array
for book in books:
    print( "* " + book) 

# How to copy a list 
copy = original.copy() 

# Split a string into multiple words (based off whitespace?)
quote = "The greatest teacher failure is"
words = quote.split() 
# words = ['The', 'greatest', 'teacher', 'failure', 'is']

# This prints a word every .5 seconds
for word in words:
        print(word)
        time.sleep(.5)

# convert text into a list
text = "Ada&Jean&Grace"
text.split("&")
# text = ["Ada", "Jean", "Grace"]
# .join() does the same thing by turning a list into a string

# list of lists
travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]
# travel_expenses[0] = [5.00, 2.75, 22.00, 0.00, 0.00]
# travel_expenses[0][1] = 2.75 

# how to itterate through list of lists
print("Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number,sum(week)))
    week_numer += 1
    # Week #1: $29.75
    # Week #2: $75,25
    # Week #3: $42.25
    