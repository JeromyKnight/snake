
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
S_WIDTH = 500
S_HEIGHT = 500

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Snake")

# Clock
clock = pygame.time.Clock()

# Snake
snake_block = 10
snake_list = []

# Score
score = 0

# Fonts
font_style = pygame.font.SysFont(None, 30)


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLUE, [x[0], x[1], snake_block, snake_block])


def score_system(score):
    value = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])


def generate_food():
    food_x = round(random.randrange(0, S_WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, S_HEIGHT - snake_block) / 10.0) * 10.0
    return food_x, food_y


def game_over():
    go_text = font_style.render("Game Over!", True, WHITE)
    screen.blit(go_text, [S_WIDTH/2 - go_text.get_width()/2, S_HEIGHT/2])


# Main game loop
game_exit = False
game_over_flag = False

x1 = S_WIDTH/2
y1 = S_HEIGHT/2
x1_change = 0
y1_change = 0

snake_list.append([x1, y1])
food_x, food_y = generate_food()

while not game_exit:

    while game_over_flag:
        screen.fill(BLACK)
        game_over()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_exit = True
                    game_over_flag = False
                if event.key == pygame.K_c:
                    x1 = S_WIDTH/2
                    y1 = S_HEIGHT/2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    snake_list.append([x1, y1])
                    food_x, food_y = generate_food()
                    score = 0
                    game_over_flag = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
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

    if x1 >= S_WIDTH or x1 < 0 or y1 >= S_HEIGHT or y1 < 0:
        game_over_flag = True

    x1 += x1_change
    y1 += y1_change

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)

    if len(snake_list) > score + 1:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over_flag = True

    draw_snake(snake_block, snake_list)
    score_system(score)

    pygame.display.update()

    if x1 == food_x and y1 == food_y:
        food_x, food_y = generate_food()
        score += 1

    clock.tick(20)

pygame.quit()
quit()
