# Claims and expansions factions
# Claim I
pairedFactionsClaimI = "Goblins and Knights"
nonPairedFactionsClaimI = ["Doppelgangers", "Dwarves", "Undead"]

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
nonPairedFactionsMagic = ["Druids", "Shape shifters", "Wizards"]

# Fire
pairedFactionsFire = "EMPTY"
nonPairedFactionsFire = ["Demons", "Fire elementals", "Poisoners", "Tricksters"]

# To add -> Alliances, Sky, Sun and Sea

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
    print("2. Organise your actuals expansions\n")
    print("3. Exit\n")

def printAddDeleteOptions():
    print("Organisation options: ")
    print("1. Add an expansion\n")
    print("2. Remove an expansion\n")
    print("3. Back\n")

def addAnExpansion(inputAdd):
    match inputAdd:
        case "Claim I":
            globalListOfPairedFactions.append(pairedFactionsClaimI)
            globalListOfNonPairedFactions.append(nonPairedFactionsClaimI)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Claim II":
            globalListOfPairedFactions.append(pairedFactionsClaimII)
            globalListOfNonPairedFactions.append(nonPairedFactionsClaimII)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Claim V":
            globalListOfPairedFactions.append(pairedFactionsClaimV)
            globalListOfNonPairedFactions.append(nonPairedFactionsClaimV)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Terror":
            globalListOfPairedFactions.append(pairedFactionsTerror)
            globalListOfNonPairedFactions.append(nonPairedFactionsTerror)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Ice":
            globalListOfPairedFactions.append(pairedFactionsIce)
            globalListOfNonPairedFactions.append(nonPairedFactionsIce)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Maps":
            globalListOfPairedFactions.append(pairedFactionsMaps)
            globalListOfNonPairedFactions.append(nonPairedFactionsMaps)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Mercenaries":
            globalListOfPairedFactions.append(pairedFactionsMercenaries)
            globalListOfNonPairedFactions.append(nonPairedFactionsMercenaries)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Magic":
            globalListOfPairedFactions.append(pairedFactionsMagic)
            globalListOfNonPairedFactions.append(nonPairedFactionsMagic)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        # Fire
        case _:
            globalListOfPairedFactions.append(pairedFactionsFire)
            globalListOfNonPairedFactions.append(nonPairedFactionsFire)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)

def removeAnExpansion(inputDelete, globalListOfPairedFactions=globalListOfPairedFactions,
                      globalListOfNonPairedFactions=globalListOfNonPairedFactions):
    match inputDelete:
        case "Claim I":
            # If the elements from our global list are not in the paired factions of Claim I, then we add it to our global list
            # we are removing from the global lists the factions from Claim I
            # Do the substraction between these 2 sets
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsClaimI]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsClaimI]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Claim II":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsClaimII]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsClaimII]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Claim V":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsClaimV]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsClaimV]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Terror":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsTerror]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsTerror]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Ice":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsIce]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsIce]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Maps":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsMaps]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsMaps]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Mercenaries":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsMercenaries]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsMercenaries]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Magic":
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsMagic]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsMagic]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        # Fire
        case _:
            globalListOfPairedFactions = [x for x in globalListOfPairedFactions if x not in pairedFactionsFire]
            globalListOfNonPairedFactions = [x for x in globalListOfNonPairedFactions if x not in nonPairedFactionsFire]

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)

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

# Welcome and show the options
printSpace()
print("Hello, welcome to Claim deck generator...")
printSpace()
printGeneralOptions()

# Get the option from the input
option = int(input("Select an option: "))
printSpace()
while option not in [1, 2, 3]:
    option = int(input("Wrong option, please enter 1,2 or 3: "))

# While the user doesn't quit
while option != 3:

    # Get a random deck
    if option == 1:
        numberOfPlayers = int(input("How many players are going to play? "))

        # Test if the user's input is available
        while numberOfPlayers not in [2, 3, 4]:
            numberOfPlayers = int(input("Wrong number of players, please enter 2,3 or 4: "))

        # Depending on how many players, you will play with 8 factions(3-4 players) or 5 factions(2 players)
        numbersOfFactions = 3

        if numberOfPlayers == 2:
            print(
                "You will have to prepare a deck with 2 paired faction(for example goblins and knights) and add 3 not paired factions")
        else:
            print(
                "You will have to prepare a deck with 2 paired faction(for example goblins and knights) and add 5 not paired factions")
            numbersOfFactions = 5
        # TO COMPLETE

    elif option == 2:
        # Organise de possible options
        printAddDeleteOptions()
        optionAddDelete = int(input("Select an option: "))
        printSpace()

        # Test if the user's input is available
        while optionAddDelete not in [1, 2, 3]:
            optionAddDelete = int(input("Wrong option, please enter 1,2 or 3: "))

        while optionAddDelete != 3:

            # Add an expansion
            if optionAddDelete == 1:

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
                    print(globalListOfPairedFactions)
                    print(globalListOfNonPairedFactions)

            # Delete an expansion
            elif optionAddDelete == 2:

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

            # Repeat the add/delete options
            printSpace()
            printAddDeleteOptions()
            optionAddDelete = int(input("Select an option: "))

        # Test if the user's input is available
        while optionAddDelete not in [1, 2, 3]:
            optionAddDelete = int(input("Wrong option, please enter 1,2 or 3: "))

    # Repeat the options
    printSpace()
    printGeneralOptions()
    option = int(input("Select an option: "))

    # Test if the user's input is available
    while option not in [1, 2, 3]:
        option = int(input("Wrong option, please enter 1,2 or 3: "))

# End the program
print("Good bye, thanks for using the randomizer <3, see you :)")




