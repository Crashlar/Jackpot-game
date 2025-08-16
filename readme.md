#  Jackpot Game

A fun and interactive number guessing game built in Python. Choose your difficulty level, test your intuition, and try to beat your high score!

##  Features

- Multiple difficulty levels: Easy, Medium, Hard
- Hint system (available only in Hard mode)
- High score tracking per difficulty
- Game duration timer
- Replay option
- Modular code structure for readability and scalability

##  Use Case

1. Run the game using `gamie.py`.
2. Choose a difficulty level:
   - Easy: 10 attempts
   - Medium: 5 attempts
   - Hard: 3 attempts + hint support
3. Try to guess the number between 1 and 100.
4. In Hard mode, type `hint` to get a clue after 3 failed attempts.
5. Beat your best score and replay as many times as you like!

##  Setup

```bash
# Clone the repository
git clone https://github.com/Crashlar/Jackpot-game.git

# Navigate to the project folder
cd Jackpot-game

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python gamie.py

```


## File Structure
```
Jackpot-game/
├── gamie.py           # Core game logic and helper functions
├── main.py            # Entry point to start the game
├── requirements.txt   # Dependencies (if any)
└── .gitignore         # Git ignore rules

```

## Future Enhancements
- Save high scores across sessions
- Add GUI using Tkinter or PyQt
- Multiplayer mode or leaderboard
- Sound effects and animations


## Contributing
Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repo and submit a pull request.

Whether you're a beginner or experienced developer, your input is valued.



<!-- <p align="center" color = "red"><strong>Made by Crashlar</strong></p> -->

##### try roadmap
````
https://roadmap.sh/projects/number-guessing-game
````

<p align="center"><strong>Made by <span style="color:red;">Crashlar</span></strong></p>

