# Librerías
# Mi propia librería con las funciones, variables y constantes
from src.ES_version import functions_variables_constantsES

# Imprimir el logo
functions_variables_constantsES.printLogo()

# Mensaje de bienvenida
functions_variables_constantsES.printSpace()
print("Hola, bienvenid@ al generador de mazos de Claim...")
functions_variables_constantsES.printSpace()

# Imprimir las opciones de selección y tomar la opción seleccionada por el usuario
functions_variables_constantsES.deploySelectOptionsAndTakeInput()

# Mientras el usuario no salga (4)
while functions_variables_constantsES.option != 4:

    # Obtener un mazo aleatorio

    # Ejecuciones excepcionales
    # No se puede jugar sin al menos 2 facciones emparejadas
    if functions_variables_constantsES.option == 1 and not functions_variables_constantsES.globalListOfPairedFactions:
        print("Por favor, añade alguna expansión con facciones emparejadas para jugar...")
        functions_variables_constantsES.printSpace()
    # No se puede jugar con menos de 3 facciones
    if functions_variables_constantsES.option == 1 and len(
            functions_variables_constantsES.globalListOfNonPairedFactions) < 3:
        print("Por favor, añade al menos 3 facciones no emparejadas para jugar...")
        functions_variables_constantsES.printSpace()

    # Ejecución normal
    if (functions_variables_constantsES.option == 1 and functions_variables_constantsES.globalListOfPairedFactions
            and len(functions_variables_constantsES.globalListOfNonPairedFactions) >= 3):
        # Preguntar al usuario cuántos jugadores van a jugar
        functions_variables_constantsES.takeNumberOfPlayersInput()

        # Excepción de ejecución del número de jugadores
        # Si el número de jugadores es 3 o 4 y la lista global de facciones no emparejadas tiene menos de 5 facciones, no se puede jugar
        if (functions_variables_constantsES.numberOfPlayers in [3, 4]
                and len(functions_variables_constantsES.globalListOfNonPairedFactions) < 5):
            print(
                f"Por favor, añade al menos 5 facciones no emparejadas para jugar con {functions_variables_constantsES.numberOfPlayers} jugadores...")
            functions_variables_constantsES.printSpace()

        # Continuar con la ejecución normal
        else:
            # Dependiendo de cuántos jugadores haya, se jugará con 8 facciones (3-4 jugadores) o 5 facciones (2 jugadores)
            functions_variables_constantsES.chooseNumberOfFactions()
            # Elegir mazos aleatoriamente y mostrarlos al usuario
            functions_variables_constantsES.generateRandomDeck()

    # Elegir entre añadir y eliminar una expansión
    elif functions_variables_constantsES.option == 2:
        # Organizar las opciones posibles
        # Imprimir opciones de añadir/eliminar y tomar la opción seleccionada por el usuario
        functions_variables_constantsES.delployAddDeleteOptionsAndTakeInput()

        while functions_variables_constantsES.optionAddDelete != 5:

            # Añadir una expansión
            if functions_variables_constantsES.optionAddDelete == 1:
                functions_variables_constantsES.addExpansionInput()

            # Eliminar una expansión
            elif functions_variables_constantsES.optionAddDelete == 2:
                functions_variables_constantsES.removeExpansionInput()

            # Limpiar todas las expansiones seleccionadas
            elif functions_variables_constantsES.optionAddDelete == 3:
                functions_variables_constantsES.cleanPool()
                print("Ahora el grupo de mazos está vacío...")

            # Añadir todas las expansiones disponibles
            elif functions_variables_constantsES.optionAddDelete == 4:
                functions_variables_constantsES.addAllExpansionsToPool()

            # Repetir las opciones de añadir/eliminar
            functions_variables_constantsES.printSpace()
            # Imprimir opciones de añadir/eliminar y tomar la opción seleccionada por el usuario
            functions_variables_constantsES.delployAddDeleteOptionsAndTakeInput()

    # Mostrar las expansiones actuales añadidas al mazo
    elif functions_variables_constantsES.option == 3:
        functions_variables_constantsES.showExpansionsAndFactions()

    # Repetir las opciones generales
    # Imprimir opciones de selección y tomar la opción seleccionada por el usuario
    functions_variables_constantsES.deploySelectOptionsAndTakeInput()

# Finalizar el programa
functions_variables_constantsES.goodByeMessage()
