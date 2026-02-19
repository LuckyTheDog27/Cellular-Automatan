from random import randint
import colour_spread
import pygame
import elements


def random_grid(width, height, cell_size):
    """Create a grid with randomly initialized cells.
    
    Args:
        width: Grid width in cells
        height: Grid height in cells
        cell_size: Size of each cell in pixels
    
    Returns:
        A grid object with randomly populated cells
    """
    grid = elements.grid(width, height, cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            grid.cell_grid[i][j] = elements.cell(state=bool(randint(0,10) == 10))
    return grid

def empty_grid(width, height, cell_size):
    """Create an empty grid with no initialized cells.
    
    Args:
        width: Grid width in cells
        height: Grid height in cells
        cell_size: Size of each cell in pixels
    
    Returns:
        An empty grid object
    """
    return elements.grid(width, height, cell_size)

def print_grid(grid, screen):
    """Render the grid to the pygame display.
    
    Args:
        grid: The grid object to render
        screen: The pygame display surface
    """
    screen.fill((0, 0, 0))
    for i in range(grid.width):
        for j in range(grid.height):
            if grid.cell_grid[i][j].state:
                pygame.draw.rect(screen, grid.cell_grid[i][j].colour, (i*grid.cell_size, j*grid.cell_size, grid.cell_size, grid.cell_size))
    pygame.display.flip()
    

def game_of_life(grid):
    """Apply Conway's Game of Life rules to the grid.
    
    Args:
        grid: The grid to apply the Game of Life rules to

    Returns:
        A new grid with updated cell states after applying the Game of Life rules
    """
    ALIVE = True

    new_grid = elements.grid(grid.width, grid.height, grid.cell_size)

    for i in range(grid.width):
        for j in range(grid.height):

            neighbors = 0
        
            for x_offset in range(-1, 2):
                for y_offset in range(-1, 2):
                    if x_offset == 0 and y_offset == 0:
                        continue
                    if i + x_offset < 0 or i + x_offset >= grid.width or j + y_offset < 0 or j + y_offset >= grid.height:
                        continue
                    if grid.cell_grid[i + x_offset][j + y_offset].state == ALIVE:
                        neighbors += 1
            

            if (neighbors == 3 or (grid.cell_grid[i][j].state == ALIVE and neighbors == 2)):
                new_grid.cell_grid[i][j].state = ALIVE
                new_grid.cell_grid[i][j].colour = grid.cell_grid[i][j].colour

    return new_grid







if __name__ == "__main__":
    running = True
    main_grid = random_grid(100, 100, 5)
    pygame.init()
    screen = pygame.display.set_mode((main_grid.screen_width, main_grid.screen_height))
    print_grid(main_grid, screen)

    while running:
        print_grid(main_grid, screen)
        main_grid = game_of_life(main_grid)
        wait_time = 100
        pygame.time.wait(wait_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    