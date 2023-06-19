import pygame
import pygame.mixer
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((620, 349)) # flags = pygame.NOFRAME - без рамки
pygame.display.set_caption("Игруля")    #название
icon = pygame.image.load('images/icon.png') # загрузка иконки   
pygame.display.set_icon(icon) # вывод иконки


bg = pygame.image.load('images/bg.png')
walk_left = [
    pygame.image.load('images/player_left/player_left_1.png'),
    pygame.image.load('images/player_left/player_left_2.png'),
    pygame.image.load('images/player_left/player_left_3.png'),
    pygame.image.load('images/player_left/player_left_4.png'),
]
walk_right = [
    pygame.image.load('images/player_right/player_right_1.png'),
    pygame.image.load('images/player_right/player_right_2.png'),
    pygame.image.load('images/player_right/player_right_3.png'),
    pygame.image.load('images/player_right/player_right_4.png'),
]


player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 7


#pygame.mixer.init()
#bg_sound = pygame.mixer.Sound('sounds/bg.mp3')  #музыка, которая не играет
#bg_sound.play(-1)

running = True
while running:

    screen.blit(bg, (bg_x, 0))#фон
    screen.blit(bg, (bg_x + 620, 0))

    keys = pygame.key.get_pressed() #передвижение
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    
    if keys[pygame.K_LEFT] and player_x > 50:#границы 
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed

    if not is_jump:# Прыжок
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7


    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2 # смена фона
    if bg_x  == -620:
        bg_x = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # крестик, чтоб выходить из игры
            running = False
            pygame.quit()

    clock.tick(10) # фреймы