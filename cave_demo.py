import random
from cave_tools import Loot, CAVE_ROOMS, LOOT_TABLE, show_title, enter_room, loot_menu

loot_table = []

# Generate loot table

player = {
    "name" : "defaultName",
    "gold" : 0,
    "loot" : []
}
# Game Loop
