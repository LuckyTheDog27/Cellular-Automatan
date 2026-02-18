from random import randint
import pygame
import cell

cell_grid = []

grid_width = 40
grid_height = 30

cell_size = 10

for i in range(grid_width):
    cell_grid.append([])
    for j in range(grid_height):
        cell_grid[i].append(cell.cell(i, j, bool(randint(0,10) == 10)))

pygame.init()
screen = pygame.display.set_mode((400, 300))

running = True

def print_grid():
    for i in range(grid_width):
        for j in range(grid_height):
            if cell_grid[i][j].state:
                pygame.draw.rect(screen, (255, 255, 255), (i*cell_size, j*cell_size, cell_size, cell_size))
    
    pygame.display.flip()

def rules():
    ...

while running:
    print_grid()
    rules()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    