# Example of for loop
my_name = "Alice"
for letter in my_name:
    print(letter)
# A
# l
# i
# c
# e

# An f-string is something we can use in python to help us print variables inside of a string 
index = 1
for item in groceries:
    print(f'{index}. {item}')
    index += 1

# 1. stuff
# 2. things
# 3. cool
# 4. shit

# range (start,stop,step)
for i in range(0, 10, 1):
    print(i) # prints 0-9

# slice[start,stop,step]
rainbow = ['red', 'orange', 'yellow', 'green', 'blue']
rainbow[1:4] = ['orange','yellow', 'green']
rainbow[3:] = ['green','blue']

my_name = 'Alice'
my_name[:3] # Ali

#-------------------
# Membership Testing - List & Tuples
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits # False
'eggplant' not in fruits # True

'eggplant' in vegetables # True
'eggplant' not in vegetables # False

# Index
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list

# Count
my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat') # 2
my_pets.count('lizard') # 0

# Membership Testing - Range 
nums = range(10)

0 in nums # True
10 in nums # False
4 in nums # True

0 not in nums # False
15 not in nums # True
10 not in nums # True


nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True


nums = range(1, 10, 2)

nums.index(5) # 2
nums.index(10) # ValueError: 10 is not in list
nums.index(1) # 0

# -----------------------------
# Sequence Operations Common to All Types
# Concatenate 
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums3 = nums1 + num2 # [1, 2, 3, 4, 5, 6]

# Count
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.count(4.0) # 2

#In
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

3.2 in student_gpas # True

# Index 
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.index(4.0) # 1

# Len 
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

len(my_pets) # 4

# Max 
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

max(student_gpas) # 4.0

# Min
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

min(student_gpas) # 1.5

# Multiply 
nums1 = [1, 2, 3]

nums1 * 2 # [1, 2, 3, 1, 2, 3]

# Not in
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

'Jellybean' not in my_pets # True

# Slice 
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas[1:3] # [4.0, 3.2]

# -----------------------------
# Mutable Sequence Only Operations 
# Append 
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

my_pets.append('Vera') # ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

# Del 
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

del my_pets[0:2] # ['Ernie', 'Squash', 'Vera']

# Insert 
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

fruits.insert(2, 'kiwi') # ['apple', 'banana', 'kiwi', 'orange', 'pear', 'strawberry']

# Pop 
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

apple = fruits.pop(0) # ['banana', 'orange', 'pear', 'strawberry'], apple = 'apple'

# Remove 
student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.remove(4.0) # [2.5, 3.2, 2.9, 3.7, 1.5, 4.0]

# Reverse 
my_pets = ['Ernie', 'Squash', 'Vera']

my_pets.reverse() # ['Vera', 'Squash', 'Ernie']