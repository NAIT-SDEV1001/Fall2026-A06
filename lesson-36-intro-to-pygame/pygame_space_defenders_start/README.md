# Introduction to Pygame - Space Defenders

## Why is this important?

So far every program we've written runs from top to bottom and then stops (or waits on a web request). Games work differently: they run a **game loop** that repeats many times a second, reading input, updating the world, and redrawing the screen.

Games are also a great place to see **classes and objects** pay off. Every ship, bullet and alien on the screen is an object with its own position and behaviour, built from a class.

In this lesson we'll use the **Pygame** package to build a small 2D shooter called Space Defenders.

## What are we going to do?

1. Install Pygame into a virtual environment.
2. Open a window and write a game loop.
3. Create a `Ship` class the player can move with the arrow keys.
4. Create a `Bullet` class and fire bullets with the space bar.
5. Create a fleet of `Alien` objects.
6. Detect collisions between bullets and aliens.

[pygame-ce Docs](https://pyga.me/docs/)

[Sprite and Group docs](https://pyga.me/docs/ref/sprite.html): the classes we use for game objects

[Rect docs](https://pyga.me/docs/ref/rect.html): positions, sizes and collisions

## Steps

### 1. Create a virtual environment and install Pygame

1. Create the virtual environment, and activate it:
```bash
python -m venv ./venv
.\venv\Scripts\activate # Or source ./venv/bin/activate on macOS/Linux
```
2. Install Pygame:
```bash
pip install pygame-ce
```
- `pygame-ce` (Community Edition) is the actively maintained version of Pygame. You still write `import pygame` in your code.
- We use it because the original `pygame` package does not have an installer for Python 3.14 on Windows yet, so `pip install pygame` fails.
3. Save the dependencies to a requirements file:
```bash
pip freeze > requirements.txt
```

### 2. Open a window and write the game loop

The `space_defenders.py` file already has some settings at the top. Using constants for settings means we can tweak the game in one place.

1. Add a `main` function below the settings:
```python
def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Defenders")
    clock = pygame.time.Clock()

    running = True
    while running:
        # 1. Handle events (input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update the game state (nothing yet)

        # 3. Draw everything
        screen.fill(BACKGROUND_COLOUR)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
```
2. Run it:
```bash
python space_defenders.py
```
- You should see an empty dark window. Close it with the X button.

What's going on:
- **The game loop** is the `while running:` loop. Every pass through it is one **frame**.
- Every frame does the same three things: **handle input, update, draw**.
- `pygame.event.get()` gives us everything that happened since the last frame (key presses, mouse clicks, the window closing).
- `screen.fill(...)` wipes the screen, then `pygame.display.flip()` shows what we drew.
- `clock.tick(FPS)` pauses just long enough to keep the game at 60 frames per second.
- Colours are `(red, green, blue)` tuples, each from 0 to 255.

### 3. Create the `Ship` class

Pygame's coordinate system starts at the **top-left** corner. `x` grows to the right and `y` grows **down**.

1. Add a `Ship` class above `main`:
```python
class Ship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((80, 220, 120))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20)
```
- `Ship` **inherits** from `pygame.sprite.Sprite`, the same idea as inheritance from Module 9.
- `self.image` is what the ship looks like (a green rectangle for now).
- `self.rect` is where the ship is and how big it is. `Rect` gives us handy positions like `midbottom`, `centerx`, `top`, `left` and `right`.

2. In `main`, create the ship before the loop and draw it each frame:
```python
    ship = Ship()

    running = True
    while running:
        # ... event handling ...

        # 3. Draw everything
        screen.fill(BACKGROUND_COLOUR)
        screen.blit(ship.image, ship.rect)
        pygame.display.flip()
```
- `screen.blit(image, rect)` draws an image at a position.

### 4. Move the ship with the arrow keys

1. Add an `update` method to `Ship`:
```python
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += SHIP_SPEED

        # Keep the ship on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
```
- `pygame.key.get_pressed()` tells us which keys are **held down** right now, so the ship keeps moving while you hold an arrow key.

2. Call it in the update section of the game loop:
```python
        # 2. Update the game state
        ship.update()
```

### 5. Fire bullets with the space bar

1. Add a `Bullet` class:
```python
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((255, 230, 90))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self) -> None:
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()  # removes the bullet from every group it is in
```
- Bullets move **up**, so we subtract from `y`.
- Once a bullet is off the top of the screen we `kill()` it. Otherwise we'd keep updating thousands of invisible bullets.

2. In `main`, create a **group** to hold the bullets:
```python
    ship = Ship()
    bullets = pygame.sprite.Group()
```
- A `Group` is like a list of sprites with superpowers: `bullets.update()` calls `update()` on every bullet, and `bullets.draw(screen)` draws them all.

3. Fire a bullet when space is pressed. Add this to the event loop:
```python
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
                    bullets.add(Bullet(ship.rect.centerx, ship.rect.top))
```
- `KEYDOWN` happens **once** per key press, which is what we want for firing. (Compare with `get_pressed()` for movement.)
- `MAX_BULLETS` stops players from just holding down fire.

4. Update and draw the bullets:
```python
        # 2. Update the game state
        ship.update()
        bullets.update()

        # 3. Draw everything
        screen.fill(BACKGROUND_COLOUR)
        screen.blit(ship.image, ship.rect)
        bullets.draw(screen)
        pygame.display.flip()
```

### 6. Create the alien fleet

1. Add an `Alien` class:
```python
class Alien(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill((230, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
```

2. Add a function that builds a grid of aliens, centred on the screen:
```python
def create_fleet() -> pygame.sprite.Group:
    aliens = pygame.sprite.Group()
    fleet_width = (ALIEN_COLUMNS - 1) * ALIEN_SPACING + 40
    left_margin = (SCREEN_WIDTH - fleet_width) // 2
    for row in range(ALIEN_ROWS):
        for column in range(ALIEN_COLUMNS):
            x = left_margin + column * ALIEN_SPACING
            y = 60 + row * 60
            aliens.add(Alien(x, y))
    return aliens
```
- This is the nested-loop pattern from Module 5: rows on the outside, columns on the inside.

3. In `main`, create the fleet and draw it:
```python
    ship = Ship()
    bullets = pygame.sprite.Group()
    aliens = create_fleet()

    # ... in the draw section ...
        aliens.draw(screen)
```

### 7. Detect collisions

1. After updating the bullets, check whether any bullet hit any alien:
```python
        # 2. Update the game state
        ship.update()
        bullets.update()
        pygame.sprite.groupcollide(bullets, aliens, True, True)

        if not aliens:
            aliens = create_fleet()
```
- `groupcollide` checks every bullet against every alien by comparing their `rect`s.
- The two `True`s mean "remove the bullet" and "remove the alien" when they collide.
- An empty group is falsy, so `if not aliens:` means "the whole fleet is gone". We make a new one.

2. Run the game. Move with the arrow keys and shoot with space.

## Exercises

1. Change the settings to make the ship faster, allow 5 bullets on screen, and add a fourth row of aliens.
2. Make the fleet move: every frame, move every alien right. When any alien touches the edge of the screen, move the whole fleet down 20 pixels and reverse direction. (Hint: store the direction in a variable, `1` for right and `-1` for left.)
3. Keep score: add 10 points for every alien destroyed and print the score in the terminal. (Hint: `groupcollide` returns a dictionary. What are its keys and values? Use `breakpoint()` to find out.)
4. **Challenge:** Show the score on the screen using `pygame.font.Font(None, 36)` and `font.render(...)`.

## Summary

In this lesson you learned how to:

- Install Pygame (`pygame-ce`) into a virtual environment.
- Write a game loop that handles input, updates the game, and draws each frame.
- Use classes that inherit from `pygame.sprite.Sprite` for game objects.
- Use `Rect` for positions and `Group` to update and draw many sprites at once.
- Tell the difference between held keys (`get_pressed`) and single key presses (`KEYDOWN`).
- Detect collisions with `groupcollide`.
