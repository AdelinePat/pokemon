# Map for pokemon

# Pokémon Game in Python

![preview main](gameplay.jpg)

This project is an implementation of the classic Pokémon game using the **Pygame** library.

🎮 Features:

- **Interative Map** : Navigate using your keyboard across different maps.
- **Pokémon Capture System**: Catch Pokémon randomly in tall grass with Pokéballs after defeating them.
- **Bike Mode**: Ride a bike by pressing the 'B' key and dismount with another press.
- **Sound Effects**: Immersive experience with in-game sound effects.

# Description

This project is a **Pokémon game** developed in **Python**. It allows players to capture, train, and battle with Pokémon in an interactive environment. The game includes several features inspired by the famous Pokémon franchise.

## Features

- **Trainer selection** : Customize your trainer and start your adventure.
- **Pokémon capture** : Capture wild Pokémon after defeating them in battle.
- **Battle Mechanics** : Engage in turn-based battles with wild and other trainers' Pokémon.
- **Health Points Management**: Keep track of your Pokémon’s health during battles.
- **Pokémon Storage**: Manage your team and store Pokémon in your inventory.
- **Map Exploration:** Navigate through a detailed map using the keyboard.
- **Bike Mode**: Speed up your exploration with the bike.

## Installation

Make sure you have Python installed (version 3.x recommended) before running the game.

### Installation Steps

1. Clone this repository or download the files:

   ```bash
   git clone https://github.com/AdelinePat/pokemon.git
   ```

2. Install dependencies if necessary:

```bash

pip install pygame
pip install pytmx
pip install pyscroll
```

## Usage

1. Run `main.py` to start the game.
2. Follow the on-screen instructions to capture and train your Pokémon.
3. Participate in battles to improve your skills.

## Project Structure

📂 pokemon-game
├── 📁 assets/ # Graphics and sound resources  
├── 📁 back_end/ # Pokémon generation and JSON file handling  
│ ├── entity.py # Handles player and entity interactions  
│ ├── keylistener.py # Manages keyboard inputs for player movement  
│ └── switch.py # Logic for map transitions and switches  
├── 📁 front_end/ # For battle system and graphical interface  
│ ├── gameplay/  
│ │ ├── entity.py # Player and entity movement logic  
│ │ ├── battlescreen.py # Displays battle screen/battle logic  
│ │ └── in_fight.py # Core combat interaction with Pokémon  
│ ├── menu/ # Handles menu navigation/user interface  
│ ├── sounds/ # Sound effects and music management 
│ └── screen.py # Manages screen rendering and visual updates  
├── 📁 new_menu/ # Custom menu handling
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── .gitignore # Files to exclude from version control  
└── main.py # Main source code, starts the game

## Detailed File Roled

- `back_end/entity.py` : Contains the logic for entities (e.g., player, wild Pokémon) in the game. The `Player` class, for example, definies movement, battles initiation and interation with the environment.

- `back_end/keylistener.py`: Handles all keyboard inputs, such as player movement or actions like riding the bike. It allows the player to move around the map and interact with the environment seamlessly.

- `back_end/switch.py`: This file is responsible for map transitions, managing different areas of the game world. It stores the logic for when and how the map should change as the player interacts with the environment (e.g., through specific switches or triggers).

- `front_end/gameplay/entity.py`: Similar to back_end/entity.py, but specifically for managing the player's actions, position, and interactions within the game. This file extends the functionality of entities in the visual portion of the game.

- `front_end/gameplay/battlescreen.py`: Manages the battle screen, which is displayed when the player engages in combat with wild Pokémon. This file includes the logic for battle flow, including turn-based actions and Pokémon stats management.

- `front_end/gameplay/in_fight.py`: Contains the core mechanics for the battle system, such as Pokémon moves, health points, and player choices during the battle.

- `front_end/sounds/`: Manages all sound effects used in the game. This includes background music for different areas of the game and battle music, enhancing the overall gameplay experience.

- `new_menu/`: Custom menus and UI elements not included in the standard gameplay loop. For instance, it could manage menus for pausing the game, displaying the player's inventory, or other interface elements.

# Contributing

This project was made by:

- [Adeline Patenne](https://github.com/AdelinePat/)
- [Florence Navet](https://github.com/florence-navet)
- [Thibault Manse](https://github.com/thibault-manse)
- [Joseph Dmytriyev ](https://github.com/joseph-Dmytrieyv)

### Licence

This project is licensed under the MIT License.

## Acknowledgments

Thanks to everyone contributing to the development of this game!
