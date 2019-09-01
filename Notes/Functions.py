# Example of a function
def favorite_show():
    print("Game of Thrones")

# Calling a function
favorite_show() 

# Function with multiple parameters
def add_two_nums(num1, num2):
    val = num1 + num2
    return val

print(add_two_nums(5, 10)) # Prints out 15

# -------- Packing -------- 

def packer(*args): # reads it as a tuple? 
    print(args)

packer('hi','i','love','python')

def calculate_total(*args) # you use *args when you dont know how many args you are gonna use
    total = sum(args)       # args is a tuple 
    print(total)

calculate_total(25,25,20,30) # prints out 100 

# -------- UnPacking -------- 

def unpacker():
    return(1,2,3)

var1, var2, var3 = unpacker() # var1 = 1 var2 = 2 var3 = 3

first, name = input('Enter your full name: \n').split(' ')

