# Documentación del código - Generador de mazos aleatorios de Claim 

## Descripción general

Este script permite generar un mazo aleatorio de facciones para un juego de cartas llamado Claim. Los jugadores pueden agregar y eliminar expansiones, ver las expansiones seleccionadas y generar un mazo según las opciones elegidas.

---

## Librerías utilizadas

- `random`: Para realizar selecciones aleatorias de facciones.
- `time`: Para manejar pausas y retardos en la ejecución.

---

## Recopilación de expansiones y facciones

### Juegos base de Claim y sus expansiones

#### Claim I

- **Facciones Emparejadas**: `Goblins and Knights`
- **Facciones No Emparejadas**: `Doppelgangers`, `Dwarves`, `Undeads`

#### Claim II

- **Facciones Emparejadas**: `Giants and Gnomes`
- **Facciones No Emparejadas**: `Dragons`, `Seers`, `Trolls`

#### Claim V (Edición V Aniversario)

- **Facciones Emparejadas**: `Royalty and Peasants`
- **Facciones No Emparejadas**: `Automatons`, `Bards`, `Raccoons`, `Vikings`, `Griffins`

### Expansiones Temáticas

#### Terror

- **Facciones No Emparejadas**: `Shadows`, `Vampires`, `Werewolves`, `Zombies`

#### Hielo

- **Facciones Emparejadas**: `Ice Queen and King`
- **Facciones No Emparejadas**: `Yetis`, `Ice Beasts`

#### Mapas

- **Facciones Emparejadas**: `Basilisks and Unicorns`
- **Facciones No Emparejadas**: `Phoenixes`

#### Mercenarios

- **Facciones Emparejadas**: `Orcs, Elves and Elves and Orcs`
- **Facciones No Emparejadas**: `Cyclops`

#### Magia

- **Facciones No Emparejadas**: `Druids`, `Shape shifters`, `Wizards`

#### Fuego

- **Facciones No Emparejadas**: `Demons`, `Fire Elementals`, `Poisoners`, `Tricksters`

---

## Variables globales

- `globalListOfPairedFactions`: Lista de facciones emparejadas seleccionadas.
- `globalListOfNonPairedFactions`: Lista de facciones no emparejadas seleccionadas.
- `expansionsNotAdded`: Lista de expansiones disponibles pero no agregadas.
- `expansionsAdded`: Lista de expansiones agregadas por el usuario.

---

## Funciones principales

### **Menú y entrada de usuario**

- `printGeneralOptions()`: Muestra las opciones del menú principal.
- `printAddDeleteOptions()`: Muestra las opciones de organización de expansiones.
- `deploySelectOptionsAndTakeInput()`: Captura la selección del usuario en el menú principal.
- `delployAddDeleteOptionsAndTakeInput()`: Captura la selección del usuario en el menú de organización.
- `takeNumberOfPlayersInput()`: Solicita el número de jugadores y valida la entrada.

### **Gestor de expansiones**

- `showExpansionsAndFactions()`: Muestra las expansiones seleccionadas y sus facciones.
- `cleanPool()`: Restablece las listas de expansiones y facciones.
- `addAllExpansionsToPool()`: Agrega todas las expansiones disponibles.
- `addEveryFaction()`: Agrega cada facción de todas las expansiones disponibles.
- `addExpansionInput()`: Solicita al usuario que agregue una expansión.
- `removeExpansionInput()`: Solicita al usuario que elimine una expansión.
- `addAnExpansion(inputAdd)`: Agrega una expansión a las listas de facciones.
- `removeAnExpansion(inputDelete)`: Elimina una expansión de las listas de facciones.

### **Generación de mazos**

- `chooseNumberOfFactions()`: Determina el número de facciones en el mazo según la cantidad de jugadores.
- `generateRandomDeck()`: Genera un mazo aleatorio basado en las facciones seleccionadas.

### **Utilidades**

- `printSpace()`: Imprime un salto de línea para mejor formato.
- `goodByeMessage()`: Muestra un mensaje de despedida y espera unos segundos.
- `printLogo()`: Muestra un logo ASCII decorativo.

---

## Flujo del programa

1. Se muestra el menú de opciones al usuario.
2. El usuario selecciona entre agregar/eliminar expansiones, mostrar expansiones agregadas o generar un mazo aleatorio.
3. Si se selecciona la generación de mazo, se solicita el número de jugadores.
4. Se seleccionan al azar facciones emparejadas y no emparejadas según las reglas establecidas.
5. Se imprime el mazo generado.

