from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

player_name = input('\nHi! Welcome to the game. To get started please enter your name: ') 
player = Player(player_name, room['outside'])

#direction = ''
# Write a loop that:


while True:

    

    #print('\n', player.name, '!')
    print('\n You are in:', player.current_room.name)
    print(' Description: ', player.current_room.description)
    #print('\nHello', player.name, '! You are currently in the:', player.current_room)
    if player.current_room.name == 'Treasure Chamber':
        print('\nYOU WIN!', player.name)
    direction = input(f'\n To move into a room, tell me your next move. \n Your options are [n] North [s] South [e] East [w] West or [q] Quit: ')
    # for i in direction:
    #     if i not in ['n', 's', 'e', 'w', 'q']:
    #         print('Please enter a valid direction: n, s, e, w, or q')
    #         continue
    #     else:
    #         print('You have now moved to: ', player.current_room.name)

    if direction != None:
        if direction == 'q':
            print('\nThanks for playing!\n')
            break
        elif direction == 'n':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
                continue
            else:
                print('\n Sorry, cant go that way. Try Again')
                continue
        elif direction == 's':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
                continue
            else:
                print('\n Sorry, cant go that way. Try Again')
                continue
        # player.current_room = player.current_room.s_to
        elif direction == 'e':
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
                continue
            else:
                print('\n Sorry, cant go that way. Try Again')
                continue
        elif direction == 'w':
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
                continue
            else:
                print('\n Sorry, cant go that way. Try Again')
                continue
    
    else:
        print('Invalid input')

    #break
    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

   
# If the user enters "q", quit the game.

