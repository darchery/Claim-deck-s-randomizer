# Librerías
import random
import time

# Claims and expansions factions
# Claim I
pairedFactionsClaimI = "Goblins y Caballeros"
nonPairedFactionsClaimI = ["Doppelgängers", "Enanos", "No muertos"]

# Claim II
pairedFactionsClaimII = "Gigantes y Gnomos"
nonPairedFactionsClaimII = ["Dragones", "Videntes", "Trolls"]

# Claim V (Facciones exclusivas del V aniversario)
pairedFactionsClaimV = "Realeza y Campesinos"
nonPairedFactionsClaimV = ["Automátas", "Bardos", "Mapaches", "Vikingos", "Grifos"]


# Expansiones
# Terror
# pairedFactionsTerror = "EMPTY"
nonPairedFactionsFear = ["Sombras", "Vampiros", "Hombres Lobo", "Zombis"]

# Hielo
pairedFactionsFrost = "Reina de Hielo y Rey de Hielo"
nonPairedFactionsFrost = ["Yetis", "Bestias de Hielo"]

# Mapas
pairedFactionsMaps = "Basiliscos y Unicornios"
nonPairedFactionsMaps = "Fénixes"

# Mercenarios
pairedFactionsMercenaries = "Orcos, Elfos y Elfos y Orcos"
nonPairedFactionsMercenaries = "Cíclopes"

# Magia
# pairedFactionsMagic = "EMPTY"
nonPairedFactionsMagic = ["Druidas", "Cambiapieles", "Magos"]

# Fuego
# pairedFactionsFire = "EMPTY"
nonPairedFactionsFire = ["Demonios", "Elementales de Fuego", "Envenenadores", "Tramposos"]

# Por agregar -> Alianzas, Cielo, Sol y Mar

# Constantes y variables globales
SELECT_OPTION_MESSAGE = "Selecciona una opción: "
WRONG_OPTION_MESSAGE = "Opción incorrecta, por favor ingresa 1, 2, 3 o 4: "
FIRE = "Fuego"
MAGIC = "Magia"
MERCENARIES = "Mercenarios"
MAPS = "Mapas"
FROST = "Hielo"
FEAR = "Terror"
CLAIM_V = "Claim V"
CLAIM_II = "Claim II"
CLAIM_I = "Claim I"

# Listas para controlar las expansiones añadidas
globalListOfPairedFactions = []
globalListOfNonPairedFactions = []

# List to control the added expansions
expansionsNotAdded = [CLAIM_I, CLAIM_II, CLAIM_V, FEAR, FROST, MAPS, MERCENARIES, MAGIC, FIRE]
expansionsAdded = []

# Definition of methods
def printSpace():
    print("\n")

def printGeneralOptions():
    print("Opciones de menú disponibles: ")
    print("1. Generar un mazo aleatorio\n")
    print("2. Organizar tus expansiones actuales\n")
    print("3. Mostrar tus expansiones seleccionadas\n")
    print("4. Salir\n")

def printAddDeleteOptions():
    print("Opciones de organización: ")
    print("1. Agregar una expansión\n")
    print("2. Eliminar una expansión\n")
    print("3. Limpiar todas las expansiones seleccionadas\n")
    print("4. Agregar todas las expansiones disponibles\n")
    print("5. Volver\n")

def showExpansionsAndFactions():
    global expansion
    if not expansionsAdded:
        print("No has seleccionado ninguna expansión, por favor agrega una...")
    else:
        print("Expansiones agregadas actualmente:")
        for expansion in expansionsAdded:
            print(f"- {expansion}")
        print("Facciones emparejadas: ")
        for index, faction in enumerate(globalListOfPairedFactions, start=1):
            print(f" {index}. {faction}")
        print("Facciones no emparejadas: ")
        for index, faction in enumerate(globalListOfNonPairedFactions, start=1):
            print(f" {index}. {faction}")
    printSpace()

def cleanPool():
    global globalListOfPairedFactions, globalListOfNonPairedFactions, expansionsNotAdded, expansionsAdded
    # Vaciar las listas globales
    globalListOfPairedFactions = []
    globalListOfNonPairedFactions = []
    # Reiniciar las listas de expansiones, rellenar la lista de expansiones no agregadas y vaciar la lista de expansiones agregadas
    expansionsNotAdded = [CLAIM_I, CLAIM_II, CLAIM_V, FEAR, FROST, MAPS, MERCENARIES, MAGIC, FIRE]
    expansionsAdded = []

def addAllExpansionsToPool():
    global expansionsNotAdded, expansionsAdded
    # Limpiar el contenido anterior
    cleanPool()
    # Volver a llenar ambas listas
    addEveryFaction()
    # Resetear las listas de expansiones, llenar de nuevo la lista de expansiones no agregadas y vaciar la de expansiones agregadas
    expansionsNotAdded = []
    expansionsAdded = [CLAIM_I, CLAIM_II, CLAIM_V, FEAR, FROST, MAPS, MERCENARIES, MAGIC, FIRE]
    print("Todas las expansiones fueron agregadas...")


def addEveryFaction():
    addAnExpansion(CLAIM_I)
    addAnExpansion(CLAIM_II)
    addAnExpansion(CLAIM_V)
    addAnExpansion(FEAR)
    addAnExpansion(FROST)
    addAnExpansion(MERCENARIES)
    addAnExpansion(MAPS)
    addAnExpansion(MAGIC)
    addAnExpansion(FIRE)

def deploySelectOptionsAndTakeInput():
    global option, wrong
    printGeneralOptions()
    option = input(SELECT_OPTION_MESSAGE)
    printSpace()
    # Test if the user's input is available
    wrong = False
    while option not in ["1", "2", "3", "4"]:
        option = input(WRONG_OPTION_MESSAGE)
        wrong = True
    # If the option was valid, then convert it to int
    option = int(option)
    if wrong:
        printSpace()

def delployAddDeleteOptionsAndTakeInput():
    global optionAddDelete, wrong
    printAddDeleteOptions()
    optionAddDelete = input(SELECT_OPTION_MESSAGE)
    printSpace()
    # Test if the user's input is available
    wrong = False
    while optionAddDelete not in ["1", "2", "3", "4", "5"]:
        optionAddDelete = input("Opción incorrecta, por favor ingresa 1, 2, 3, 4 o 5: ")
        wrong = True
    # If the input was valid, then convert it to int
    optionAddDelete = int(optionAddDelete)
    if wrong:
        printSpace()

def takeNumberOfPlayersInput():
    global numberOfPlayers, wrong
    numberOfPlayers = input("¿Cuántos jugadores van a jugar? ")
    printSpace()
    # Comprobar si la entrada del usuario es válida
    wrong = False
    while numberOfPlayers not in ["2", "3", "4"]:
        numberOfPlayers = input("Número de jugadores incorrecto, por favor ingresa 2, 3 o 4: ")
        wrong = True
    # Si el número de jugadores fue válido, convertirlo a int
    numberOfPlayers = int(numberOfPlayers)
    if wrong:
        printSpace()

def generateRandomDeck():
    # Vamos a seleccionar 2 facciones emparejadas
    random.shuffle(globalListOfPairedFactions)
    pairedGenerated = random.choice(globalListOfPairedFactions)
    # Luego seleccionamos 3 o 5 facciones no emparejadas para construir nuestro mazo    random.shuffle(globalListOfNonPairedFactions)
    nonPairedGenerated = random.sample(globalListOfNonPairedFactions, numbersOfFactions)
    print(f"Tu mazo generado aleatoriamente para {numberOfPlayers} jugadores está compuesto por: ")
    print(f"- {pairedGenerated}")
    if len(nonPairedGenerated) > 1:
        print("- " + ", ".join(nonPairedGenerated[:-1]) + " y " + nonPairedGenerated[-1])
    else:
        print(nonPairedGenerated[0])
    printSpace()

def addExpansionInput():
    global expansion, wrong
    # Comprobando si la lista está vacía
    if not expansionsNotAdded:
        print("Todas las expansiones ya han sido agregadas.")
    else:
        print("Expansiones disponibles: ")
        for expansion in expansionsNotAdded:
            print(f"- {expansion}")
        inputAdd = input("Escribe el nombre de la expansión: ")
        printSpace()

        wrong = False
        while inputAdd not in expansionsNotAdded:
            inputAdd = input("Entrada incorrecta, escribe una expansión disponible: ")
            wrong = True
        if wrong:
            printSpace()

        # Agregar la expansión
        addAnExpansion(inputAdd)
        print(f"{inputAdd} se ha agregado correctamente...")


def removeExpansionInput():
    global expansion
    # The List.isEmpty of python
    if not expansionsAdded:
        print("No has agregado ninguna expansión aún.")
    else:
        print("Expansiones actuales: ")
        for expansion in expansionsAdded:
            print(f"- {expansion}")
        inputDelete = input("Escribe el nombre de la expansión: ")
        printSpace()

        while inputDelete not in expansionsAdded:
            inputDelete = input("Entrada incorrecta, escribe una expansión agregada: ")

        # Eliminar la expansión
        removeAnExpansion(inputDelete)
        print(f"{inputDelete} se ha eliminado correctamente...")

def chooseNumberOfFactions():
    global numbersOfFactions
    numbersOfFactions = 3
    if numberOfPlayers == 2:
        print(
            "Tendrás que preparar un mazo con 2 facciones emparejadas y agregar 3 facciones no emparejadas, en total 5 facciones.")
    else:
        print(
            "Tendrás que preparar un mazo con 2 facciones emparejadas y agregar 5 facciones no emparejadas, en total 7 facciones.")
        numbersOfFactions = 5

def goodByeMessage():
    print("Adiós, gracias por usar el generador de mazos <3, ¡nos vemos! :)")
    # Esperar 3 segundos para mostrar el mensaje
    time.sleep(3)

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
            # Se puede usar extend
            # globalListOfNonPairedFactions.extend(nonPairedFactionsClaimI)
            # Pero en este caso estamos usando un bucle para tener más control
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
            # Terror no tiene facciones emparejadas para agregar
            #globalListOfPairedFactions.append(pairedFactionsFear)
            for faction in nonPairedFactionsFear:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Hielo":
            globalListOfPairedFactions.append(pairedFactionsFrost)
            for faction in nonPairedFactionsFrost:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Mapas":
            globalListOfPairedFactions.append(pairedFactionsMaps)
            # Mapas solo tiene una facción no emparejada
            globalListOfNonPairedFactions.append(nonPairedFactionsMaps)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Mercenarios":
            globalListOfPairedFactions.append(pairedFactionsMercenaries)
            # Mercenarios solo tiene una facción no emparejada
            globalListOfNonPairedFactions.append(nonPairedFactionsMercenaries)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        case "Magia":
            # Magic no tiene facciones emparejadas para agregar
            #globalListOfPairedFactions.append(pairedFactionsMagic)
            for faction in nonPairedFactionsMagic:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)
        # Fuego
        case _:
            # Fuego no tiene facciones emparejadas para agregar
            #globalListOfPairedFactions.append(pairedFactionsFire)
            for faction in nonPairedFactionsFire:
                globalListOfNonPairedFactions.append(faction)

            expansionsNotAdded.remove(inputAdd)
            expansionsAdded.append(inputAdd)

def removeAnExpansion(inputDelete):
    global globalListOfPairedFactions, globalListOfNonPairedFactions
    match inputDelete:
        case "Claim I":
            # Eliminar de la lista emparejada global
            globalListOfPairedFactions.remove(pairedFactionsClaimI)
            # Eliminar de la lista no emparejada global
            # Para cada facción no emparejada de Claim I
            for faction in nonPairedFactionsClaimI:
                # Si está en la lista global de nonPairedFactions, eliminarla
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
            # Terror no tiene facciones emparejadas para eliminar
            #globalListOfPairedFactions.remove(pairedFactionsFear)
            for faction in nonPairedFactionsFear:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Hielo":
            globalListOfPairedFactions.remove(pairedFactionsFrost)
            for faction in nonPairedFactionsFrost:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Mapas":
            globalListOfPairedFactions.remove(pairedFactionsMaps)
            for faction in nonPairedFactionsMaps:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Mercenarios":
            globalListOfPairedFactions.remove(pairedFactionsMercenaries)
            for faction in nonPairedFactionsMercenaries:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        case "Magia":
            # Magic no tiene facciones emparejadas para eliminar
            #globalListOfPairedFactions.remove(pairedFactionsMagic)
            for faction in nonPairedFactionsMagic:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)
        # Fuego
        case _:
            # Fuego doesn't have paired factions
            #globalListOfPairedFactions.remove(pairedFactionsFire)
            for faction in nonPairedFactionsFire:
                if faction in globalListOfNonPairedFactions:
                    globalListOfNonPairedFactions.remove(faction)

            expansionsNotAdded.append(inputDelete)
            expansionsAdded.remove(inputDelete)