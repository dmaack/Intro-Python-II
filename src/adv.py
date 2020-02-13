from room import Room
from player import Player
from item import Item

# Declare all the items
flashlight = Item('Flashlight', 'May it be a light to you in dark places')
compass = Item('Compass', 'May this point you in the right directions')
sword = Item('Sword', 'May this help in your defense')



# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", flashlight),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", compass),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", sword),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(input('\n-> Hi! Welcome to the game. To get started please enter your name: '), room['outside'])
print(f'\nHello, {player.name}!')
#direction = ''
# Write a loop that:
print('\n To move into a room your options are: [n] North [s] South [e] East [w] West [d] Drop Item [a] Add Item to Inventory or [q] Quit')
print(player.current_room)

while True:
    if player.current_room.name == 'Treasure Chamber':
        print('\n CONGRATS! YOU WIN!', player.name)
    #print('\n', player.name, '!')
    cmd = input('--> ').lower()
    if cmd in ['n', 's', 'e', 'w']:
        player.travel(cmd)
    # elif cmd == 'd':
    #     print()
    elif cmd == 'a':
        player.add_item(cmd)
        print(f'-- You picked up {player.current_room.items}')
    elif cmd == 'q':
        print('Goodbye!')
        exit()
    else:
        print('Invalid Input, try again')
        print('\nTo move into a room your options are: [n] North [s] South [e] East [w] West or [q] Quit')


    

    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

   
# If the user enters "q", quit the game.

