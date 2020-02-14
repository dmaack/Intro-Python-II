# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room
        self.inventory = []

    def travel(self, direction):
        #Grab the n/s/e/w attribute from the room
        next_room = getattr(self.current_room, f'{direction}_to')
        #item = getattr(self.current_room, self.current_room.items)
        if next_room is not None:
            self.current_room = next_room
            # self.current_room.items = item
            print(self.current_room)
            # print(self.current_room.items)
        else:
            print('You cannot go that direction')

    def take_item(self, item):
        found = False
        for i in self.current_room.items:
            if i.name.lower() == item:
                self.inventory.append(i)
                self.current_room.items.remove(i)
                found = True
                print(f'You picked up an {i.name} and added it to your inventory')
        if not found:
            print(f'This {item} is not in this room')
                    
    def drop_item(self, item):
        found = False
        for i in self.inventory:
            if i.name.lower() == item:
                self.inventory.remove(i)
                self.current_room.items.append(i) 
                found = True
                print(f'You have dropped {i.name} in {self.current_room.name}') 
        if not found:
            print(f'The {item} was not found in your inventory')        

