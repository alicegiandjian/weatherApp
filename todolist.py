# Create a new empty list named item_list
item_list = [] 

def show_help(): 
    print("What do you need to do?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see current list.
    """)


# Create a function named add_to_list that declares a paramter named item 
    # Add item to the list
def add_to_list(item):
    item_list.append(item)
    # Notify user that the item was added, and state the number of items currently in the list
    print("Added! List has {} items".format(len(item_list)))

# Define a function named show_list that prints all the items in the list
def show_list():
    print("List: ")
    for item in item_list:
        print(item)

show_help() 
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue # will send you back to the while loop 
        # Enable the SHOW commant to show the list
    elif new_item == 'SHOW':
        show_list()
        continue

    # Call add_to_list with new_item as an argument 
    add_to_list(new_item)

show_list()