---
theme: ./nait-theme-test
title: Slidev Theme Starter
layout: nait-main-cover
---
# SDEV 1001

## Programming Fundamentals
<br/>
<br/>

## Packages and virtual environments - 7
---

# Expectations - What I expect from you
<br/>

## - No Late Assignments
<br/>

## - No Cheating
<br/>

## - Be a good classmate
<br/>

## - Don't waste your time
<br/>

## - Show up to class
<br/>

---
layout: two-cols
---

# Agenda

On the right is what we will cover today.

::right::


#### What is Pygame?
#### Is Python Good for Games?
#### Setup: pygame-ce
#### The Game Loop
#### Coordinates and Colours
#### Sprites and Rects
#### Groups
#### Held Keys vs Key Presses
#### Collisions
#### Space Defenders Example
#### Exercises
#### Summary

---

## What is Pygame?

- A package for making **2D games** in Python.
- Handles the hard parts for us:
  - Opening a window and drawing to it.
  - Reading the keyboard and mouse.
  - Timing, images, sound and collisions.
- Games are a great fit for **classes and objects**: every ship, bullet and alien is an object.

---

## Is Python Good for Games?

- Great for **learning** and **prototyping** game ideas quickly.
- Most commercial games use faster languages and engines:
  - **C++**: Unreal Engine, most AAA games.
  - **C#**: Unity, Godot (also supports C#).
- The concepts you learn today (game loop, sprites, collisions) carry over to every engine.

---

## Setup: pygame-ce

1. **Create + activate a virtual environment:**
   ```
   python -m venv ./venv
   .\venv\Scripts\activate
   ```
2. **Install Pygame Community Edition:**
   ```
   pip install pygame-ce
   ```
3. **Run the game:**
   ```
   python space_defenders.py
   ```
- `pygame-ce` is the actively maintained fork. You still `import pygame`.
- The original `pygame` package won't install on Python 3.14 yet.

---

## The Game Loop

- A game is a loop that runs **every frame** (60 times a second):
   ```python
   running = True
   while running:
       # 1. Handle events (input)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False

       # 2. Update the game state

       # 3. Draw everything
       screen.fill(BACKGROUND_COLOUR)
       pygame.display.flip()

       clock.tick(FPS)
   ```
- **Input → Update → Draw**, over and over.

---

## Coordinates and Colours

- `(0, 0)` is the **top-left** corner of the window.
- `x` grows to the **right**, `y` grows **down**.
  - Moving up means **subtracting** from `y`.
- Colours are `(red, green, blue)` tuples from 0 to 255:
   ```python
   BACKGROUND_COLOUR = (15, 15, 35)   # dark blue
   (80, 220, 120)                     # green
   (230, 80, 80)                      # red
   ```

---

## Sprites and Rects

- A **Sprite** is a game object. We inherit from `pygame.sprite.Sprite`.
- `image` is what it looks like, `rect` is where it is and how big.
   ```python
   class Ship(pygame.sprite.Sprite):
       def __init__(self) -> None:
           super().__init__()
           self.image = pygame.Surface((60, 20))
           self.image.fill((80, 220, 120))
           self.rect = self.image.get_rect()
           self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20)
   ```
- `Rect` has handy positions: `x`, `y`, `top`, `left`, `right`, `centerx`, `midbottom`...

---

## Groups

- A `pygame.sprite.Group` holds many sprites.
   ```python
   bullets = pygame.sprite.Group()
   bullets.add(Bullet(ship.rect.centerx, ship.rect.top))

   bullets.update()        # calls update() on every bullet
   bullets.draw(screen)    # draws every bullet
   ```
- `sprite.kill()` removes a sprite from all of its groups.
- An empty group is falsy: `if not aliens:` means "no aliens left".

---

## Held Keys vs Key Presses

- **Held keys**: smooth movement while a key is down.
   ```python
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:
       self.rect.x -= SHIP_SPEED
   ```
- **Key presses**: happen **once** each time a key goes down.
   ```python
   for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               ...  # fire one bullet
   ```

---

## Collisions

- Two objects collide when their `rect`s overlap.
- `groupcollide` checks every sprite in one group against every sprite in another:
   ```python
   pygame.sprite.groupcollide(bullets, aliens, True, True)
   ```
- The two `True`s: remove the bullet, remove the alien.
- It returns a **dictionary**: `{bullet: [aliens it hit]}`.

---

## Space Defenders Example

- Follow along in `pygame_space_defenders_start/README.md`:
  1. Open a window with a game loop.
  2. Add a `Ship` and move it.
  3. Fire `Bullet`s with space.
  4. Build a fleet of `Alien`s.
  5. Destroy aliens with collisions.

---

## Exercises

1. Tweak the settings: faster ship, 5 bullets, a fourth row of aliens.
2. Make the fleet move side to side and drop down at the edges.
3. Add 10 points per alien and print the score.
4. **Challenge:** draw the score on the screen with `pygame.font`.

---

## Summary

- You learned how to:
  - Install `pygame-ce` into a virtual environment.
  - Write a game loop: input, update, draw.
  - Use `Sprite`, `Rect` and `Group` for game objects.
  - Tell held keys from single key presses.
  - Detect collisions with `groupcollide`.
- Next class: finish the game. Moving fleet, score, and game over.
- Read **Chapter 13: Aliens!** in *Python Crash Course*.
