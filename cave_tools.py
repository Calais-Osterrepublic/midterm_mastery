# cave_tools - Data file

# Class - Object Blueprint
import random


class Loot:
    # Constructor - Function to instantiate a Loot object
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Public Method - Function within an object, defined within the class
    def display_loot(self):
        print("="*36)
        print("          Item Description")
        print("Name:", self.name)
        print("Value:", self.value)
        print("="*36)
        print()
        input("Press enter to continue ")

# Tuple - Values that aren't meant to change
CAVE_ROOMS = ("Dust Dunes","Steel Coils", "Mercurial Pools", "Rust Halls")
# LOOT_TABLE = (
#     Loot("Dust Dial", 15),
#     Loot("Coil Shard", 15),
#     Loot("Themostat", 15),
#     Loot("Rust Scepter", 15),
# )
LOOT_TABLE = ("Old Sun Dial", "Crystal Shard", "Gold Rod", "Cave Scepter")

# Functions 
def show_title():
    print("="*31)
    print("          Cave Seeker")
    print("="*31)
    print("Come seek the secrets of the Cave.")
    print()
    return input("Welcome! What is your name, Seeker? ->")

def enter_room(room_name):
    print("-" * 31)
    print(f"You step into {room_name}")

def loot_menu(loot_pile):
    print("="*29)
    print("          Loot Menu")
    print()
    for index, loot in enumerate(loot_pile):
        print(index, "-", loot.name, )
    print()
    user_input = input("Select an item (by number) ->")
    while int(user_input) > len(loot_pile) or int(user_input) < 0:
        print("Invalid Input: Not within length of list")
        user_input = input("Select an item (by number) ->")
    return loot_pile[int(user_input)]

def generate_loot_table(loot_names):
    loot_table = []
    for item in loot_names:
        loot_table.append(Loot(item, random.randint(1, 20)))
    return loot_table

def die_roll():
    return random.randint(1, 6) + random.randint(1, 6)