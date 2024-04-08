class Room:
    def __init__(self, number='', name='', description='',north=None, east=None, south=None, west=None):
        self.number = number
        self.name = name
        self.description = description
        self.north_room = north
        self.east_room = east
        self.south_room = south
        self.west_room = west


def enter_room(room):
    print(f"You entered the {room.name.lower()}: {room.description}.")
    print()


def main():
    rooms = []

    rooms.append(Room(0, "Living Room"))
    rooms.append(Room(1, "Kitchen"))
    rooms.append(Room(2, "Bedroom"))
    rooms.append(Room(3, "Bathroom"))
    rooms.append(Room(4, "Guest Room"))
    rooms.append(Room(5, "Hallway"))
    rooms.append(Room(6, "Balcony"))
    rooms.append(Room(7, "Study"))
    rooms.append(Room(8, "Dining Room"))

    # Set room descriptions
    rooms[0].description = ("The room has multiple couches and a very gothic feeling. In the middle of the room on the wall there is a fireplace with skulls above it\n"
                            "there is a door to the east and one to the north")
    rooms[1].description = ("Te kitchen feels more modern than the rest of the house leaving you questioning what you area ctually dealing with here\n"
                            ".there is a door to the east and to the south")
    rooms[2].description = ("The bedroom has coffins all over and is decorated with human bones, it is lit by only candle light...\n"
                            "there is a door to the west and to the north")
    rooms[3].description = ("The bathroom is too large to be just a simple bathroom.  There has to be something more to this...\n"
                            "there is a door to the east and to the west")
    rooms[4].description = ("The guest bedroom is filled with coffins and upside down crosses...\n"
                            "there is a door to the south")
    rooms[5].description = ("The hallway stretches for miles with suits of armor and what seems to be werewolf pelts as rugs...\n"
                            "there is a door to the north, east and south")
    rooms[6].description = ("you have reached the balcony, the door slams shut behind you and the rope seems to be cut.\n"
                            "You feel a presence above but before you could look up, everything goes black...")
    rooms[7].description = ("The study has bookshelves on every wall with books that seem to date hunndreds of years back...\n"
                            "there is a door to the north, east and south")
    rooms[8].description = ("The dining room has a long  table with a black candeleria in the middle and only one large, throne like seat at the head of the table"
                            "with the romanian flag...\n"
                            "there is a door to the north and to the east")

    #living room connection
    rooms[0].north_room = rooms[1]
    rooms[0].east_room = rooms[5]

    #kitchen connection
    rooms[1].east_room = rooms[7]
    rooms[1].south_room = rooms[0]

    #study connection
    rooms[7].west_room = rooms[1]
    rooms[7].south_room = rooms[5]
    rooms[7].north_room = rooms[4]

    #hallway connections
    rooms[5].south_room = rooms[8]
    rooms[5].north_room = rooms[7]
    rooms[5].west_room = rooms[0]

    #dining room connection
    rooms[8].east_room = rooms[3]
    rooms[8].north_room = rooms[5]

    #bathroom connection
    rooms[3].east_room = rooms[2]
    rooms[3].west_room = rooms[8]

    #bedroom connections
    rooms[2].north_room = rooms[6]
    rooms[2].west_room = rooms[3]

    #guest room
    rooms[4].south_room = rooms[7]


    current_room = rooms[0]
    enter_room(current_room)

    print("Welcome to David's Adventure! Try to escape out to the balcony and get down the rope.\n"
          "To change rooms, use cardinal direction inputs n, s, e, w.\nCan you escape?")
    print(f"you enter the abandoned mansion of your taker and find yourself standing in {current_room.name}: {current_room.description}")

    max_moves = 12
    moves_left = max_moves

    while moves_left >= 0:
        user_input = input("\nWhat would you like to do? ").strip().lower()

        if user_input == 'n' or user_input == 'north':
            if current_room.north_room:
                current_room = current_room.north_room
                enter_room(current_room)
            else:
                print("You can't go that way.")
        elif user_input == 'e' or user_input == 'east':
            if current_room.east_room:
                current_room = current_room.east_room
                enter_room(current_room)
            else:
                print("You can't go that way.")
        elif user_input == 's' or user_input == 'south':
            if current_room.south_room:
                current_room = current_room.south_room
                enter_room(current_room)
            else:
                print("You can't go that way.")
        elif user_input == 'w' or user_input == 'west':
            if current_room.west_room:
                current_room = current_room.west_room
                enter_room(current_room)
            else:
                print("You can't go that way.")
        else:
            print("Sorry, I didn't understand that. Please try again.")

        if user_input in ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']:
            moves_left -= 1

            if moves_left == 0:
                print("all the doors around you slam shut!  the room starts to shake...\n"
                      "You fall to the ground and feel the evil take over...")
                print("GAME OVER!")
                break

        if current_room.number == 6:
            print("You have completed the game!")
            break


if __name__ == "__main__":
    main()
