import pygame
import random
pygame.init()

# Colors
White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)

# Screen Interface
screen_height = 600
screen_width = 900
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SnakeGame With Madhur")
pygame.display.update()

# Game Specific Variables
exit_game = False
game_over = False
init_velocity = 5
velocity_x = 0
velocity_y = 0
snake_x = 45
snake_y = 55
snake_size = 25
food_x = random.randint(20, 800)
food_y = random.randint(20, 500)
fps = 60
score = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Creating Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score = score + 1
        print("Score: ", score*10)

        food_x = random.randint(80, screen_width / 2)
        food_y = random.randint(80, screen_height / 2)
    gameWindow.fill(White)
    text_screen("Score:" + str(score * 10), Red, 5, 5)
    pygame.draw.rect(gameWindow, Red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, Black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()