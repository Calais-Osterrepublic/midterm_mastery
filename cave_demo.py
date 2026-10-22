import random
import time
from cave_tools import Loot, CAVE_ROOMS, die_roll, generate_loot_table, show_title, enter_room, loot_menu

# Generate loot table
loot_table = generate_loot_table()

player = {
    "name" : "defaultName",
    "gold" : 0,
    "loot" : {},
    "progress" : {}
}
# Game Loop:
# Game asks for player name at start
# Player goes through each room at random
# Player rolls the dice to determine the outcome of the room
# Player moves into the next room,
# and the game continues until the player exits or completes all rooms.
player_name = show_title()
while len(player["progress"]) < len(CAVE_ROOMS):
    # Game randomly selects a room from the CAVE_ROOMS tuple
    room = random.choice(CAVE_ROOMS)
    enter_room(room)
    player["progress"].append(room)
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
        player["progress"] = {}
        player["loot"] = {}
        player["gold"] = 0
    else:
        loot_found = random.choice(loot_table)
        print(f"You found a {loot_found.name} worth {loot_found.value} gold!")
        player["loot"][loot_found.name] = loot_found.value
        
    if player["progress"] == {}:
        print("Do you want to try again? (y/n)")
    elif len(player["progress"]) < len(CAVE_ROOMS):
        print("Do you want to continue to the next room? (y/n)")
    continue_game = input("-> ")
    if continue_game.lower() == "n":
        break
# At the end of the game, 
# if the player has loot, the game will open up a smaller loop
# for displaying the loot the player has collected, 
# using the loot_menu function to display the loot 
# and allow the player to select an item to view its description.
# once you leave the loop, you will display the total gold earned and the game will end.
# If the player has no loot, the game will say there is no loot to display, and simply display the total gold earned.
# if the player has no loot or gold, the game will simply close.

if player["loot"]:
    see_loot = input("You have loot! Do you want to see your loot? (y/n) -> ")
    if see_loot.lower() == "y":
        while True:
            selected_loot = loot_menu(list(player["loot"]))
            loot_table[selected_loot].display_loot()
            see_more = input("Do you want to see more loot? (y/n) -> ")
            if see_more.lower() == "n":
                break
    player["gold"]
    print(f"You have {player['gold']} gold!")
elif player["gold"] > 0:
    print(f"You have {player['gold']} gold!")
print("Thanks for playing,", player_name, "!")