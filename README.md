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

### 1. User Requirements

User requirements describe the player's expectations and desired experiences.
For each of the user requirements below, a Scrum-style user story is provided along with specific acceptance criteria to ensure that the requirement is met effectively.
To define priorities, the MoSCoW method is used, categorising requirements as Must Have, Should Have, or Could Have based on their importance to the core gameplay experience.
The MoSCoW method is a simple, practical way to decide what really matters in a project—especially popular in software development projects when using Agile methodology.

#### UR1 – Player Movement and Control
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

#### UR2 – Combat and Shooting Mechanics
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

#### UR3 – Health and Damage Feedback
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

#### UR4 – Enemy Behaviour and Challenge
**Priority:** Must Have  

**Description:** Enemies patrol game level and chase the player when detected.

**Scrum Story:**  
> *As a player, I want enemies to patrol game level and chase me when they see me, so that the game feels challenging and immersive.*

**Acceptance Criteria:**
- Enemies follow patrol paths
- Detect/'see' and chase player
- Multiple enemy types including boss demon

---

#### UR5 – Game Progression and Win/Lose Conditions
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

#### UR6 – User Interface and HUD
**Priority:** Should Have  

**Description:** Provide clear, informative UI and menus.

**Scrum Story:**  
> *As a player, I want a clear HUD and menu system, so that I can understand my status and navigate the game easily.*

**Acceptance Criteria:**
- Main menu: Start, Leaderboard, Credits, Exit
- HUD shows health, ammo, kills, score
- Briefing screen explains controls and objectives

---

#### UR7 – Audio and Visual Feedback
**Priority:** Could Have  

**Description:** Audio and visual effects enhance immersion.

**Scrum Story:**  
> *As a player, I want sound effects and visual cues, so that combat and exploration feel immersive.*

**Acceptance Criteria:**
- Ambient dungeon music plays
- Sound effects on shooting, enemy death, damage
- Music changes during boss fights and victory

---

### 2. System Requirements

System requirements describe the **internal functionality** of the game.
Here again, in order to define priorities, the MoSCoW method is used, categorising requirements as Must Have, Should Have, or Could Have based on their importance.

#### SR1 – Game Engine and Rendering
**Priority:** Must Have  

**Description:** Render 3D-like environment using raycasting algorithm.

**Scrum Story:**  
> *As a system, I must render dungeon walls and objects using a raycasting algorithm, so that the game appears as a retro 3D FPS.*

**Acceptance Criteria:**
- Raycasting renders walls and corridors
- Perspective changes with player rotation
- Stable rendering performance

---

#### SR2 – Main Game Loop
**Priority:** Must Have  

**Description:** Continuously process input from control, game logic e.g. collision detection, enemies AI etc. and rendering updated screen.

**Scrum Story:**  
> *As a system, I must continuously process player input, game logic, and rendering, so that gameplay runs smoothly.*

**Acceptance Criteria:**
- Input captured from the control (keyboard and mouse) and processed correctly
- Game state updates correctly
- Rendering updates at a consistent frame rate

---

#### SR3 – Enemy AI System
**Priority:** Must Have  

**Description:** Manage enemy AI states like patrol, chase, attack.

**Scrum Story:**  
> *As a system, I must manage enemy AI states, so that enemies behave realistically.*

**Acceptance Criteria:**
- Enemies patrol a certain area of the game level until detecting player
- Chase and attack on detection
- Boss demon has enhanced behavior

---

#### SR4 – Collision Detection
**Priority:** Must Have  

**Description:** Prevent passing through walls and objects.

**Scrum Story:**  
> *As a system, I must detect collisions, so that movement and combat interactions are realistic.*

**Acceptance Criteria:**
- Player cannot move through walls
- Enemies respect level boundaries
- Projectiles register hits correctly

---

#### SR5 – HUD and UI Rendering
**Priority:** Should Have  

**Description:** Render UI elements on top of gameplay.

**Scrum Story:**  
> *As a system, I must display HUD elements and menus, so that players receive real-time game information.*

**Acceptance Criteria:**
- HUD updates in real time
- Menus respond to input
- Smooth screen transitions

---

#### SR6 – Audio System
**Priority:** Could Have  

**Description:** Manage background music and sound effects.

**Scrum Story:**  
> *As a system, I must play music and sound effects at appropriate times, so that the game feels immersive.*

**Acceptance Criteria:**
- Background music loops correctly and is played at the background
- Sound effects sync with actions (e.g. shooting, enemy death)
- Audio transitions for boss and victory states

---

### 3. Requirements Prioritisation Summary

| Priority | Description                                                                         |
|----------|-------------------------------------------------------------------------------------|
| **Must Have** | Core gameplay: movement, combat, AI, rendering, win/lose logic                      |
| **Should Have** | HUD, menus, UI polish, feedback                                                     |
| **Could Have** | Extra audio, collectibles, multiple weapons, leaderboard, more game levels designed |

---

## Scrum-style backlog

In this section Scrum-style product backlog is created based on the user and system requirements defined above.
The product backlog is organised into a set of epics and user stories with associated definition of done / acceptance criteria.
Each user story is assigned a priority and estimated story points to help with sprint planning and development focus.
One story point is equivalent to approximately 3 hours of work for a developer, and the total story points for each epic can help in estimating the overall effort required for that epic.

### Epic 1: Game Core Architecture

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                                                                                                                        |
| --- | --- | --- | --- |--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EPIC 1 | Game Core Architecture | As a developer, I want to create the main game loop structure so that the game can update, render, and respond to user input in real time. | High | 16           | - Game initializes successfully and remains stable. <br/>- Game loop runs >60 FPS without crashing. <br/>- ESC exits cleanly. <br/>Tests: Launch game, verify loop, FPS monitor output, check memory leak logs. |
| US 1.1 | Input System | As a player, I want to control movement with WASD keys and shooting with the mouse. | High | 8            | - Player moves forward/backward, strafes left/right. <br/>- Mouse input triggers shooting sound and animation. <br/>Tests: Press each control; <br/>verify response on-screen.                                  |
| US 1.2 | Collision Detection | As a player, I shouldn’t walk through walls or objects. | High | 5            | - Player stops when colliding with wall tiles. <br/>- No clipping through level geometry.                                                                                                                       |
| US 1.3 | Game Menu | As a user, I want a menu to start new games, view credits, and quit. | Medium | 3            | - Menu buttons functional. <br/>- Navigation intuitive.                                                                                                                                                              |

### Epic 2: Rendering & Visual System (Raycasting)

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                                                                                             |
| --- | --- | --- | --- |--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EPIC 2 | Rendering & Visual System (Raycasting) | As a player, I want a retro 3D feel via raycasting visuals for immersion. | High | 8            | - Basic walls rendered using raycasting. <br/>- Movement alters perspective dynamically. <br/>Tests: Verify wall perspective with player rotation; <br/>check performance stability. |
| US 2.1 | Dungeon Level Rendering | As a player, I want a dungeon labyrinth rendered where I can walk and explore. | High | 8            | - Map correctly loads from file. <br/>- Player spawns at “S” location. <br/>- Textures displayed consistently.                                                                            |

### Epic 3: Enemy AI & Combat System

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                                                |
| --- | --- | --- | --- |--------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| EPIC 3 | Enemy AI & Combat System | As a player, I want to fight enemies that move, see, and chase me. | High | 8            | - Enemies patrol and chase when player in sight. <br/>- Combat mechanics functional (attack, damage, kill).                             |
| US 3.1 | Demon Patrol AI | As a player, I want demons to patrol corridors realistically. | High | 3            | - Pathfinding limited to patrol sector. <br/>- Patrol route random or predefined.                                                       |
| US 3.2 | Chase & Combat Behavior | As a player, I want demons to detect and attack me when I’m visible. | High | 3            | - Detection radius system. <br/>- Enemy moves toward player, attacks reduce health. <br/>Tests: Step into enemy view; <br/>observe chase/attack logic. |
| US 3.3 | Boss-Demon Encounter | As a player, I want an end-level boss that’s harder to defeat. | Medium | 2            | - Special “victory” event triggers upon boss defeat.                                                                                    |

### Epic 4: Player HUD & Stats

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                         |
| --- | --- | --- | --- |--------------|--------------------------------------------------------------------------------------------------|
| EPIC 4 | Player HUD & Stats | As a player, I want to see my current health, ammo, and score. | High | 8            | - HUD appears during gameplay. <br/>- Updates dynamically when stats change.                          |
| US 4.1 | Health System | As a player, my health should decrease when hit and slowly auto-recover. | High | 3            | - Implement health regeneration rate. <br/>- Death triggers Game Over screen.                         |
| US 4.2 | Ammo System | As a player, I want ammo tracking to add tactical challenge. | Medium | 3            | - Ammo count decreases when firing. <br/>- Reload/top-up mechanics functional if time permits.        |
| US 4.3 | Kill Counter / Score | As a player, I want scoring for defeating enemies. | Medium | 2            | - Each kill adds to counter and total points. <br/>Tests: Kill 3 enemies, UI should show +3 increase. |

### Epic 5: Sound & Feedback Mechanics

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                                                |
| --- | --- | --- | --- |--------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| EPIC 5 | Sound & Feedback Mechanics | As a player, I want immersive sound and visual feedback for hits and kills. | Medium | 4            | - Sound effects for shooting, hits, enemy death. <br/>- Visual flash (screen reddens) when hit. <br/>Tests: Take damage; <br/>verify red overlay. |

### Epic 6: Game Flow & Win/Lose Conditions

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                     |
| --- | --- | --- | --- |--------------|----------------------------------------------------------------------------------------------|
| EPIC 6 | Game Flow & Win/Lose Conditions | As a player, I want clear winning/losing outcomes based on my performance. | High | 4            | - Win screen upon killing boss. <br/>- Game Over when health = 0. <br/>- Restart options in menu. |

### Epic 7: User Interface & Screens

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                  |
| --- | --- | --- | --- |--------------|-------------------------------------------------------------------------------------------|
| EPIC 7 | User Interface & Screens | As a player, I want polished UI screens for each game phase. | Medium | 7            | - Menu, HUD, Game Over and Victory screens functional. <br/>- Style cohesive with retro theme. |

### Epic 8: Level Design

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                              |
| --- | --- | --- | --- |--------------|-------------------------------------------------------------------------------------------------------|
| EPIC 8 | Level Design | As a developer, I want a functional maze level to demonstrate core gameplay. | High | 9            | - One level designed and implemented with enemies, boss, and exit. <br/>- Player can fully traverse level. |

### Epic 9: Asset Integration

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                    |
| --- | --- | --- | --- |--------------|-------------------------------------------------------------------------------------------------------------|
| EPIC 9 | Asset Integration | As a developer, I want to integrate sprites, textures, and ambient effects for atmosphere. | Medium | 10           | - Demon sprites animated. <br/>- Dungeon textures consistent. <br/>- Ambient lighting and horror sound complete. |

### Epic 10: Testing & Optimization

| ID | Feature / Epic | User Story | Priority | Story Points | Definition of Done / Acceptance Criteria                                                                                                                                                             |
| --- | --- | --- | --- |--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EPIC 10 | Testing & Optimization | As a developer, I need to test frame rate, AI, collision, and gameplay. | High | 6            | - Minimum 60 FPS across system. <br/>- No crash after 10 mins gameplay. <br/>- All UI elements update properly. <br/>Tests: Gameplay diagnostics report; <br/>FPS counter logs; <br/>AI behavior test cases manual. |

---

### Sprint Planning

Based on the above product backlog, the development can be organised into sprints, with each sprint focusing on a specific set of features or epics.
The sprint planning is designed to ensure that core gameplay mechanics are developed first, followed by additional features and polish in later sprints.
Each sprint is estimated to last 1 week, allowing for focused development and testing of the assigned features.
The sprint 5 is going to end on 17.03.2026 as the deadline for the project is set for 20.03.2026.

| Sprint   | Goals                                                                                           | Focused Features |
|----------|-------------------------------------------------------------------------------------------------|------------------|
| Sprint 1 | Game loop setup, input system                                                                   | EPIC 1           |
| Sprint 2 | Raycasting visual engine, <br/>Enemy AI & basic combat                                          | EPIC 2, 3        |
| Sprint 3 | HUD, health, and scoring, <br/>Sound & Feedback Mechanics, <br/>Game Flow & Win/Lose Conditions | EPIC 4, 5, 6     |
| Sprint 4 | User Interface & Screens, <br/>Level Design                                                     | EPIC 7 & 8       |
| Sprint 5 | Asset Integration, <br/>Testing & Optimization                                       | EPIC 9 & 10      |

---

## Testing

In this section, test cases are defined to verify the functionality of the game based on the user and system requirements.
The test cases cover various aspects of the game, including player movement, combat mechanics, enemy behavior, health system, win/lose conditions, rendering, HUD updates, audio feedback, and performance. 
Each test case includes a unique ID, a description of the test, preconditions that must be met before executing the test, and the expected outcome to determine if the test passes or fails.
Below is a first stab at the test cases for the game and more can be added as the development progresses and new features are implemented.

| Test Case ID | Description                           | Precondition | Expected Outcome                                    |
| --- |---------------------------------------| --- |-----------------------------------------------------|
| TC-01 | Verify player can move with WASD      | Game started | Player moves and stops correctly on key presses     |
| TC-02 | Verify shooting functionality         | Weapon equipped | Gun fires, muzzle sound plays, ammo reduces         |
| TC-03 | Verify demon chase behavior           | Player enters detection radius | Demon moves toward player, attacks                  |
| TC-04 | Verify health decrease and regenerate | Player hit by enemy | Health decreases, then slowly regenerates over time |
| TC-05 | Verify win condition                  | Boss defeated | Exit door unlocks, victory screen shown             |
| TC-06 | Verify lose condition                 | Health reaches 0 | Game Over screen displayed                          |
| TC-07 | Verify raycasting view rendering      | Game started | Dungeon walls visible with proper perspective       |
| TC-08 | Verify HUD update                     | Health or ammo changes | HUD updates in real time                            |
| TC-09 | Verify ambient music & sound          | Game active | Horror ambient and sound effects play correctly     |
| TC-10 | Verify FPS performance                | Game running > 5 min | FPS ≥ 60, no freeze or crash                        |