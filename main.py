import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 533

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shooter")

screen_fill_color = (32, 52, 71)

background = pygame.image.load('images/background.jpg')

FIGHTER_STEP = 5  
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = fighter_x + fighter_width / 2 - rocket_width / 2 - rocket_width / 2, fighter_y - rocket_height
rocket_was_fired = False

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
        
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    screen.fill(screen_fill_color)
    screen.blit(background, (0, 0))
    screen.blit(fighter_image, (fighter_x, fighter_y))

    pygame.display.update()
    clock.tick(60)  
