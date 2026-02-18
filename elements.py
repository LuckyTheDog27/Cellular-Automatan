class cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

class grid:
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size
        
        self.cell_grid = [[cell(i, j, False) for j in range(height)] for i in range(width)]
