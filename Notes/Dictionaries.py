{key:value} # Dictionary

# Accessing value from dictionaries 
course = {'teacher':'Ashely', 'title':'Introducting Dictionaries','level':'beginner'}
print(course['teacher']) # Prints 'Ashely'

course.keys() # access all keys
course.values() # access all values

# How to change value in dictionary 
course['level'] = 'hard'

# How to add a new value 
course['stages'] = 2 # course = {'teacher':'Ashely', 'title':'Introducting Dictionaries','level':'beginner', 'stages':2}

# How to iterate dictionaries
for key, value in course.items():
    print(key)
    print(value)

# Packing 

def print_teacher(**kkwargs):
    for key, value in kkwargs.items():
        print(f'{key}: {value}')

print_teacher(name='Ashley', job='Instructor',topic='python')