# Software Development - Semester B - Demons Dungeon retro-style first-person shooter game  

---

## Project Overview

*Demons Dungeon* is a retro-style first-person shooter (FPS) game designed and developed as part of a Software Development module. 
The game draws inspiration from classic FPS titles such as *Doom* and *Wolfenstein 3D*, focusing on fast-paced gameplay, dungeon exploration, and combat against demonic enemies.  
The primary objective of this project is to design and implement a playable FPS prototype that demonstrates core game development concepts including player movement, weapon mechanics, enemy artificial intelligence (AI), level design, and rendering. 
The project utilises modern development tools while maintaining a retro aesthetic through low-resolution textures, pixelated visuals, and classic sound effects.  
This report documents the planning, design, implementation, testing, and evaluation of *Demons Dungeon* first-person shooter game. 

---

## 1. Introduction

First-person shooter games have remained one of the most popular genres in the video game industry due to their immersive gameplay and fast-paced mechanics. 
Retro-style FPS games, in particular, have seen renewed interest because of their simplicity, nostalgia, and focus on core gameplay mechanics.
The motivation behind *Demons Dungeon* is to recreate the feel of classic FPS games while applying modern software development practices. 

---

## User and System Requirements  

In this section user and system requirements are captured in the form of Scrum-style user stories and acceptance criteria.

---

## 1. User Requirements

User requirements describe the player's expectations and desired experiences.
For each of the user requirements below, a Scrum-style user story is provided along with specific acceptance criteria to ensure that the requirement is met effectively.
To define priorities, the MoSCoW method is used, categorising requirements as Must Have, Should Have, or Could Have based on their importance to the core gameplay experience.
The MoSCoW method is a simple, practical way to decide what really matters in a project—especially popular in software development projects when using Agile methodology.

### UR1 – Player Movement and Control
**Priority:** Must Have  

**Description:** Players must move freely through the dungeon using keyboard and mouse.

**Scrum Story:**  
> *As a player, I want to move, strafe, and aim smoothly using WASD keys and the mouse, so that I can react quickly to enemies and survive combat.*

**Acceptance Criteria:**
- Move forward, backward, and strafe using keyboard (WASD)
- Mouse controls camera rotation and aiming
- Smooth and responsive movement
- Controls explained in briefing screen

---

### UR2 – Combat and Shooting Mechanics
**Priority:** Must Have  

**Description:** Players must be able to shoot demons using a weapon to eliminate enemies and proceed through the game level.

**Scrum Story:**  
> *As a player, I want to shoot demons using a weapon, so that I can defend myself and clear the dungeon to get to the exit.*

**Acceptance Criteria:**
- Weapon fires on left mouse button click
- Enemies take damage and die when hit
- Visual and sound feedback confirms hits
- Ammo count shown on HUD

---

### UR3 – Health and Damage Feedback
**Priority:** Must Have  

**Description:** Players need clear feedback when taking damage and recovering health.

**Scrum Story:**  
> *As a player, I want to see my health decrease when I am hit and recover when safe, so that I can manage risk of losing the game and plan my actions.*

**Acceptance Criteria:**
- Health decreases when attacked
- Screen flashes red when damaged
- Health visible on HUD
- Health regenerates when no damage occurs

---

### UR4 – Enemy Behaviour and Challenge
**Priority:** Must Have  

**Description:** Enemies patrol game level and chase the player when detected.

**Scrum Story:**  
> *As a player, I want enemies to patrol game level and chase me when they see me, so that the game feels challenging and immersive.*

**Acceptance Criteria:**
- Enemies follow patrol paths
- Detect/'see' and chase player
- Multiple enemy types including boss demon

---

### UR5 – Game Progression and Win/Lose Conditions
**Priority:** Must Have  

**Description:** Clear win and lose conditions for the player.

**Scrum Story:**  
> *As a player, I want clear win and lose conditions, so that I understand my objective and outcome.*

**Acceptance Criteria:**
- Player loses when health = 0
- Player wins the game by defeating boss demon
- Game Over or Victory screen shown
- Score and stats displayed

---

### UR6 – User Interface and HUD
**Priority:** Should Have  

**Description:** Provide clear, informative UI and menus.

**Scrum Story:**  
> *As a player, I want a clear HUD and menu system, so that I can understand my status and navigate the game easily.*

**Acceptance Criteria:**
- Main menu: Start, Leaderboard, Credits, Exit
- HUD shows health, ammo, kills, score
- Briefing screen explains controls and objectives

---

### UR7 – Audio and Visual Feedback
**Priority:** Could Have  

**Description:** Audio and visual effects enhance immersion.

**Scrum Story:**  
> *As a player, I want sound effects and visual cues, so that combat and exploration feel immersive.*

**Acceptance Criteria:**
- Ambient dungeon music plays
- Sound effects on shooting, enemy death, damage
- Music changes during boss fights and victory

---

## 2. System Requirements

System requirements describe the **internal functionality** of the game.
Here again, in order to define priorities, the MoSCoW method is used, categorising requirements as Must Have, Should Have, or Could Have based on their importance.

### SR1 – Game Engine and Rendering
**Priority:** Must Have  

**Description:** Render 3D-like environment using raycasting algorithm.

**Scrum Story:**  
> *As a system, I must render dungeon walls and objects using a raycasting algorithm, so that the game appears as a retro 3D FPS.*

**Acceptance Criteria:**
- Raycasting renders walls and corridors
- Perspective changes with player rotation
- Stable rendering performance

---

### SR2 – Main Game Loop
**Priority:** Must Have  

**Description:** Continuously process input from control, game logic e.g. collision detection, enemies AI etc. and rendering updated screen.

**Scrum Story:**  
> *As a system, I must continuously process player input, game logic, and rendering, so that gameplay runs smoothly.*

**Acceptance Criteria:**
- Input captured from the control (keyboard and mouse) and processed correctly
- Game state updates correctly
- Rendering updates at a consistent frame rate

---

### SR3 – Enemy AI System
**Priority:** Must Have  

**Description:** Manage enemy AI states like patrol, chase, attack.

**Scrum Story:**  
> *As a system, I must manage enemy AI states, so that enemies behave realistically.*

**Acceptance Criteria:**
- Enemies patrol a certain area of the game level until detecting player
- Chase and attack on detection
- Boss demon has enhanced behavior

---

### SR4 – Collision Detection
**Priority:** Must Have  

**Description:** Prevent passing through walls and objects.

**Scrum Story:**  
> *As a system, I must detect collisions, so that movement and combat interactions are realistic.*

**Acceptance Criteria:**
- Player cannot move through walls
- Enemies respect level boundaries
- Projectiles register hits correctly

---

### SR5 – HUD and UI Rendering
**Priority:** Should Have  

**Description:** Render UI elements on top of gameplay.

**Scrum Story:**  
> *As a system, I must display HUD elements and menus, so that players receive real-time game information.*

**Acceptance Criteria:**
- HUD updates in real time
- Menus respond to input
- Smooth screen transitions

---

### SR6 – Audio System
**Priority:** Could Have  

**Description:** Manage background music and sound effects.

**Scrum Story:**  
> *As a system, I must play music and sound effects at appropriate times, so that the game feels immersive.*

**Acceptance Criteria:**
- Background music loops correctly and is played at the background
- Sound effects sync with actions (e.g. shooting, enemy death)
- Audio transitions for boss and victory states

---

## 3. Requirements Prioritisation Summary

| Priority | Description                                                                         |
|----------|-------------------------------------------------------------------------------------|
| **Must Have** | Core gameplay: movement, combat, AI, rendering, win/lose logic                      |
| **Should Have** | HUD, menus, UI polish, feedback                                                     |
| **Could Have** | Extra audio, collectibles, multiple weapons, leaderboard, more game levels designed |

---

