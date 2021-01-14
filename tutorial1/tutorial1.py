import pygame
pygame.init()
# Creating Window Screen
gameWindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("My First Game")

# Game Specific Variable
exit_game = False
game_over = False

# Creating a Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You Pressed Right Key")


# Quiting the game
pygame.quit()
quit()
