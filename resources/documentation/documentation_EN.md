# Code documentation - Random deck generator for Claim

## General description

This script allows generating a random faction deck for a card game called Claim. Players can add and remove expansions, view selected expansions, and generate a deck based on chosen options.

---

## Libraries used

- `random`: To randomly select factions.
- `time`: To handle execution pauses and delays.

---

## Faction definitions

### Claims and expansions

#### Claim I

- **Paired Factions**: `Goblins and Knights`
- **Unpaired Factions**: `Doppelgangers`, `Dwarves`, `Undeads`

#### Claim II

- **Paired Factions**: `Giants and Gnomes`
- **Unpaired Factions**: `Dragons`, `Seers`, `Trolls`

#### Claim V (V Anniversary Edition)

- **Paired Factions**: `Royalty and Peasants`
- **Unpaired Factions**: `Automatons`, `Bards`, `Raccoons`, `Vikings`, `Griffins`

### Thematic expansions

#### Fear

- **Unpaired Factions**: `Shadows`, `Vampires`, `Werewolves`, `Zombies`

#### Frost

- **Paired Factions**: `Ice Queen and King`
- **Unpaired Factions**: `Yetis`, `Ice Beasts`

#### Maps

- **Paired Factions**: `Basilisks and Unicorns`
- **Unpaired Factions**: `Phoenixes`

#### Mercenaries

- **Paired Factions**: `Orcs, Elves and Elves and Orcs`
- **Unpaired Factions**: `Cyclops`

#### Magic

- **Unpaired Factions**: `Druids`, `Shape shifters`, `Wizards`

#### Fire

- **Unpaired Factions**: `Demons`, `Fire Elementals`, `Poisoners`, `Tricksters`

---

## Global variables

- `globalListOfPairedFactions`: List of selected paired factions.
- `globalListOfNonPairedFactions`: List of selected unpaired factions.
- `expansionsNotAdded`: List of available but not added expansions.
- `expansionsAdded`: List of expansions added by the user.

---

## Main functions

### **Menu and user input**

- `printGeneralOptions()`: Displays the main menu options.
- `printAddDeleteOptions()`: Displays the expansion management options.
- `deploySelectOptionsAndTakeInput()`: Captures user selection in the main menu.
- `delployAddDeleteOptionsAndTakeInput()`: Captures user selection in the expansion management menu.
- `takeNumberOfPlayersInput()`: Requests the number of players and validates input.

### **Expansion manager**

- `showExpansionsAndFactions()`: Displays selected expansions and their factions.
- `cleanPool()`: Resets the expansion and faction lists.
- `addAllExpansionsToPool()`: Adds all available expansions.
- `addEveryFaction()`: Adds each faction from all available expansions.
- `addExpansionInput()`: Prompts the user to add an expansion.
- `removeExpansionInput()`: Prompts the user to remove an expansion.
- `addAnExpansion(inputAdd)`: Adds an expansion to the faction lists.
- `removeAnExpansion(inputDelete)`: Removes an expansion from the faction lists.

### **Deck generation**

- `chooseNumberOfFactions()`: Determines the number of factions in the deck based on the number of players.
- `generateRandomDeck()`: Generates a random deck based on selected factions.

### **Utilities**

- `printSpace()`: Prints a line break for better formatting.
- `goodByeMessage()`: Displays a farewell message and waits a few seconds.
- `printLogo()`: Displays a decorative ASCII logo.

---

## Program flow

1. The options menu is displayed to the user.
2. The user selects between adding/removing expansions, showing added expansions, or generating a random deck.
3. If deck generation is selected, the number of players is requested.
4. Paired and unpaired factions are randomly selected according to established rules.
5. The generated deck is printed.