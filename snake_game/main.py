import pygame

#The snake moves automatically.
#The player controls the snake using arrow keys (⬆️⬇️⬅️➡️).
#The snake eats food (red squares 🍎) to grow longer.
#If the snake hits the wall or itself, the game is over.

import random

#initialise game
pygame.init()

#gamesettings
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

#snake & food setup

snake = [(100, 100)]
snake_dir = (GRID_SIZE, 0)
food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)
    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check collision with food
    if new_head == food:
        food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    else:
        snake.pop()  # Remove tail if no food eaten

    # Check collisions (Wall & Self)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake[1:]):
        running = False  # Game over

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control speed (FPS)

pygame.quit()
