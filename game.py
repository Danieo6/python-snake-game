'''
######################################
# Python Snake Game using PyGame     #
# Author: Daniel Budziński           #
# 2019                               #
######################################
'''
import sys
import pygame
import random

#Initialize PyGame
pygame.init()

#Setup game window
window = width, height = 480, 480
background = 255, 255, 255

screen = pygame.display.set_mode(window)
pygame.display.set_caption("Python Snake")
clock = pygame.time.Clock()

#Game variable setup
snake_x = 0
snake_y = 0
direction_x = 0
direction_y = 0
snake_positions = [(0, 0)]
points = 0
food_present = False
gameover = False

#Game loop
while True:
    clock.tick(3)
    print(gameover)
    #Listen to events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        #If a WSAD key is pressed, change the snake direction
        elif event.type == pygame.KEYDOWN:
            if(not gameover):
                if event.key == pygame.K_w:
                    direction_x = 0
                    direction_y = -1
                elif event.key == pygame.K_d:
                    direction_x = 1
                    direction_y = 0
                elif event.key == pygame.K_s:
                    direction_x = 0
                    direction_y = 1
                elif event.key == pygame.K_a:
                    direction_x = -1
                    direction_y = 0
            else:
                #Restart the game
                if(event.key == pygame.K_r):
                    snake_x = 0
                    snake_y = 0
                    direction_x = 0
                    direction_y = 0
                    snake_positions = [(0, 0)]
                    points = 0
                    food_present = False
                    gameover = False
    
    #Move the snake
    if(not gameover):
        snake_x += direction_x*48
        snake_y += direction_y*48

    #Generate position for food
    if(food_present == False):
        food_x = random.randrange(0, 10)*48
        food_y = random.randrange(0, 10)*48
        food_present = True

    #Check for snake-food collision
    if(snake_x == food_x and snake_y == food_y):
        food_present = False
        points += 1
    
    #Check for snake-snake collision
    if( (snake_x, snake_y) in snake_positions and len(snake_positions) > 1):
        direction_x = 0
        direction_y = 0
        gameover = True

    #Check for game over
    if(snake_x > 480 or snake_x < 0 or snake_y > 480 or snake_y < 0):
        direction_x = 0
        direction_y = 0
        gameover = True

    #Clear play ground
    screen.fill(background)
    #Remember snake position
    snake_positions.append((snake_x, snake_y))

    #Draw food
    pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(food_x, food_y, 48, 48))
    #Move and draw the snake
    if(not gameover):
        i = 0
        while i <= points:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snake_positions[len(snake_positions)-(1+i)][0], snake_positions[len(snake_positions)-(1+i)][1], 48, 48))
            i += 1
    #Clear unnecessary items from the list
    if(len(snake_positions) > points):
        snake_positions.pop(0)
    #Draw points counter
    font = pygame.font.SysFont("Arial", 28)
    score_counter = font.render("Points: %s" % points, True, (0, 100, 255))
    screen.blit(score_counter, (10, 10))
    #Draw game over sign
    if(gameover):
        gameover_sign = font.render("Game Over! Press 'R' to restart", True, (255, 50, 50))
        screen.blit(gameover_sign, (240 - gameover_sign.get_width() // 2, 240 - gameover_sign.get_height() // 2))
    #Update screen
    pygame.display.update()