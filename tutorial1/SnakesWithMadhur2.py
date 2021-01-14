import pygame
import random
import  os
pygame.init()

# specific variables

screen_width = 900
screen_height = 500




font = pygame.font.SysFont(None, 45)
clock = pygame.time.Clock()
fps = 30

# COLORS

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


# interface of game

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeRevision")
pygame.display.update()


def screen_text(text, color, x, y):
    text_screen = font.render(text, True, color)
    game_window.blit(text_screen, [x, y])


def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# game loop


def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(white)
        screen_text("welcome to snakes", black, 150, 100)
        screen_text("press space to play", black, 120, 130)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()


def game_loop():
    exit_game = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    snake_x = 55
    snake_y = 75
    score = 0
    snake_length = 0
    if (not os.path.exists("hyscore.txt")):
        with open("hyscore.txt", "w") as f:
            f.write("0")
    with open("hyscore.txt") as f:
        hyscore = f.read()
    food_x = random.randint(20, 800)
    food_y = random.randint(20, 400)
    snake_size = 25
    snake_list = []

    while not exit_game:
        if game_over:
            with open("hyscore.txt", "w") as f:
                f.write(str(hyscore))
            game_window.fill(white)
            screen_text("game over press enter to continue", red, 100, 150)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame. KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame. K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame. K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                    if event.key == pygame. K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    
            snake_x += velocity_x
            snake_y += velocity_y
            game_window.fill(white)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            game_window.fill(white)
            if snake_y > screen_height or snake_y < 0 or snake_x < 0 or snake_x > screen_width:
                game_over = True

            plot_snake(game_window, black, snake_list, snake_size)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                food_x = random.randint(20, 800)
                food_y = random.randint(20, 400)
                score += 10
                snake_length += 4
                if score > int(hyscore):
                    hyscore = score

            screen_text("Score: " + str(score) +"  "+ "Hyscore: "+ str(hyscore), red, 35, 15)
            clock.tick(30)
            pygame.display.update()

    pygame.quit()
    quit()

welcome()