import pygame
import random
import os
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# variables
screen_width = 800
screen_height = 600

font = pygame.font.SysFont("comicsansms", 25, True)


clock = pygame.time.Clock()


# functions


def screen_text(text, color, x, y):
    text_screen = font.render(text, True, color)
    gamewindow.blit(text_screen, [x, y])


def plot_snake(gamewindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


# game interface

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# game loop


def game_loop():

    snake_x = 80
    snake_y = 80
    snake_size = 25
    velocity_x = 0
    velocity_y = 0
    snake_length = 0
    snake_list = []
    score = 0
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w")as f:
            f.write("0")

    with open("highscore.txt")as f:
         highscore = f.read()
    exit_game = False
    game_over = False
    food_x = random.randint(100, 700)
    food_y = random.randint(100, 500)

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w")as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            screen_text("Game Over\nPress Enter to continue..", black, 150, 250 )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 9
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -9
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -9
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 9
                        velocity_x = 0
            snake_x += velocity_x
            snake_y += velocity_y

            gamewindow.fill(white)

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            plot_snake(gamewindow, black, snake_list, snake_size)
            pygame.draw.rect(gamewindow, red, (food_x, food_y, snake_size, snake_size))
            screen_text(f"Score: {score}  Highscore: {highscore}", red, 30, 30)

            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10:
                food_x = random.randint(100, 700)
                food_y = random.randint(100, 500)
                score = score + 10
                snake_length += 4
                if score > int(highscore):
                    highscore = score

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True

            clock.tick(30)
            pygame.display.update()

    pygame.quit()
    quit()

game_loop()
