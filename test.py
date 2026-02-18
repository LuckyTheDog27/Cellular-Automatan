from random import randint
import pygame
import cell

cell_grid = []

screen_width = 700
screen_height = 700

cell_size = 5


grid_width = screen_width // cell_size
grid_height = screen_height // cell_size




def random_grid():
    for i in range(grid_width):
        cell_grid.append([])
        for j in range(grid_height):
            cell_grid[i].append(cell.cell(i, j, bool(randint(0,10) == 10)))

def empty_grid():
    for i in range(grid_width):
        cell_grid.append([])
        for j in range(grid_height):
            cell_grid[i].append(cell.cell(i, j, False))

random_grid()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

running = True

def print_grid():
    screen.fill((0, 0, 0))
    for i in range(grid_width):
        for j in range(grid_height):
            if cell_grid[i][j].state:
                pygame.draw.rect(screen, (255, 255, 255), (i*cell_size, j*cell_size, cell_size, cell_size))
    pygame.display.flip()

def game_of_life():
    ALIVE = True

    buffer = [[False for j in range(grid_height)] for i in range(grid_width)]

    for i in range(grid_width):
        for j in range(grid_height):

            neighbors = 0
        
            for x_offset in range(-1, 2): # -1, 0, 1
                for y_offset in range(-1, 2):
                    if x_offset == 0 and y_offset == 0:
                        continue
                    if i + x_offset < 0 or i + x_offset >= grid_width or j + y_offset < 0 or j + y_offset >= grid_height:
                        continue
                    if cell_grid[i + x_offset][j + y_offset].state == ALIVE:
                        neighbors += 1
            

            if (neighbors == 3 or (cell_grid[i][j].state == ALIVE and neighbors == 2)):
                buffer[i][j] = ALIVE
            else:
                buffer[i][j] = False

    for i in range(grid_width):
        for j in range(grid_height):
            cell_grid[i][j].state = buffer[i][j]

            
    

while running:
    print_grid()
    game_of_life()
    # wait_time = 100
    # pygame.time.wait(wait_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    