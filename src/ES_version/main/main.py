# Librerías
import functions_variables_constants as fvc

fvc.printLogo()
fvc.printSpace()
print("Hola, bienvenid@ al generador de mazos de Claim...")
fvc.printSpace()

fvc.deploySelectOptionsAndTakeInput()

while fvc.option != 4:

    if fvc.option == 1 and not fvc.globalListOfPairedFactions:
        print("Por favor, añade alguna expansión con facciones emparejadas para jugar...")
        fvc.printSpace()
    if fvc.option == 1 and len(fvc.globalListOfNonPairedFactions) < 3:
        print("Por favor, añade al menos 3 facciones no emparejadas para jugar...")
        fvc.printSpace()

    if (fvc.option == 1 and fvc.globalListOfPairedFactions
            and len(fvc.globalListOfNonPairedFactions) >= 3):
        fvc.takeNumberOfPlayersInput()

        if (fvc.numberOfPlayers in [3, 4]
                and len(fvc.globalListOfNonPairedFactions) < 5):
            print(
                f"Por favor, añade al menos 5 facciones no emparejadas para jugar con {fvc.numberOfPlayers} jugadores...")
            fvc.printSpace()

        else:
            fvc.chooseNumberOfFactions()
            fvc.generateRandomDeck()

    elif fvc.option == 2:
        fvc.delployAddDeleteOptionsAndTakeInput()

        while fvc.optionAddDelete != 5:

            if fvc.optionAddDelete == 1:
                fvc.addExpansionInput()

            elif fvc.optionAddDelete == 2:
                fvc.removeExpansionInput()

            elif fvc.optionAddDelete == 3:
                fvc.cleanPool()
                print("Ahora el grupo de mazos está vacío...")

            elif fvc.optionAddDelete == 4:
                fvc.addAllExpansionsToPool()

            fvc.printSpace()
            fvc.delployAddDeleteOptionsAndTakeInput()

    elif fvc.option == 3:
        fvc.showExpansionsAndFactions()

    fvc.deploySelectOptionsAndTakeInput()

fvc.goodByeMessage()