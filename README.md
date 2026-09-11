# ♟️ Python Chess Game (PvP & Bot)

A lightweight, clean chess application built in Python using [`python-chess`](https://python-chess.readthedocs.io/) for core rules and move generation, paired with [`pygame`](https://www.pygame.org/) for rendering.

Supports local 2-player pass-and-play and single-player vs. a Minimax evaluation bot.

---

## Quick Start

### Prerequisites
- Python 3.10+

### Installation

1. Clone the repository:
   ```
   git clone [https://github.com/](https://github.com/estherg12/ChessGameBot.git
   cd ChessGameBot
   ```
2. Create and activate a virtual enviromen
* Windows: 
```
py -m venv .venv
.venv\Scripts\activate
```
* Linux / macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies: ```pip install -r requirements.txt```
4. Run the game: ```python main.py```

---

## Controls
| Key/Action | Description                                  |
|------------|----------------------------------------------|
| 1          | Switch to **PvP Pass & Play** mode           |
| 2          | Switch to **Vs. Bot** mode (Bot plays Black) |
| R          | Reset the board                              |
| Left Click | Select a piece / Target square to move       |

## Roadmap & Up next
We have open issues tracking immediate enhancements:

- [ ] Legal move indicator dots on selection
- [ ] Sound effects for moves, captures, checks, and game over
- [ ] High-resolution realistic piece sets (with toggles)
- [ ] Beginner Mode: hover trajectory arrows/target highlights
- [ ] Realistic simulated think delay for bot turns
- [ ] UCI / Stockfish engine support with variable difficulty levels

Want to tackle one of these? Check out our [Issues](https://github.com/estherg12/ChessGameBot/issues) tab and read [CONTRIBUTING.md](https://github.com/estherg12/ChessGameBot/blob/main/CONTRIBUTING.md) to get started!

---

## Contributing
Contributions are what make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are greatly appreciated. Please see [CONTRIBUTING.md]([CONTRIBUTING.md](https://github.com/estherg12/ChessGameBot/blob/main/CONTRIBUTING.md)) for details on code style, issue assignment, and pull request workflows.

---

## License
Distributed under the MIT License.
