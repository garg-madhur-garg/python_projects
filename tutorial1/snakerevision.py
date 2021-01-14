import pygame
import random
pygame.init()


# Colors
white =(255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Specific Game Variables

exit_game = False
game_over = False
screen_width = 900
screen_height = 500
snake_x = 45
snake_y = 55
food_x = random.randint(20, 700)
food_y = random.randint(20, 400)
snake_size = 20
velocity_x = 0
velocity_y = 0
clock = pygame.time.Clock()
fps = 30

# Interface of Screen
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeRevision")
pygame.display.update()


# Game Loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0
            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0
    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x-food_x) < 6 or abs(snake_y-food_y) < 6:
        food_x = random.randint(20, 700)
        food_y = random.randint(20, 400)
    game_window.fill(white)
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
