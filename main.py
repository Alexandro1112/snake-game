import random
import pygame
import re

snake_blocks = [[0, 0]]
size = 15
margin = 9
count_blocks = 25
W = count_blocks * (size + margin) + size * 2
H = count_blocks * (size + margin) + 100 + size
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.init()
BLACK = (155, 55, 50)
count = 0
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FRAME_COLOR = (0, 255, 100)
BLUE = (204, 255, 255)

s_col = 0
s_row = 0
ds_row = 1
ds_col = 0
x = random.randint(0, size)
y = random.randint(0, size)
x_ = random.randint(0, size)
y_ = random.randint(0, size)


def get_record():
    with open('record', 'r') as f:
        record = f.read()
        if count > int(record.replace(',', '')[-1]):
            with open('record', 'a') as _f_:
                _f_.write(str(str(count) + str(",")))
        else:
            ...
    return record.split(',')

def draw_block(color, c, r):
    x = size + c * size + margin * (c + 1)
    y = 100 + r * size + margin * (r + 1)
    pygame.draw.rect(screen, color, (x, y, size, size))



while True:

    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ds_row != 1:
                ds_row = -1
                ds_col = 0
            elif event.key == pygame.K_DOWN and ds_row != -1:
                ds_row = 1
                ds_col = 0
            elif event.key == pygame.K_LEFT and ds_col != 1:
                ds_row = 0
                ds_col = -1
            elif event.key == pygame.K_RIGHT and ds_col != -1:
                ds_row = 0
                ds_col = 1

    screen.fill(BLACK)
    for row in range(count_blocks):
        for col in range(count_blocks):
            if (row + col) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color, col, row)

    s_col += ds_col
    s_row += ds_row
    draw_block(RED, s_col, s_row)
    for i in snake_blocks:
        draw_block(RED, i[0], i[-1])
    del snake_blocks[0]
    snake_blocks.append([s_col, s_row])
    draw_block(GREEN, x, y)
    x_ = random.randint(0, size)
    y_ = random.randint(0, size)


    if s_col == x and s_row == y:
        count += 1

        x = random.randint(0, size)
        y = random.randint(0, size)

        snake_blocks.append([-190, -30])

    if s_col > 24 or s_row > 24 or s_col < 0 or s_row < 0:
        get_record()
        quit()
    for i in range(len(snake_blocks) - 1):
        if snake_blocks[i] == snake_blocks[-1]:
            get_record()
            quit()

    font = pygame.font.Font('WOOPPECKER.ttf', 30).render(
        f'Score {count}', True, (100, 180, 90)
    )
    font_ = pygame.font.Font('WOOPPECKER.ttf', 30).render(
        f'Record {max(get_record())}', True, (100, 180, 90)
    )

    screen.blit(font, (10, 50))
    screen.blit(font_, (200, 50))

    pygame.display.update()

