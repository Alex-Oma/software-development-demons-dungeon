# Demons Dungeon — Detailed User Guide & Software Operating Instructions

## 1. Introduction

Demons Dungeon is a retro-style first-person shooter built with Python 3.12 and PyGame. The game is inspired by classic FPS titles such as Doom and Wolfenstein 3D. The player explores a dungeon, fights demons, manages health and ammo, and attempts to defeat the boss demon and reach the exit to win.

This guide explains how to start the game, understand the controls, read the HUD, fight enemies, use the menu system, and handle the main game states.

---

## 2. System Requirements and Platform

### 2.1 Supported platform
- Windows is the primary development and test platform.
- The game is a desktop application.

### 2.2 Software stack
- Python 3.12
- PyGame
- JSON file storage for leaderboard data
- PyCharm is the main development environment used for the project

### 2.3 Required files and assets
The game uses local assets stored in the project folder, including:
- textures
- sprites
- sound effects
- menu background image
- font files
- leaderboard JSON file

---

## 3. Starting the Game

### 3.1 Launching the application
Start the game from the project entry point. The game opens in a desktop window and shows the main menu.

### 3.2 Main menu behavior
The main menu includes the following options:
- Player Name
- New Game
- Leaderboard
- Game Credits
- Quit Game

You can navigate the menu using the keyboard. The currently selected option is highlighted with a red rectangle.

### 3.3 Menu controls
- Up/Down arrows: move through menu options
- Enter or Spacebar: confirm the selected option
- Escape: quit the game during gameplay

---

## 4. Player Name Entry

Before starting a new game, you can enter a player name from the menu.

### Steps
1. Open the main menu.
2. Select **Player Name**.
3. Type the desired name.
4. Press **Enter** to confirm.

The player name is used for leaderboard tracking when the game ends.

---

## 5. Core Gameplay Loop

### 5.1 Objective
The main goal is to survive the dungeon, defeat demons, collect points, and reach the exit after defeating the boss demon.

### 5.2 Basic loop
- Move through the dungeon.
- Find and fight enemies.
- Manage ammo and health.
- Collect points for kills.
- Defeat the boss demon.
- Reach the exit to win.

### 5.3 Player state tracked in the game
The HUD and game logic track:
- health
- ammo
- score
- kill count
- current weapon
- armor status when active

---

## 6. Controls

### 6.1 Movement and view
- **W**: move forward
- **S**: move backward
- **A**: strafe left
- **D**: strafe right
- **Mouse movement**: rotate the view and aim

### 6.2 Combat
- **Left mouse button**: fire the current weapon

### 6.3 Weapon switching
The game supports direct weapon selection with the number keys:
- **1**: Shotgun
- **2**: AN94
- **3**: Minigun

### 6.4 General controls
- **Escape**: quit the game

---

## 7. Heads-Up Display (HUD)

The HUD is displayed across the top of the screen during gameplay.

### 7.1 HUD elements
The HUD shows:
- Score
- Level
- Ammo
- Kill count
- Player health
- Active weapon icon and weapon name
- Warning when switching weapons is blocked
- Armor icon and armor timer while armor is active

### 7.2 HUD layout
The main HUD text is arranged across the top of the screen, while the current weapon icon is shown in the bottom-right corner.

### 7.3 Armor display
When armor is active, the HUD shows:
- an armor icon
- the text `Armor Active: <seconds remaining>`

When the armor timer expires, the icon and timer disappear.

---

## 8. Weapons

The game includes three player weapons.

### 8.1 Shotgun
- Default weapon at game start
- Single-shot weapon
- Uses shotgun sprites and sound
- Best for controlled, powerful shots

### 8.2 AN94
- Automatic weapon
- Balanced damage and fire rate
- Uses its own weapon sprites and firing sound
- Can be fired continuously while the mouse button is held

### 8.3 Minigun
- High-rate-of-fire automatic weapon
- Lower per-shot damage
- Uses its own weapon sprites and firing sound
- Designed for sustained fire

### 8.4 Weapon switching rules
- Use **1/2/3** to switch directly between weapons
- The current weapon icon and name update on the HUD
- Switching can be blocked while the current weapon is reloading
- If blocked, the message `Cannot switch while reloading` appears briefly

---

## 9. Armor System

### 9.1 What armor does
Armor is a collectible pickup that temporarily reduces incoming damage by **50%**.

### 9.2 How to collect armor
Move over the armor pickup sprite in the level. When collected:
- the armor sprite disappears
- armor becomes active
- the HUD shows the armor icon and countdown
- a pickup sound is played

### 9.3 Duration
Armor remains active for **60 seconds**.

### 9.4 Damage reduction
While armor is active, any enemy damage taken by the player is halved.

### 9.5 Expiration
After the armor timer ends:
- the armor effect is disabled
- the HUD armor icon disappears
- damage returns to normal

---

## 10. Enemies

The game contains multiple enemy types. Enemies use shared AI behavior:
- idle when the player is not detected
- chase when the player is seen
- attack when in range
- play pain animation when hit
- play death animation when killed

### 10.1 Enemy types

The current implementation includes the following enemy classes:
- BloodGhost: a weak flying enemy that swarms the player and blocks movement
- Abaddon: a medium-range enemy that shoots projectiles at the player
- BloodDemon: a stronger melee enemy that can take more damage and deal more damage
- Afrit: a flying enemy that shoots fireballs at the player
- Aguares: a faster mid-tier enemy that pressures the player at close to medium range
- Celt: a durable close-range melee enemy that remains a strong threat when the player gets close
- Annihilator: the boss demon that must be defeated to win the game

### 10.2 General enemy rules
- Enemies can only attack when they have line of sight and are within range.
- Enemies take damage when the player hits them.
- When enemy health reaches zero, the enemy dies and the player gains score.

---

## 11. Win and Lose Conditions

### 11.1 Losing the game
You lose when the player’s health reaches zero.

When this happens:
- the Game Over screen is shown
- the game returns to the main menu after a short delay
- the score may be saved to the leaderboard if it qualifies

### 11.2 Winning the game
You win when:
- the boss demon is defeated
- the player reaches the exit door

When this happens:
- the Victory screen is shown
- the game returns to the main menu after a short delay
- the score may be saved to the leaderboard if it qualifies

---

## 12. Menus and Screens

### 12.1 Main menu
The main menu provides access to:
- Player Name entry
- New Game
- Leaderboard
- Game Credits
- Quit Game

### 12.2 Game Over screen
Shown when the player dies.

### 12.3 Victory screen
Shown when the player defeats the boss and reaches the exit.

### 12.4 Leaderboard
The leaderboard stores top scores in a JSON file and can be viewed from the menu.

### 12.5 Game Credits
The credits screen identifies the project and creator information.

---

## 13. Sound and Visual Feedback

The game uses audio and visuals to indicate important events.

### 13.1 Player damage
- Screen flashes red
- Player pain sound plays
- Health decreases on the HUD

### 13.2 Enemy hit
- Enemy pain animation plays
- Enemy pain sound plays

### 13.3 Enemy death
- Enemy death animation plays
- Enemy death sound plays
- Score and kill count increase

### 13.4 Weapon firing
- Weapon firing animation plays
- Weapon sound plays
- Ammo decreases

### 13.5 Background music
The game plays ambient dungeon music during gameplay.

---

## 14. Level Navigation and Gameplay Tips

- Keep moving to avoid enemy attacks.
- Use mouse aiming and line-of-sight to line up shots.
- Manage ammo carefully.
- Switch weapons when needed:
  - Shotgun for strong single hits
  - AN94 for balanced sustained fire
  - Minigun for continuous high-rate damage
- Collect armor when available to survive longer.
- Learn enemy behavior so you can retreat or attack at the right time.

---

## 15. Troubleshooting

### 15.1 Game does not start
Check that:
- Python 3.12 is installed
- PyGame is installed
- You are running the project from the correct directory
- The asset folders are present

### 15.2 Missing textures or sprites
If a texture does not appear, confirm that the file exists in the correct `assets/` folder and that the filename matches the code exactly.

### 15.3 No sound plays
Check:
- sound files exist in `assets/sound/`
- the audio device is available
- the system volume is not muted

### 15.4 Controls feel unresponsive
Check:
- the game window is focused
- the keyboard and mouse are connected and working
- the game is not paused or blocked by a modal screen

### 15.5 Leaderboard does not update
Check that:
- the game completed normally
- the score qualified for leaderboard saving
- the `assets/files/leaderboard.json` file is writable

---

## 16. File and Folder Reference

### Important files
- `main.py` — game entry point
- `game.py` — main game loop
- `player.py` — player movement, combat, armor, and health
- `enemy.py` — enemy classes and AI behavior
- `objects_manager.py` — spawns enemies and pickups
- `hud_screen.py` — HUD rendering
- `sound_manager.py` — audio playback
- `menu.py` — menus, leaderboard, credits
- `README.md` — project documentation

### Important asset folders
- `assets/sprites/weapon/` — weapon images
- `assets/sprites/animated/enemies/` — enemy sprites
- `assets/sprites/animated/armor/` — armor sprites
- `assets/sprites/static/` — ammo and health pickups
- `assets/textures/` — level and screen textures
- `assets/sound/` — audio files

---

## 17. Summary

This guide describes how to run and play Demons Dungeon using the features documented in the project README and the current codebase. The key gameplay elements are movement, shooting, weapon switching, enemy combat, armor pickup, HUD feedback, and win/lose progression.

