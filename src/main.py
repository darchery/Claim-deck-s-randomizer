# Definition of methods
def printSpace():
    print("\n")

# Claims and expansions factions

# Claim I
pairedFactionsClaimI = "Goblins and Knights"
nonPairedFactionsClaimI = ["Doopelgangers", "Dwarves", "Undead"]

# Claim II
pairedFactionsClaimII = "Giants and Gnomes"
nonPairedFactionsClaimII = ["Dragons", "Seers", "Trolls"]

# Claim V Anniversary exclusive factions
pairedFactionsClaimV = "Royalty and Peasants"
nonPairedFactionsClaimV = ["Automatons", "Bards", "Racoons", "Vikings", "Griffins"]

# Expansions

# Terror
pairedFactionsTerror = "EMPTY"
nonPairedFactionsTerror = ["Shadows", "Vampires", "Werewolves", "Zombies"]

# Ice
pairedFactionsIce = "Ice Queen and King"
nonPairedFactionsIce = ["Yetis", "Ice Beasts"]

# Maps
pairedFactionsMaps = "Basilisks and Unicorns"
nonPairedFactionsMaps = "Phoenixes"

# Mercenaries
pairedFactionsMercenaries = "Orcs, Elves and Elves and Orcs"
nonPairedFactionsMercenaries = "Cyclops"

# Magic
pairedFactionsMagic = "EMPTY"
nonPairedFactionsMagic = ["Druids", "Shapeshifters", "Wizards"]

# Fire
pairedFactionsFire = "EMPTY"
nonPairedFactionsFire = ["Demons", "Fire elementals", "Poisoners", "Tricksters"]

# To add -> Alliances, Sky, Sun and Sea

# Print the title
print(r""" 
   _____   _                   _____   __  __        _____    ______    _____   _  __
  / ____| | |          /\     |_   _| |  \/  |      |  __ \  |  ____|  / ____| | |/ /
 | |      | |         /  \      | |   | \  / |      | |  | | | |__    | |      | ' / 
 | |      | |        / /\ \     | |   | |\/| |      | |  | | |  __|   | |      |  <  
 | |____  | |____   / ____ \   _| |_  | |  | |      | |__| | | |____  | |____  | . \ 
  \_____| |______| /_/    \_\ |_____| |_|  |_|      |_____/  |______|  \_____| |_|\_\ 
  
   _____   ______   _   _   ______   _____               _______    ____    _____  
  / ____| |  ____| | \ | | |  ____| |  __ \      /\     |__   __|  / __ \  |  __ \ 
 | |  __  | |__    |  \| | | |__    | |__) |    /  \       | |    | |  | | | |__) |
 | | |_ | |  __|   | . ` | |  __|   |  _  /    / /\ \      | |    | |  | | |  _  / 
 | |__| | | |____  | |\  | | |____  | | \ \   / ____ \     | |    | |__| | | | \ \ 
  \_____| |______| |_| \_| |______| |_|  \_\ /_/    \_\    |_|     \____/  |_|  \_\
  """)

printSpace()

print("Hello, welcome to Claim deck generator...")

printSpace()

availableNumberOfPlayers = [2,3,4]

numberOfPlayers = int(input("How many players are going to play? "))

while numberOfPlayers not in availableNumberOfPlayers:
    numberOfPlayers = int(input("Wrong number of players, please enter 2,3 or 4: "))

# Depending on how many players, you will play with 8 factions(3-4 players) or 5 factions(2 players)
typeOfGame = 3

if numberOfPlayers == 2:
    print("You will have to prepare a deck with 2 paired faction(for example goblins and knights) and add 3 not paired factions")
else:
    print(
        "You will have to prepare a deck with 2 paired faction(for example goblins and knights) and add 5 not paired factions")
    typeOfGame = 5

# List with the factions
globalListOfPairedFactions = []
globalListOfNonPairedFactions = []



