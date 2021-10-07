
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
    room = Room("You are standing in the Porch. There are shoes scattered on the ground."
                "There is a hallway to the west and a garage to the east.",
                None, 1, None, 3)
    room_list.append(room)
    room = Room("You are standing in the Garage. There is a nice car in here."
                "There is a pool to the north and a porch to the west",
                2, None, None, 0)
    room_list.append(room)
    room = Room("You are standing next to the Pool. It is full of chocolate milk."
                "There is a garage to the south.",
                None, None, 1, None)
    room_list.append(room)
    room = Room("You are standing in the East Hallway. There are some nice statues and paintings"
                "There is a Kitchen to the north, Porch to the east, Bedroom to the south, "
                "and a West Hallway to the west.",
                7, 0, 6, 4)
    room_list.append(room)
    room = Room("You are standing in the West Hallway. There is a piano at the end of it."
                "There is a Living Room to the north, a Bedroom to the south, and a East Hallway to the west.",
                8, 3, 5, None)
    room_list.append(room)
    room = Room("You are standing in the Master Bedroom. There is a bed and a desk in the room."
                "There is a West Hallway to the north and a bedroom to the east.",
                4, 6, None, None)
    room_list.append(room)
    room = Room("You are standing in the Guest Room. There is a desk with a smaller bed in here."
                "There is a East Hallway to the north and a Master Bedroom to the west.",
                3, None, None, 5)
    room_list.append(room)
    room = Room("You are standing in the Kitchen. There are some sharp knives."
                "There is a Living Room to the West and a East Hallway to the south.",
                None, None, 3, 8)
    room_list.append(room)
    room = Room("You are standing in the Living Room. There is a couple couches and a TV in here."
                "There is a Kitchen to the east and a West Hallway to the south.",
                None, 7, 4, None)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to Do?")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north





main()

