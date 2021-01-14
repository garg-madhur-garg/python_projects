import pygame
import random
import os
pygame.init()

# Color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


font = pygame.font.SysFont(None, 45)
clock = pygame.time.Clock()

# Functions


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Interface of screen
screen_width = 900
screen_height = 500

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeWithMadhur")


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snakes", black, 260, 180)
        text_screen("Press SpaceBar to Continue", black, 220, 210)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()


# Game loop
def game_loop():

    # Specific variables in game
    snake_length = 1
    snake_list = []
    exit_game = False
    game_over = False
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt") as f:
        hiscore = f.read()

    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 60
    food_x = random.randint(50, 800)
    food_y = random.randint(50, 400)
    score = 0

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("game over! press enter to continue", red, 150, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 6
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -6
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -6
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 6
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            gameWindow.fill(white)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            plot_snake(gameWindow, black, snake_list, snake_size)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                food_x = random.randint(50, 800)
                food_y = random.randint(50, 400)
                score = score + 10
                snake_length = snake_length + 5
                if score > int(hiscore):
                    hiscore = score

            text_screen("Score:" + str(score) + "  " + "Hiscore" + str(hiscore), red, 20, 20)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
