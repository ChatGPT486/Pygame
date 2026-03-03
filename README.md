# 🏍️ CHAT TPG's Game Window
> Pygame Fundamentals Exercise — Python 3.12 | Pygame 2.6.1 | 800×600

---

## 🎯 Objective

Create a game window using Pygame, personalise it with your name, and ensure it closes cleanly without a force quit.

---

## ✅ Requirements

### Core
- [x] Window title set to `"CHAT TPG's Game Window"`
- [x] Window size is 800×600 pixels
- [x] Window closes properly via the X button (no force quit)

### Bonus (Completed)
- [x] Sprite loaded and drawn — `bike_nobg.png` centered on screen
- [x] Name drawn as text — `"CHAT TPG"` rendered with `pygame.font`

---

## 📁 Project Files

```
Pygame/
├── game_window.py               # Main Python script
├── bike_nobg.png                # Motorcycle sprite (background removed)
└── README.md                    # This file
```

---

## ⚙️ Setup

### 1. Install Python 3.12
Download from https://www.python.org/downloads/  
✔ Check **"Add Python to PATH"** during installation.

### 2. Install Pygame
```bash
pip install pygame
```

### 3. Place files together
`game_window.py` and `bike_nobg.png` must be in the **same folder**.

---

## ▶️ How to Run

Open a terminal, navigate to the project folder, then run:

```powershell
cd "C:\Users\CHAT TPG\Desktop\Pygame"
python game_window.py
```

---

## 🕹️ Controls

| Input | Action |
|-------|--------|
| Window `X` button | Closes the window properly |

---

## 🧠 How the Code Works

| Function | Purpose |
|----------|---------|
| `pygame.init()` | Starts all pygame modules |
| `set_mode((800, 600))` | Creates the 800×600 window |
| `set_caption(...)` | Sets the window title bar text |
| `pygame.event.get()` | Listens for the close button |
| `pygame.QUIT` | Event fired when X is clicked |
| `screen.blit(sprite, (x, y))` | Draws the sprite onto the screen |
| `font.render(...)` | Converts text string to a drawable surface |
| `pygame.display.flip()` | Pushes the drawn frame to the screen |
| `pygame.quit() + sys.exit()` | Shuts everything down cleanly |

---

## 🔧 Troubleshooting

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: pygame` | Run `pip install pygame` |
| Image not loading | Make sure `bike_nobg.png` is in the same folder as `game_window.py` |
| Wrong Python version | Use Python 3.12, not 3.14 |
| Timeout during pip install | Run `pip install pygame --timeout 300` |

---

*CHAT TPG — Pygame Exercise — 2026*
