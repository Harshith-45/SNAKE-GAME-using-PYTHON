import pygame
import time
import random
pygame.init()
width, height = 600, 400
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
block_size = 10
speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

def message(text, color):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, [width / 4, height / 4])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(black)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(green)

        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        for segment in snake:
            pygame.draw.rect(win, white, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length += 1

        clock.tick(speed)

    pygame.quit()

game_loop()
