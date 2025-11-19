import pygame
from time import sleep
from random import randint

pygame.init()
screen=pygame.display.set_mode((601,601))
pygame.display.set_caption("PINK SNAKE")
running = True

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
PINK = (255,0,255)
GREEN = (0,200,0)
clock = pygame.time.Clock()

snake=[[5,6],[5,7]]
direction = "right"
pausing = False
apple=[randint(0,19),randint(0,19)]
score=0
font_small = pygame.font.SysFont("Arial",20)
font_big = pygame.font.SysFont("Arial",30)

screen.fill(WHITE)
pygame.display.flip()
title_txt = font_small.render("WELCOME TO PINK SNAKE", True, PINK)
screen.blit(title_txt, (120, 200))
title_txt = font_small.render("GET READY", True, PINK)
screen.blit(title_txt, (120, 250))
pygame.display.flip()
pygame.time.delay(3000)

screen.fill(BLACK)
pygame.display.flip()



while running:
    clock.tick(60)
    screen.fill(BLACK)
    tail_x = snake[0][0]
    tail_y = snake[0][1]

    #Grid
    for i in range(21):
        pygame.draw.line(screen,WHITE,(0,i*30),(600,i*30))
        pygame.draw.line(screen,WHITE,(i*30,0),(i*30,600))
    #Snake
    for block in snake:
        pygame.draw.rect(screen,PINK,(block[0]*30,(block[1]*30),30,30))
    # Score
        score_txt = font_big.render("SCORE: " + str(score), True, WHITE)
        screen.blit(score_txt, (5, 5))
    #Apple
    pygame.draw.rect(screen,RED, (apple[0]*30, apple[1]*30, 30, 30))

    if snake[-1][0] == apple[0] and snake[-1][1] == apple[1]:
        snake.insert(0,[tail_x, tail_y])
        apple = [randint(0, 19), randint(0, 19)]
        score+=1



    #Move
    if pausing==False:
        if direction == "right":
            snake.append([snake[-1][0] + 1, snake[-1][1]])
            snake.pop(0)
        if direction == "left":
                snake.append([snake[-1][0] - 1, snake[-1][1]])
                snake.pop(0)
        if direction == "up":
            snake.append([snake[-1][0], snake[-1][1]-1])
            snake.pop(0)
        if direction == "down":
            snake.append([snake[-1][0], snake[-1][1]+1])
            snake.pop(0)
    sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE and pausing==True:
                pausing=False
                snake = [[5, 6], [5, 7]]
                apple = [randint(0, 19), randint(0, 19)]
                score = 0
    # Check crash with body
    for i in range(len(snake) - 1):
        if snake[-1][0] == snake[i][0] and snake[-1][1] == snake[i][1]:
            pausing = True
    # Check crash with edge
    if snake[-1][0] < 0 or snake[-1][0] >19 or snake[-1][1] < 0 or snake[-1][1] > 19:
        pausing = True
    #Game over
    if pausing==True:
        print("Game Over")
        game_over_txt = font_big.render("GAME OVER!", True, WHITE)
        game_score_txt = font_big.render("SCORE: " + str(score), True, WHITE)
        game_space_txt = font_big.render("PRESS SPACE TO CONTINUE", True, WHITE)
        screen.blit(game_over_txt, (30, 200))
        screen.blit(game_score_txt, (30, 250))
        screen.blit(game_space_txt, (30, 300))

    pygame.display.flip()
pygame.quit()