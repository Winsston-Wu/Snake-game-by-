import pygame
import sys
import random
import time


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇-By Winston Wu')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)
ROYALBLUE= (65,105,225)

snake_block = 10
snake_speed = 15


snake_list = []
snake_length = 1


x1 = WIDTH / 2
y1 = HEIGHT / 2

x1_change = 0
y1_change = 0


foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0


def show_start_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont('arial', 35)
    text = font.render('Snake Game', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    screen.blit(text, text_rect)

    text = font.render('Press any key to start', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text, text_rect)


    credit_font = pygame.font.SysFont('arial', 20)
    credit_text = credit_font.render('By Winston Wu', True, LIGHT_BLUE)
    credit_rect = credit_text.get_rect(topleft=(10, 10))
    screen.blit(credit_text, credit_rect)

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def show_game_over_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont('arial', 35)
    text = font.render('Game Over', True, RED)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    screen.blit(text, text_rect)

    text = font.render('Press Q to Quit or R to Restart', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text, text_rect)


    credit_font = pygame.font.SysFont('arial', 20)
    credit_text = credit_font.render('By Winston Wu', True, LIGHT_BLUE)
    credit_rect = credit_text.get_rect(topleft=(10, 10))
    screen.blit(credit_text, credit_rect)

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting = False


game_over = False
show_start_screen()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0


    x1 += x1_change
    y1 += y1_change
    screen.fill(BLACK)


    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        game_over = True
        show_game_over_screen()
        game_over = False
        snake_list = []
        snake_length = 1
        x1 = WIDTH / 2
        y1 = HEIGHT / 2
        foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
        continue


    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True
            show_game_over_screen()
            game_over = False
            snake_list = []
            snake_length = 1
            x1 = WIDTH / 2
            y1 = HEIGHT / 2
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            continue


    pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])


    for segment in snake_list:
        pygame.draw.rect(screen, ROYALBLUE, [segment[0], segment[1], snake_block, snake_block])


    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
        snake_length += 1

    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)

pygame.quit()
sys.exit()
