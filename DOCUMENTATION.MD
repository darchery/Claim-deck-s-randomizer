# Code Documentation — Claim Deck Generator

## General description

This script generates a random faction deck for the card game Claim. Players can add and remove expansions, view their current selection, and generate a deck based on the chosen options. The program is split into two files: `main.py` handles the program flow, and `functions_variables_constants.py` contains all data, logic and helper functions.

---

## Project structure

```
Claim-deck-s-randomizer/
├── src/
│   ├── EN_version/
│   │   ├── main/
│   │   │   ├── main.py
│   │   │   └── functions_variables_constants.py
│   │   └── test/
│   │       └── test.py
│   └── ES_version/
│       ├── main/
│       │   ├── main.py
│       │   └── functions_variables_constants.py
│       └── test/
│           └── test.py
├── installer/
├── resources/
├── README.md
└── DOCUMENTATION.MD
```

---

## Libraries used

- `random` — to randomly select factions when generating a deck
- `time` — to add a short delay in the goodbye message

---

## Faction definitions (`functions_variables_constants.py`)

### Base games

| Expansion | Paired factions | Non-paired factions |
|-----------|----------------|---------------------|
| Claim I | Goblins and Knights | Doppelgangers, Dwarves, Undeads |
| Claim II | Giants and Gnomes | Dragons, Seers, Trolls |
| Claim V | Royalty and Peasants | Automatons, Bards, Raccoons, Vikings, Griffins |

### Thematic expansions

| Expansion | Paired factions | Non-paired factions |
|-----------|----------------|---------------------|
| Fear | — | Shadows, Vampires, Werewolves, Zombies |
| Frost | Ice Queen and King | Yetis, Ice Beasts |
| Maps | Basilisks and Unicorns | Phoenixes |
| Mercenaries | Orcs, Elves and Elves and Orcs | Cyclops |
| Magic | — | Druids, Shape shifters, Wizards |
| Fire | — | Demons, Fire Elementals, Poisoners, Tricksters |

---

## Global variables

| Variable | Type | Description |
|----------|------|-------------|
| `globalListOfPairedFactions` | `list` | Paired factions currently in the pool |
| `globalListOfNonPairedFactions` | `list` | Non-paired factions currently in the pool |
| `expansionsNotAdded` | `list` | Expansions available but not yet selected |
| `expansionsAdded` | `list` | Expansions currently selected by the user |
| `option` | `int` | Current selection in the main menu |
| `optionAddDelete` | `int` | Current selection in the expansion manager menu |
| `numberOfPlayers` | `int` | Number of players entered by the user |
| `numbersOfFactions` | `int` | Number of non-paired factions to include in the deck |

---

## Constants

| Constant | Value |
|----------|-------|
| `SELECT_OPTION_MESSAGE` | `"Select an option: "` |
| `WRONG_OPTION_MESSAGE` | `"Wrong option, please enter 1, 2, 3 or 4: "` |
| `CLAIM_I` … `FIRE` | String identifiers for each expansion |

---

## Functions

### Menu and user input

**`printGeneralOptions()`**
Prints the four options of the main menu to the console.

**`printAddDeleteOptions()`**
Prints the five options of the expansion manager menu.

**`deploySelectOptionsAndTakeInput()`**
Displays the main menu, reads the user's input, and validates it. Loops until a valid option (`1`–`4`) is entered. Stores the result as an integer in the global variable `option`.

**`delployAddDeleteOptionsAndTakeInput()`**
Same as above for the expansion manager menu. Validates options `1`–`5` and stores the result in `optionAddDelete`.

**`takeNumberOfPlayersInput()`**
Prompts the user for the number of players. Validates that the input is `2`, `3` or `4` and stores it as an integer in `numberOfPlayers`.

---

### Expansion manager

**`showExpansionsAndFactions()`**
Prints the currently added expansions along with their paired and non-paired factions. If no expansions have been added, it prints a warning message.

**`cleanPool()`**
Resets all four global lists to their initial state: empties `globalListOfPairedFactions`, `globalListOfNonPairedFactions` and `expansionsAdded`, and refills `expansionsNotAdded` with all expansions.

**`addAllExpansionsToPool()`**
Calls `cleanPool()` first to avoid duplicates, then calls `addEveryFaction()` to populate both faction lists, and finally sets `expansionsAdded` to the full list and `expansionsNotAdded` to empty.

**`addEveryFaction()`**
Calls `addAnExpansion()` for every available expansion in sequence.

**`addExpansionInput()`**
Displays the available expansions and prompts the user to type a name. Validates the input against `expansionsNotAdded` and calls `addAnExpansion()`.

**`removeExpansionInput()`**
Displays the currently added expansions and prompts the user to type a name. Validates the input against `expansionsAdded` and calls `removeAnExpansion()`.

**`addAnExpansion(inputAdd)`**
Uses a `match/case` statement to add the correct paired and non-paired factions to the global lists based on the expansion name. Moves the expansion from `expansionsNotAdded` to `expansionsAdded`.

**`removeAnExpansion(inputDelete)`**
Uses a `match/case` statement to remove the correct factions from the global lists. Moves the expansion from `expansionsAdded` back to `expansionsNotAdded`.

---

### Deck generation

**`chooseNumberOfFactions()`**
Sets the global variable `numbersOfFactions` based on `numberOfPlayers`: `3` for 2 players, `5` for 3–4 players. Also prints a description of the deck structure.

**`generateRandomDeck()`**
Shuffles `globalListOfPairedFactions` and picks one randomly. Then uses `random.sample()` to pick `numbersOfFactions` non-paired factions from `globalListOfNonPairedFactions`. Prints the resulting deck.

---

### Utilities

**`printSpace()`**
Prints two newlines for visual separation between console outputs.

**`printLogo()`**
Prints the ASCII art logo of the program at startup.

**`goodByeMessage()`**
Prints a farewell message and waits 3 seconds before the program exits.

---

## Program flow

```
Start
  │
  ├─ printLogo()
  ├─ Welcome message
  ├─ deploySelectOptionsAndTakeInput()
  │
  └─ while option != 4:
       │
       ├─ option == 1 → Generate deck
       │     ├─ Validate paired factions exist
       │     ├─ Validate at least 3 non-paired factions
       │     ├─ takeNumberOfPlayersInput()
       │     ├─ Validate enough factions for player count
       │     ├─ chooseNumberOfFactions()
       │     └─ generateRandomDeck()
       │
       ├─ option == 2 → Manage expansions
       │     └─ while optionAddDelete != 5:
       │           ├─ 1 → addExpansionInput()
       │           ├─ 2 → removeExpansionInput()
       │           ├─ 3 → cleanPool()
       │           └─ 4 → addAllExpansionsToPool()
       │
       ├─ option == 3 → showExpansionsAndFactions()
       │
       └─ deploySelectOptionsAndTakeInput()  ← repeat menu

  goodByeMessage()
End
```

---

## Unit tests

The project includes comprehensive unit tests located in `src/EN_version/test/test.py` (for EN version) and `src/ES_version/test/test.py` (for ES version).

### Running the tests

```bash
# From EN version test folder
cd src/EN_version/test && python test.py

# From ES version test folder
cd src/ES_version/test && python test.py
```

### Test coverage

The tests cover all major functions and edge cases:

| Test class | Tests | Description |
|------------|-------|-------------|
| `TestCleanPool` | 5 | Verifies pool cleanup resets all lists correctly |
| `TestAddAnExpansion` | 26 | Tests adding each of the 9 expansions with their factions |
| `TestRemoveAnExpansion` | 11 | Tests removing expansions and faction cleanup |
| `TestAddAllExpansionsToPool` | 5 | Verifies adding all expansions at once |
| `TestChooseNumberOfFactions` | 3 | Tests faction count based on player count |
| `TestGenerateRandomDeck` | 3 | Tests deck generation doesn't modify global lists |
| `TestDeploySelectOptionsAndTakeInput` | 3 | Tests main menu input validation |
| `TestDelployAddDeleteOptionsAndTakeInput` | 2 | Tests expansion manager menu input |
| `TestTakeNumberOfPlayersInput` | 4 | Tests player count input validation |
| `TestEdgeCases` | 7 | Tests error handling and edge cases |

**Total: 63 tests per version**

### Test functions

#### cleanPool

- `test_clean_pool_empties_paired_factions`
- `test_clean_pool_empties_non_paired_factions`
- `test_clean_pool_resets_expansions_not_added`
- `test_clean_pool_empties_expansions_added`
- `test_clean_pool_restores_all_nine_expansions`

#### addAnExpansion

For each expansion (Claim I, Claim II, Claim V, Fear, Frost, Maps, Mercenaries, Magic, Fire):
- `test_add_<expansion>_adds_paired_faction` (where applicable)
- `test_add_<expansion>_adds_non_paired_factions` (or single faction)
- `test_add_<expansion>_moves_to_added_list`

#### removeAnExpansion

For each expansion:
- `test_remove_<expansion>_removes_paired_faction` (where applicable)
- `test_remove_<expansion>_removes_non_paired_factions`
- `test_remove_<expansion>_moves_back_to_not_added`

Plus cross-expansion tests:
- `test_add_and_remove_does_not_change_other_expansions`

#### Edge cases tested

- Adding the same expansion twice raises `ValueError`
- Removing an expansion not in the pool raises `ValueError`
- Clean pool after add all resets correctly
- Expansions added list tracks correctly
- Expansions without paired factions (Fear, Magic, Fire) don't add to paired list

### Test structure

```python
def reset_state():
    """Helper to reset all global state between tests."""
    fvc.globalListOfPairedFactions = []
    fvc.globalListOfNonPairedFactions = []
    fvc.expansionsNotAdded = [fvc.CLAIM_I, fvc.CLAIM_II, ...]
    fvc.expansionsAdded = []
```

Each test class has a `setUp()` method that calls `reset_state()` to ensure test independence.
