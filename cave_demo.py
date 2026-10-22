# cave_demo - Main game loop file

### Libraries: import random, a class we've used before
import random

### OWN modules: put reusable code in another file & import that file as a module
from cave_tools import CAVE_ROOMS, full_loot_table, die_roll, generate_loot_table, show_title, enter_room, loot_menu

# Generate loot table
loot_table = generate_loot_table(full_loot_table)

### Dictionary: key-value paired data
player = {
    "name" : "defaultName",
    "gold" : 0,
    ### List: stores gathered information - in this case, instances of loot_table
    "loot" : [],
    ### Set: store unique information instances
    "progress" : set()
}
# Game Loop:
# Game asks for player name at start
# Player goes through each room at random
# Player rolls the dice to determine the outcome of the room
# Player moves into the next room,
# and the game continues until the player exits or completes all rooms.

### Dictionary: how to access and update a value using its key
### Function: how to call a function & how to use a returned value in a program
### OWN modules: use a function from an imported module
player["name"] = show_title()


### WHILE loop: Uses a condition to control repetition
#.  This condition checks if it is still true that the player hasn't visited all rooms
#.  The loop breaks(without direct user breakage) when the player has visited all rooms, 
#   thus making player["progress"] no longer less than the length of CAVE_ROOMS 
while len(player["progress"]) < len(CAVE_ROOMS):
    # Game randomly selects a room from the CAVE_ROOMS tuple
    ### Tuple: access a value in a tuple
    ### Libraries: Used a taught function from the library
    #.  In this case, the function takes a random value between the two listed values
    #   (random.randint is inclusive of both low and high end bounds)
    random_room = random.randint(0, len(CAVE_ROOMS)-1)
    room = CAVE_ROOMS[random_room]
    while room in player["progress"]:
        room = random.choice(CAVE_ROOMS)
    enter_room(room)
    ### Sets: how to add a value to a Set
    player["progress"].add(room)
    # # Game rolls the dice to determine the outcome of the room
    # 1-6: Gold Found
    # 7: Combat Found, loses game
    # 8-12: Loot Found
    outcome = die_roll();
    if outcome <= 6:
        gold_found = random.randint(1, 10)
        print(f"You found {gold_found} gold!")
        player["gold"] += gold_found
    elif outcome == 7:
        print("You encountered a monster and lost the game!")
        player["progress"] = set()
        player["loot"] = []
        player["gold"] = 0
    else:
        loot_found = random.choice(loot_table)
        print(f"You found a {loot_found.name} worth {loot_found.value} gold!")
        player["loot"].append(loot_found)

    if not(player["progress"]):
        print("Do you want to try again? (y/n)")
    elif len(player["progress"]) < len(CAVE_ROOMS):
        print("Do you want to continue to the next room? (y/n)")
    else:
        print("Looks like you're done! Press enter to continue")
    continue_game = input("-> ")
    if continue_game.lower() != "y":
        break

if player["loot"]:
    # if the player has duplicates, the value of every other variant decreases by one
    loot_duplcate_check_set = set()
    for loot in len(player["loot"]):
        ### Lists: update an item in a list
        if loot.name in loot_duplcate_check_set:
            ### Public attributes - access and update an attribute through an object
            loot.value = loot.value // 2
        loot_duplcate_check_set.add(loot.name)

    see_loot = input("You have loot! Do you want to see your loot? (y/n) -> ")
    if see_loot.lower() == "y":
        while True:
            selected_loot = loot_menu(player["loot"])
            ### Public Method
            selected_loot.display_loot()
            see_more = input("Do you want to see more loot? (y/n) -> ")
            if see_more.lower() == "n":
                break
    if player["gold"]:
        print(f"You also have {player['gold']} gold!")
        for loot in player["loot"]:
            player["gold"] += loot.value
        print(f"With your loot, you have a net value of {player["gold"]}")
    else:
        for loot in player["loot"]:
            player["gold"] += loot.value
        print(f"With your loot, you have a net value of {player["gold"]}")
elif player["gold"] > 0:
    print(f"You have {player['gold']} gold!")
print("Thanks for playing,", player["name"], "!")