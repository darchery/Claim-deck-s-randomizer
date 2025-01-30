# Libraries
import random

# Claims and expansions factions
# Claim I
pairedFactionsClaimI = "Goblins and Knights"
nonPairedFactionsClaimI = ["Doppelgangers", "Dwarves", "Undeads"]

# Claim II
pairedFactionsClaimII = "Giants and Gnomes"
nonPairedFactionsClaimII = ["Dragons", "Seers", "Trolls"]

# Claim V Anniversary exclusive factions
pairedFactionsClaimV = "Royalty and Peasants"
nonPairedFactionsClaimV = ["Automatons", "Bards", "Racoons", "Vikings", "Griffins"]

# Expansions

# Terror
# pairedFactionsTerror = "EMPTY"
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
# pairedFactionsMagic = "EMPTY"
nonPairedFactionsMagic = ["Druids", "Shape shifters", "Wizards"]

# Fire
# pairedFactionsFire = "EMPTY"
nonPairedFactionsFire = ["Demons", "Fire elementals", "Poisoners", "Tricksters"]

# To add -> Alliances, Sky, Sun and Sea

# Constants and global variables
SELECT_OPTION_MESSAGE = "Select an option: "
WRONG_OPTION_MESSAGE = "Wrong option, please enter 1,2 or 3: "

# List with the factions
globalListOfPairedFactions = []
globalListOfNonPairedFactions = []

# List to control the added expansions
expansionsNotAdded = ["Claim I", "Claim II", "Claim V", "Terror", "Ice", "Maps", "Mercenaries", "Magic", "Fire"]
expansionsAdded = []

# Definition of methods
def printSpace():
    print("\n")

def printGeneralOptions():
    print("Available menu options: ")
    print("1. Generate a random deck\n")
    print("2. Organise your actual expansions\n")
    print("3. Show your selected expansions\n")
    print("4. Exit\n")

def printAddDeleteOptions():
    print("Organisation options: ")
    print("1. Add an expansion\n")
    print("2. Remove an expansion\n")
    print("3. Clean all the expansions selected\n")
    print("4. Add all the available expansions\n")
    print("5. Back\n")

def showExpansionsAndFactions():
    global expansion
    if not expansionsAdded:
        print("You didn't select any expansion, please add one...")
    else:
        print("Actual added expansions:")
        for expansion in expansionsAdded:
            print(f"- {expansion}")
        print("Paired factions: ")
        for index, faction in enumerate(globalListOfPairedFactions, start=1):
            print(f" {index}. {faction}")
        print("Non-paired factions: ")
        for index, faction in enumerate(globalListOfNonPairedFactions, start=1):
            print(f" {index}. {faction}")

def cleanPool():
    global globalListOfPairedFactions, globalListOfNonPairedFactions, expansionsNotAdded, expansionsAdded
    # Set to empty the global lists
    globalListOfPairedFactions = []
    globalListOfNonPairedFactions = []
    # Reset the expansions lists, refill the not added list and set to empty de added list
    expansionsNotAdded = ["Claim I", "Claim II", "Claim V", "Terror", "Ice", "Maps", "Mercenaries", "Magic", "Fire"]
    expansionsAdded = []

def addAllExpansionsToPool():
    global expansionsNotAdded, expansionsAdded
    # Clean the previous content
    cleanPool()
    # Refill both lists
    addEveryFaction()
    # Reset the expansions lists, refill the not added list and set to empty de added list
    expansionsNotAdded = []
    expansionsAdded = ["Claim I", "Claim II", "Claim V", "Terror", "Ice", "Maps", "Mercenaries", "Magic", "Fire"]
    print("All expansions were added...")


def addEveryFaction():
    addAnExpansion("Claim I")
    addAnExpansion("Claim II")
    addAnExpansion("Claim V")
    addAnExpansion("Terror")
    addAnExpansion("Ice")
    addAnExpansion("Mercenaries")
    addAnExpansion("Maps")
    addAnExpansion("Magic")
    addAnExpansion("Fire")

def printLogo():
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

def addAnExpansion(inputAdd):
    match inputAdd:
        case "Claim I":
            globalListOfPairedFactions.append(pairedFactionsClaimI)
            # Can use extend
            # globalListOfNonPairedFactions.extend(nonPairedFactionsClaimI)
            # But in this case we are using for to have more control
            for faction in nonPairedFactionsClaimI:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Claim II":
            globalListOfPairedFactions.append(pairedFactionsClaimII)
            for faction in nonPairedFactionsClaimII:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Claim V":
            globalListOfPairedFactions.append(pairedFactionsClaimV)
            for faction in nonPairedFactionsClaimV:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Terror":
            # Terror doesn't have paired factions to add
            #globalListOfPairedFactions.append(pairedFactionsTerror)
            for faction in nonPairedFactionsTerror:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Ice":
            globalListOfPairedFactions.append(pairedFactionsIce)
            for faction in nonPairedFactionsIce:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Maps":
            globalListOfPairedFactions.append(pairedFactionsMaps)
            # Maps only have on non-paired faction
            globalListOfNonPairedFactions.append(nonPairedFactionsMaps)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Mercenaries":
            globalListOfPairedFactions.append(pairedFactionsMercenaries)
            # Mercenaries only have on non-paired faction
            globalListOfNonPairedFactions.append(nonPairedFactionsMercenaries)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Magic":
            # Magic doesn't have paired factions to add
            #globalListOfPairedFactions.append(pairedFactionsMagic)
            for faction in nonPairedFactionsMagic:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        # Fire
        case _:
            # Fire doesn't have paired factions to add
            #globalListOfPairedFactions.append(pairedFactionsFire)
            for faction in nonPairedFactionsFire:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)

def removeAnExpansion(inputDelete):
    global globalListOfPairedFactions, globalListOfNonPairedFactions
    match inputDelete:
        case "Claim I":
            # Remove from paired global list
            globalListOfPairedFactions.remove(pairedFactionsClaimI)
            # Remove from non-paired global list
            # For every non-paried faction from Claim I
            for faction in nonPairedFactionsClaimI:
                # If it's in on the nonPairedFactions global list, then remove it
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Claim II":
            globalListOfPairedFactions.remove(pairedFactionsClaimII)
            for faction in nonPairedFactionsClaimII:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Claim V":
            globalListOfPairedFactions.remove(pairedFactionsClaimV)
            for faction in nonPairedFactionsClaimV:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Terror":
            # Terror doesn't have paired factions to remove
            #globalListOfPairedFactions.remove(pairedFactionsTerror)
            for faction in nonPairedFactionsTerror:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Ice":
            globalListOfPairedFactions.remove(pairedFactionsIce)
            for faction in nonPairedFactionsIce:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Maps":
            globalListOfPairedFactions.remove(pairedFactionsMaps)
            for faction in nonPairedFactionsMaps:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Mercenaries":
            globalListOfPairedFactions.remove(pairedFactionsMercenaries)
            for faction in nonPairedFactionsMercenaries:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Magic":
            # Maic doesn't have paired factions to delete
            #globalListOfPairedFactions.remove(pairedFactionsMagic)
            for faction in nonPairedFactionsMagic:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        # Fire
        case _:
            # Fire doesn't have paired factions
            #globalListOfPairedFactions.remove(pairedFactionsFire)
            for faction in nonPairedFactionsFire:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)

# Print the logo
printLogo()

# Welcome and show the options
printSpace()
print("Hello, welcome to Claim deck generator...")
printSpace()
printGeneralOptions()

# Get the option from the input
option = int(input(SELECT_OPTION_MESSAGE))

# Test if the user's input is available
while option not in [1, 2, 3, 4]:
    option = int(input(WRONG_OPTION_MESSAGE))

# While the user doesn't quit(4)
while option != 4:

    # Get a random deck
    if option == 1 and not globalListOfPairedFactions:
        print("Please add any expansion with paired factions to play...")
    if option == 1 and globalListOfPairedFactions:
        printSpace()
        numberOfPlayers = int(input("How many players are going to play? "))

        # Test if the user's input is available
        while numberOfPlayers not in [2, 3, 4]:
            numberOfPlayers = int(input("Wrong number of players, please enter 2,3 or 4: "))

        # Depending on how many players, you will play with 8 factions(3-4 players) or 5 factions(2 players)
        numbersOfFactions = 3

        if numberOfPlayers == 2:
            print(
                "You will have to prepare a deck with 2 paired factions(for example goblins and knights) and add 3 not paired factions")
        else:
            print(
                "You will have to prepare a deck with 2 paired factions(for example goblins and knights) and add 5 not paired factions")
            numbersOfFactions = 5

        # We are going to select 2 paired factions
        random.shuffle(globalListOfPairedFactions)
        pairedGenerated = random.choice(globalListOfPairedFactions)

        # Then we are going to select 3 or 5 non-paired factions to build our deck
        random.shuffle(globalListOfNonPairedFactions)
        nonPairedGenerated = random.sample(globalListOfNonPairedFactions, numbersOfFactions)

        print(f"Your randomly generated deck for {numberOfPlayers} players is composed by: ")
        print(f"- {pairedGenerated}")
        if len(nonPairedGenerated) > 1:
            print("- " + ", ".join(nonPairedGenerated[:-1]) + " and " + nonPairedGenerated[-1])
        else:
            print(nonPairedGenerated[0])

    # Choose between add and remove and expansion
    elif option == 2:
        # Organise de possible options
        printSpace()
        printAddDeleteOptions()
        optionAddDelete = int(input(SELECT_OPTION_MESSAGE))

        # Test if the user's input is available
        while optionAddDelete not in [1, 2, 3, 4, 5]:
            optionAddDelete = int(input(WRONG_OPTION_MESSAGE))

        while optionAddDelete != 5:

            # Add an expansion
            if optionAddDelete == 1:

                printSpace()
                # The List.isEmpty of python
                if not expansionsNotAdded:
                    print("All expansions were added")
                else:
                    print("Available expansions: ")
                    for expansion in expansionsNotAdded:
                        print(f"- {expansion}")
                    inputAdd = input("Type the name: ")

                    while inputAdd not in expansionsNotAdded:
                        inputAdd = input("Wrong input, type an available expansion: ")

                    # Add the expansion
                    addAnExpansion(inputAdd)
                    print(f" {inputAdd} was succesfully added...")

            # Delete an expansion
            elif optionAddDelete == 2:

                printSpace()
                # The List.isEmpty of python
                if not expansionsAdded:
                    print("You didn't added any faction")
                else:
                    print("Actual expansions: ")
                    for expansion in expansionsAdded:
                        print(f"- {expansion}")
                    inputDelete = input("Type the name: ")

                    while inputDelete not in expansionsAdded:
                        inputDelete = input("Wrong input, type an added expansion: ")

                    # Remove the expansion
                    removeAnExpansion(inputDelete)
                    print(f" {inputDelete} was succesfully removed...")

            # Clean all the expansions selected
            elif optionAddDelete == 3:
                cleanPool()
                print("Now the deck pool it's empty...")

            # Add all the available expansions
            elif optionAddDelete == 4:
                addAllExpansionsToPool()

            # Repeat the add/delete options
            printSpace()
            printAddDeleteOptions()
            optionAddDelete = int(input(SELECT_OPTION_MESSAGE))

        # Test if the user's input is available
        while optionAddDelete not in [1, 2, 3, 4, 5]:
            optionAddDelete = int(input(WRONG_OPTION_MESSAGE))

    # Show the actual expansions added to your deck
    elif option == 3:
        showExpansionsAndFactions()

    # Repeat the options
    printSpace()
    printGeneralOptions()
    option = int(input(SELECT_OPTION_MESSAGE))

    # Test if the user's input is available
    while option not in [1, 2, 3, 4]:
        option = int(input(WRONG_OPTION_MESSAGE))

# End the program
print("Good bye, thanks for using the randomizer <3, see you :)")




