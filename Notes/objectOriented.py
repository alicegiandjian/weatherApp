# example of a class 
class Student:
    name = "Alice"

me = Student() # create instance of class
print(me.name) # prints name from that instance 

# Intro to Methods 
class Thief: 
    sneaky = True

    def pickpocket(self):
        print("Called by {}".format(self))
        return bool(random.randint(0,1))

        # alice = Thief()
        # alice.pickpocket() or Thief.pickpocket(alice) 

    def sneakyPick(self):
        if self.sneaky:     # if the instance is sneaky then continue 
            return bool(random.randint(0,1))
        return False

# Example Using Self
# When you instantiate the class with me = Student() you then use the 'me' instance (variable) to call the functions in the class. 
# Also, this snippet does not print anything; you could do that a couple of different ways, but this should do the trick:
class Student:
    name = "Alice"

    def praise(self):
        pos = "You're doing a great job, {}".format(self.name)
        return pos 

me = Student() 
print(me.praise())