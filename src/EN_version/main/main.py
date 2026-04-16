# Libraries
# My own library with the functions, variables and constants
import functions_variables_constants

# Print the logo
functions_variables_constants.printLogo()

# Welcome message
functions_variables_constants.printSpace()
print("Hello, welcome to Claim deck generator...")
functions_variables_constants.printSpace()

# Print select options, and take the selected option from the user's input
functions_variables_constants.deploySelectOptionsAndTakeInput()

# While the user doesn't quit(4)
while functions_variables_constants.option != 4:

    # Get a random deck

    # Exceptional executions
    # You can't play without at least 2 paired factions
    if functions_variables_constants.option == 1 and not functions_variables_constants.globalListOfPairedFactions:
        print("Please add any expansion with paired factions to play...")
        functions_variables_constants.printSpace()
    # You can't play with less than 3 factions
    if functions_variables_constants.option == 1 and len(functions_variables_constants.globalListOfNonPairedFactions) < 3:
        print("Please add at least 3 non-paired factions to play...")
        functions_variables_constants.printSpace()

    # Normal execution
    if (functions_variables_constants.option == 1 and functions_variables_constants.globalListOfPairedFactions
            and len(functions_variables_constants.globalListOfNonPairedFactions) >= 3):
        # Ask the user how many players are going to play
        functions_variables_constants.takeNumberOfPlayersInput()

        # Number of players execution exception
        # If the number of players is 3 or 4 and the global non-paired list have less than 5 factions, you can't play
        if (functions_variables_constants.numberOfPlayers in [3, 4]
                and len(functions_variables_constants.globalListOfNonPairedFactions) < 5):
            print(f"Please add at least 5 non-paired factions to play with {functions_variables_constants.numberOfPlayers} players...")
            functions_variables_constants.printSpace()

        # Continue normal execution
        else:
            # Depending on how many players, you will play with 8 factions(3-4 players) or 5 factions(2 players)
            functions_variables_constants.chooseNumberOfFactions()
            # Choose decks randomly and shows to the user
            functions_variables_constants.generateRandomDeck()

    # Choose between add and remove and expansion
    elif functions_variables_constants.option == 2:
        # Organise de possible options
        # Print add/delete options, and take the add/delete option from the user's input
        functions_variables_constants.delployAddDeleteOptionsAndTakeInput()

        while functions_variables_constants.optionAddDelete != 5:

            # Add an expansion
            if functions_variables_constants.optionAddDelete == 1:
                functions_variables_constants.addExpansionInput()

            # Delete an expansion
            elif functions_variables_constants.optionAddDelete == 2:
                functions_variables_constants.removeExpansionInput()

            # Clean all the expansions selected
            elif functions_variables_constants.optionAddDelete == 3:
                functions_variables_constants.cleanPool()
                print("Now the deck pool it's empty...")

            # Add all the available expansions
            elif functions_variables_constants.optionAddDelete == 4:
                functions_variables_constants.addAllExpansionsToPool()

            # Repeat the add/delete options
            functions_variables_constants.printSpace()
            # Print add/delete options, and take the add/delete option from the user's input
            functions_variables_constants.delployAddDeleteOptionsAndTakeInput()

    # Show the actual expansions added to your deck
    elif functions_variables_constants.option == 3:
        functions_variables_constants.showExpansionsAndFactions()

    # Repeat the general options
    # Print select options, and take the selected option from the user's input
    functions_variables_constants.deploySelectOptionsAndTakeInput()

# End the program
functions_variables_constants.goodByeMessage()



 