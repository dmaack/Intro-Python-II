# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, starting_room):
        self.name = name 
        self.current_room = starting_room
        self.items = []

    def travel(self, direction):
        #Grab the n/s/e/w attribute from the room
        next_room = getattr(self.current_room, f'{direction}_to')
        item = getattr(self.current_room, self.current_room.items)
        if next_room is not None:
            self.current_room = next_room
            self.current_room.items = item
            print(self.current_room)
            print(self.current_room.items)
        else:
            print('You cannot go that direction')
