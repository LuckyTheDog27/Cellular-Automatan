import elements
import random

def colour_grid_random(width=100, height=100, cell_size=5, fill_chance=0.5):
    """
    Creates a grid with randomly populated cells and random colours.
    
    Args:
        width: Width of the grid in cells
        height: Height of the grid in cells
        cell_size: Size of each cell in pixels
        fill_chance: Probability that a cell is initially active (between 0 and 1)
    
    Returns:
        A grid object with randomly populated cells and random colours
    """
    grid = elements.grid(width, height, cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            grid.cell_grid[i][j] = elements.cell(state=bool(random.random() < fill_chance), colour=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return grid

def colour_grid_random_fill(width=100, height=100, cell_size=5):
    """
    Creates a grid with all cells populated and random colours.
    
    Args:
        width: Width of the grid in cells
        height: Height of the grid in cells
        cell_size: Size of each cell in pixels
    
    Returns:
        A grid object with all cells populated with random colours
    """
    grid = elements.grid(width, height, cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            grid.cell_grid[i][j] = elements.cell(state=True, colour=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return grid

def colour_grid_corners(width=100, height=100, cell_size=5):
    """
    Creates a grid with populated cells at the corners and random colours.
    
    Args:
        width: Width of the grid in cells
        height: Height of the grid in cells
        cell_size: Size of each cell in pixels
    
    Returns:
        A grid object with only the corner cells populated with random colours
    """
    grid = elements.grid(width, height, cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            if (i == 0 and j == 0) or (i == grid.width - 1 and j == 0) or (i == 0 and j == grid.height - 1) or (i == grid.width - 1 and j == grid.height - 1):
                grid.cell_grid[i][j] = elements.cell(state=True, colour=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            else:
                grid.cell_grid[i][j] = elements.cell(state=False, colour=(0, 0, 0))
    return grid
    

def spread_colour(grid: elements.grid):
    """
    Spreads colours from active cells to inactive neighboring cells.
    
    For each inactive cell, averages the colours of all active neighbors.
    If neighbors exist, the cell becomes active with the averaged colour.
    
    Active cells retain their original colour.
    
    Args:
        grid: The grid to apply colour spreading to
    
    Returns:
        A new grid with updated cell states and colours after spreading
    """
    new_grid = elements.grid(grid.width, grid.height, grid.cell_size)
    for i in range(grid.width):
        for j in range(grid.height):
            if not grid.cell_grid[i][j].state:
                new_colour = (0, 0, 0)
                colour_count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (i + x >= 0 and i + x < grid.width) and (j + y >= 0 and j + y < grid.height):
                            if grid.cell_grid[i + x][j + y].state:
                                new_colour = tuple(map(lambda a, b: a + b, new_colour, grid.cell_grid[i + x][j + y].colour))
                                colour_count += 1
                if colour_count > 0:
                    new_colour = tuple(map(lambda a: a // colour_count, new_colour))
                    new_grid.cell_grid[i][j] = elements.cell(state=True, colour=new_colour)
            else:
                new_grid.cell_grid[i][j] = elements.cell(state=True, colour=grid.cell_grid[i][j].colour)
    return new_grid