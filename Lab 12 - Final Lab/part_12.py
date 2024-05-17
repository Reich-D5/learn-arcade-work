import random

class Item:
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description

class Player:
    def __init__(self):
        self.inventory = []
        self.health = 100
        self.current_room = None

    def add_to_inventory(self, items):
        self.inventory.append(items)

    def display_inventory(self):
        if self.inventory:
            print("Inventory")
            for item in self.inventory:
                print("-", item.name)
        else:
            print("Inventory is empty")

    def has_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return True
        return False

    def has_lighter(self):
        return self.has_item("lighter")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.health = 100
        self.encounter_chance = 0.5  # Default encounter chance

    def move_randomly(self):
        possible_directions = []
        if self.current_room.north_room:
            possible_directions.append('north')
        if self.current_room.east_room:
            possible_directions.append('east')
        if self.current_room.south_room:
            possible_directions.append('south')
        if self.current_room.west_room:
            possible_directions.append('west')

        if possible_directions:
            direction = random.choice(possible_directions)
            if direction == 'north':
                self.current_room = self.current_room.north_room
            elif direction == 'east':
                self.current_room = self.current_room.east_room
            elif direction == 'south':
                self.current_room = self.current_room.south_room
            elif direction == 'west':
                self.current_room = self.current_room.west_room

    def detect_player(self, player):
        if self.current_room == player.current_room:
            print(f"The {self.name} spots you!")

class Room:
    def __init__(self, number='', name='', description='', north=None, east=None, south=None, west=None):
        self.number = number
        self.name = name
        self.description = description
        self.north_room = north
        self.east_room = east
        self.south_room = south
        self.west_room = west
        self.items = []

    def add_item(self, item):
        self.items.append(item)

def enter_room(room):
    print(f"You entered the {room.name.lower()}: {room.description}.")
    print()

def interact_with_enemy(player, enemy):
    print(f"You encountered the {enemy.name}!")

    while True:
        print(f"Your health: {player.health}")
        print(f"{enemy.name}'s health: {enemy.health}")

        action = input("What would you like to do? (attack/flee): ").strip().lower()

        if action == 'attack':
            damage_to_enemy = random.randint(10, 20)
            enemy.health -= damage_to_enemy
            print(f"You attack the {enemy.name} for {damage_to_enemy} damage!")
            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                break
            else:
                damage_to_player = random.randint(5, 15)
                player.health -= damage_to_player
                print(f"The {enemy.name} attacks you for {damage_to_player} damage!")
                if player.health <= 0:
                    print("Your health reaches zero. You are defeated!")
                    exit()

        elif action == 'flee':
            print("You attempt to flee...")
            flee_chance = random.random()
            if player.has_lighter():
                flee_chance += 0.2
                flee_chance = min(flee_chance, 1.0)
            if flee_chance < 0.5:
                print("You successfully flee from the enemy!")
                break
            else:
                print("You failed to flee! The enemy attacks you!")
                damage_to_player = random.randint(10, 20)
                player.health -= damage_to_player
                print(f"The {enemy.name} attacks you for {damage_to_player} damage!")
                if player.health <= 0:
                    print("Your health reaches zero. You are defeated!")
                    exit()
        else:
            print("Invalid action! Please choose 'attack' or 'flee'.")

class GameDifficulty:
    EASY = 1
    NORMAL = 2
    HARD = 3

def choose_difficulty():
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in [GameDifficulty.EASY, GameDifficulty.NORMAL, GameDifficulty.HARD]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def adjust_difficulty(difficulty_level, enemy):
    if difficulty_level == GameDifficulty.EASY:
        enemy.encounter_chance = 0.2
    elif difficulty_level == GameDifficulty.NORMAL:
        enemy.encounter_chance = 0.4
    elif difficulty_level == GameDifficulty.HARD:
        enemy.encounter_chance = 0.6

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

    rooms[0].description = ("The room has multiple couches and a very gothic feeling. In the middle of the room on the wall there is a fireplace with skulls above it\n"
                            "there is a door to the east and one to the north")
    rooms[1].description = ("The kitchen feels more modern than the rest of the house leaving you questioning what you are actually dealing with here\n"
                            "There is a door to the east and to the south")
    rooms[2].description = ("The bedroom has coffins all over and is decorated with human bones, it is lit by only candle light...\n"
                            "There is a door to the west and to the north")
    rooms[3].description = ("The bathroom is too large to be just a simple bathroom. There has to be something more to this...\n"
                            "There is a door to the east and to the west")
    rooms[4].description = ("The guest bedroom is filled with coffins and upside-down crosses...\n"
                            "There is a door to the south")
    rooms[5].description = ("The hallway stretches for miles with suits of armor and what seems to be werewolf pelts as rugs...\n"
                            "There is a door to the north, east, and south")
    rooms[6].description = ("You have reached the balcony, the door slams shut behind you and the rope seems to be cut.\n"
                            "You feel a presence above but before you could look up, everything goes black...")
    rooms[7].description = ("The study has bookshelves on every wall with books that seem to date hundreds of years back...\n"
                            "There is a door to the north, east, and south")
    rooms[8].description = ("The dining room has a long table with a black candelabra in the middle and only one large, throne-like seat at the head of the table\n"
                            "With the Romanian flag...\n"
                            "There is a door to the north and to the east")

    item1 = Item("lighter", "an old zippo lighter")
    item2 = Item("hammer", "Who would need a hammer in a place like this?")
    item3 = Item("candle", "hmmm... Did I pick up that lighter")
    item4 = Item("key", "a gold key encrusted with rubies and emeralds")
    item5 = Item("mysterious chalice", "a strange chalice with odd engravings on the side")
    item6 = Item("sword", "A knight's favorite weapon")

    rooms[1].add_item(item1)
    rooms[2].add_item(item3)
    rooms[4].add_item(item6)
    rooms[7].add_item(item5)
    rooms[5].add_item(item4)
    rooms[8].add_item(item2)

    rooms[0].north_room = rooms[1]
    rooms[0].east_room = rooms[5]

    rooms[1].east_room = rooms[7]
    rooms[1].south_room = rooms[0]

    rooms[7].west_room = rooms[1]
    rooms[7].south_room = rooms[5]
    rooms[7].north_room = rooms[4]

    rooms[5].south_room = rooms[8]
    rooms[5].north_room = rooms[7]
    rooms[5].west_room = rooms[0]

    rooms[8].east_room = rooms[3]
    rooms[8].north_room = rooms[5]

    rooms[3].east_room = rooms[2]
    rooms[3].west_room = rooms[8]

    rooms[2].north_room = rooms[6]
    rooms[2].west_room = rooms[3]

    rooms[4].south_room = rooms[7]

    player = Player()

    enemy = Enemy("unknown creature")
    enemy.current_room = rooms[random.randint(0, len(rooms) - 1)]
    player.current_room = rooms[0]

    print("Welcome to David's Adventure! Try to escape out to the balcony and get down the rope.\n"
          "To change rooms, use cardinal direction inputs n, s, e, w.\n"
          "You can use the command 'inventory' to check the items you pick up along the way\nCan you escape?")

    difficulty_level = choose_difficulty()
    adjust_difficulty(difficulty_level, enemy)

    print(f"You enter the abandoned mansion of your taker and find yourself standing in {player.current_room.name}: {player.current_room.description}")

    max_moves = 12
    moves_left = max_moves

    while moves_left >= 0:
        if enemy.current_room:
            if random.random() < enemy.encounter_chance:
                enemy.detect_player(player)

        if player.current_room == enemy.current_room:
            interact_with_enemy(player, enemy)

        user_input = input("\nWhat would you like to do? ").strip().lower()

        if user_input == 'inventory':
            player.display_inventory()
            continue

        if player.current_room.items:
            print("You see something else in the room:")
            for item in player.current_room.items:
                print("-", item.name)
            pick_up = input("Do you want to pick up this item? (y/n): ").strip().lower()
            if pick_up == 'y':
                for item in player.current_room.items:
                    player.add_to_inventory(item)
                print("Item(s) picked up!")
                player.current_room.items = []
            elif pick_up == 'n':
                print("Maybe later for this one...")
            else:
                print("Invalid input! Please enter y/n...")
            continue

        if user_input in ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']:
            if user_input == 'n' or user_input == 'north':
                if player.current_room.north_room:
                    player.current_room = player.current_room.north_room
                    enter_room(player.current_room)
                else:
                    print("You can't go that way.")
            elif user_input == 'e' or user_input == 'east':
                if player.current_room.east_room:
                    player.current_room = player.current_room.east_room
                    enter_room(player.current_room)
                else:
                    print("You can't go that way.")
            elif user_input == 's' or user_input == 'south':
                if player.current_room.south_room:
                    player.current_room = player.current_room.south_room
                    enter_room(player.current_room)
                else:
                    print("You can't go that way.")
            elif user_input == 'w' or user_input == 'west':
                if player.current_room.west_room:
                    player.current_room = player.current_room.west_room
                    enter_room(player.current_room)
                else:
                    print("You can't go that way.")

            moves_left -= 1

            if moves_left == 0:
                print("All the doors around you slam shut! The room starts to shake...\n"
                      "You fall to the ground and feel the evil take over...")
                print("GAME OVER!")
                break

            if player.current_room.number == 6:
                if player.has_item("key"):
                    print("Congratulations! You have escaped the mansion!")
                    break
                else:
                    print("You need the key to unlock the balcony door.")

        if player.current_room.number == 6:
            print("You have completed the game!")
            break

if __name__ == "__main__":
    main()