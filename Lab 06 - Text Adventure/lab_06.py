class Room:
    def __init__(self, description='', north=None, east=None, south=None, west=None):
        self.description = description
        self.north_room = north
        self.east_room = east
        self.south_room = south
        self.west_room = west

def enter_room(room):
    print(f"You entered the {room.description.lower()}.")
    print(room.description)
    print()

def main():
    living_room = Room("Living Room", "There is a door to the kitchen to the north and a door to the hallway to the east.")
    kitchen = Room("Kitchen", "There is a door to the living room to the south.")
    bedroom = Room("Bedroom", "There is a door to the hallway to the west, a door to the bathroom to the south, and a door to the guest room to the east.")
    bathroom = Room("Bathroom", "There is a door to the bedroom to the north.")
    guest_room = Room("Guest Room", "There is a door to the bedroom to the west.")
    hallway = Room("Hallway", "There is a door to the living room to the west, a door to the bedroom to the east, a door to the study to the north, and a door to the dining room to the south.")
    balcony = Room("Balcony", "There is a door to the hallway to the south.")
    study = Room("Study", "There is a door to the hallway to the south.")
    dining_room = Room("Dining Room", "There is a door to the hallway to the north.")

    # Set room connections
    living_room.north_room = kitchen
    living_room.east_room = hallway

    kitchen.south_room = living_room

    bedroom.west_room = hallway
    bedroom.south_room = bathroom
    bedroom.east_room = guest_room

    bathroom.north_room = bedroom

    guest_room.west_room = bedroom

    hallway.west_room = living_room
    hallway.east_room = bedroom
    hallway.north_room = study
    hallway.south_room = dining_room

    study.south_room = hallway

    dining_room.north_room = hallway

    balcony.north_room = hallway

    current_room = living_room
    enter_room(current_room)

    print("Welcome to David's Adventure! Try to escape out to the balcony and get down the rope.\n"
          "To change rooms, use cardinal direction inputs n, s, e, w.\nCan you escape?")

    while True:

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

if __name__ == "__main__":
    main()
