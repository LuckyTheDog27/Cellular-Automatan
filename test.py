from random import randint
import pygame
import elements


def random_grid(width, height, cell_size):
    grid = elements.grid(width, height, cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            grid.cell_grid[i][j] = elements.cell(i, j, bool(randint(0,10) == 10))
    return grid

def empty_grid(width, height, cell_size):
    return elements.grid(width, height, cell_size)

def print_grid(grid, screen):
    screen.fill((0, 0, 0))
    for i in range(grid.width):
        for j in range(grid.height):
            if grid.cell_grid[i][j].state:
                pygame.draw.rect(screen, (255, 255, 255), (i*grid.cell_size, j*grid.cell_size, grid.cell_size, grid.cell_size))
    pygame.display.flip()

def game_of_life(grid):
    ALIVE = True

    buffer = [[False for j in range(grid.height)] for i in range(grid.width)]

    for i in range(grid.width):
        for j in range(grid.height):

            neighbors = 0
        
            for x_offset in range(-1, 2): # -1, 0, 1
                for y_offset in range(-1, 2):
                    if x_offset == 0 and y_offset == 0:
                        continue
                    if i + x_offset < 0 or i + x_offset >= grid.width or j + y_offset < 0 or j + y_offset >= grid.height:
                        continue
                    if grid.cell_grid[i + x_offset][j + y_offset].state == ALIVE:
                        neighbors += 1
            

            if (neighbors == 3 or (grid.cell_grid[i][j].state == ALIVE and neighbors == 2)):
                buffer[i][j] = ALIVE


    for i in range(grid.width):
        for j in range(grid.height):
            grid.cell_grid[i][j].state = buffer[i][j]








running = True

main_grid = random_grid(100, 100, 5)
second_grid = empty_grid(100, 100, 5)

pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode((main_grid.screen_width, main_grid.screen_height))

while running:
    print_grid(main_grid, screen)
    game_of_life(main_grid)
    # wait_time = 100
    # pygame.time.wait(wait_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    