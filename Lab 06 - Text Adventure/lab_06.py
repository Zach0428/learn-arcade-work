
class Room:
    """
    This is the class that represents the room.
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("You are standing in the porch. There are shoes scattered on the ground."
                "There is a hallway to the west and a garage to the east.",
                None, 1, None, 3)
    room_list.append(room)
    room = Room("You are standing in the garage. There is a nice car in here."
                "There is a pool to the north and a porch to the west",
                2, None, None, 0)
    room_list.append(room)
    room = Room("You are standing next to the pool. It is full of chocolate milk."
                "There is a garage to the south.",
                None, None, 1, None)
    room_list.append(room)
    room = Room("You are standing in the east hallway. There are some nice statues and paintings"
                "There is a kitchen to the north, porch to the east, bedroom to the south, "
                "and a west hallway to the west.",
                7, 0, 6, 4)
    room_list.append(room)
    room = Room("You are standing in the west Hallway. There is a piano at the end of it."
                "There is a living room to the north, a bedroom to the south, and a east hallway to the west.",
                8, 3, 5, None)
    room_list.append(room)
    room = Room("You are standing in the master bedroom. There is a bed and a desk in the room."
                "There is a west hallway to the north and a bedroom to the east.",
                4, 6, None, None)
    room_list.append(room)
    room = Room("You are standing in the guest room. There is a desk with a smaller bed in here."
                "There is a east hallway to the north and a master bedroom to the west.",
                3, None, None, 5)
    room_list.append(room)
    room = Room("You are standing in the kitchen. There are some sharp knives."
                "There is a living room to the West and a east hallway to the south.",
                None, None, 3, 8)
    room_list.append(room)
    room = Room("You are standing in the living room. There is a couple couches and a TV in here."
                "There is a kitchen to the east and a west hallway to the south.",
                None, 7, 4, None)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to do?")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print("Get out of my house!")

        else:
            print("Pick again.")


main()
