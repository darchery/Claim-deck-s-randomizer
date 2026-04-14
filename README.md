# Claim Deck Generator

A console interface program which creates random decks for the card game **Claim**.

> 🔗 [Official Claim distributor](http://playsdgames.com/coleccion/claim/)

---

## Requirements

- Python 3.10 or higher (the program uses `match/case` statements)
- No external libraries needed — only Python's standard library

---

## Installation

### Windows

1. Download and install Python from [python.org](https://www.python.org/downloads/)
   - During installation, check **"Add Python to PATH"**
2. Download or clone this repository:
   ```
   git clone https://github.com/darchery/Claim-deck-s-randomizer.git
   ```
3. Open **Command Prompt** and navigate to the project folder:
   ```
   cd path\to\Claim-deck-s-randomizer
   ```

### macOS

1. Install Python via [python.org](https://www.python.org/downloads/) or Homebrew:
   ```
   brew install python
   ```
2. Clone the repository:
   ```
   git clone https://github.com/darchery/Claim-deck-s-randomizer.git
   ```
3. Open **Terminal** and navigate to the project folder:
   ```
   cd path/to/Claim-deck-s-randomizer
   ```

### Linux

1. Install Python (most distros include it by default):
   ```
   sudo apt install python3      # Ubuntu/Debian
   sudo dnf install python3      # Fedora
   sudo pacman -S python         # Arch
   ```
2. Clone the repository:
   ```
   git clone https://github.com/darchery/Claim-deck-s-randomizer.git
   ```
3. Open a terminal and navigate to the project folder:
   ```
   cd path/to/Claim-deck-s-randomizer
   ```

---

## Running the program

From inside the `src/EN_version/` folder:

```
cd src/EN_version
python main.py
```

Or from the project root:

```
python src/EN_version/main.py
```

---

## How to use

When you launch the program, you will see the main menu:

```
Available menu options:
1. Generate a random deck
2. Organise your actual expansions
3. Show your selected expansions
4. Exit
```

### Step 1 — Add your expansions (option 2)

Before generating a deck, you need to add the expansions you own. Select option `2` to open the expansion manager:

```
Organisation options:
1. Add an expansion
2. Remove an expansion
3. Clean all the expansions selected
4. Add all the available expansions
5. Back
```

- **Add an expansion (1):** Shows the list of available expansions and asks you to type the name of the one you want to add.
- **Remove an expansion (2):** Shows your current expansions and lets you remove one.
- **Clean all (3):** Removes all expansions from the current pool.
- **Add all (4):** Adds every available expansion at once.
- **Back (5):** Returns to the main menu.

Available expansions: `Claim I`, `Claim II`, `Claim V`, `Fear`, `Frost`, `Maps`, `Mercenaries`, `Magic`, `Fire`

> ⚠️ You need at least **1 paired faction** and **3 non-paired factions** to generate a deck. With 3 or 4 players you need at least **5 non-paired factions**.

### Step 2 — Check your pool (option 3)

Use option `3` to see which expansions and factions are currently selected before generating.

### Step 3 — Generate a deck (option 1)

Select option `1` and enter the number of players (`2`, `3` or `4`). The program will randomly generate a deck:

- **2 players:** 1 paired faction + 3 non-paired factions (5 total)
- **3–4 players:** 1 paired faction + 5 non-paired factions (7 total)

Example output:
```
Your randomly generated deck for 2 players is composed by:
- Goblins and Knights
- Dwarves, Undeads and Dragons
```

### Step 4 — Exit (option 4)

Select option `4` to close the program.