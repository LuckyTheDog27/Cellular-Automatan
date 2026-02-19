class cell:
    """
    Represents a single cell in the grid with a state and colour.
    
    Args:
        state: Boolean indicating whether the cell is active (True) or inactive (False)
        colour: Tuple of RGB values for the cell's colour
    """
    def __init__(self, state = False, colour=(255, 255, 255)):
        self.state = state
        self.colour = colour

class grid:
    """
    Represents the grid of cells for the cellular automaton.
    
    Args:
        width: Grid width in cells
        height: Grid height in cells
        cell_size: Size of each cell in pixels
    """
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size
        
        self.cell_grid = [[cell() for j in range(height)] for i in range(width)]
