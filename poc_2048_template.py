"""
Clone of 2048 game.
"""

import poc_2048_gui
from random import randint

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

def liner(line):
    """Align non zeroes to the left."""
    res = [0] * len(line)
    counter = 0
    for elem in line:
        if elem != 0:
            res[counter] = elem
            counter += 1
    return res

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    if len(line) == 1:
       return line
    line = liner(line)
    res = []
    zeroes = []
    while (len(line) > 1):
        elem = line.pop(0)
        if elem == line[0]:
            res.append(elem*2)
            zeroes.append(0)
            line.pop(0)
        else:
            res.append(elem)

    return res + line + zeroes


class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.row = grid_height
        self.col = grid_width
        self.grid = []
        self.reset()
        self.initial = {1: [(0, x) for x in range(self.col)],
                        2: [(self.row-1, x) for x in range(self.col)],
                        3: [(x, 0) for x in range(self.row)],
                        4: [(x, self.col-1) for x in range(self.row)]}
    
    def test(self, dummy):
        """
        Insert dummy grid for testing 
        """
        self.grid = dummy

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        for dummy_elem in range(self.row):
            self.grid.append([0] * self.col)
            
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self.string_grid = ''
        for elem in self.grid:
            self.string_grid += (str(elem) + '\n')
        return self.string_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.row
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.col
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tiles = self.initial[direction]
        row_offset = OFFSETS[direction][0]
        col_offset = OFFSETS[direction][1]
        rows = tiles[0][0]
        cols = tiles[0][1]
        outloop = self.col
        if direction == 3:
            outloop = self.row
        for row in range(outloop):
            outer += 1  # DEBUG
            line = []
            inloop = self.row
            if direction in [3, 4]:
                inloop = self.col
            for count in range(inloop): 
                temprow = rows + (count * row_offset)
                tempcol = cols + (count * col_offset)
                print temprow, tempcol
                inner += 1  # DEBUG
                line.append(self.get_tile(temprow, tempcol))
            inner = 0
            res = merge(line)
            print res, line
            for elem in res:
                self.set_tile(rows, cols, elem)

                if direction == 1:
                    rows += 1
                elif direction == 2:
                    rows -= 1
                elif direction == 3:
                    cols += 1
                elif direction == 4:
                    cols -= 1
            if direction in [3,4]:
                rows += 1 
                cols = tiles[0][1]
            else:
                cols += 1
                rows = tiles[0][0]
            if row == self.row and direction in [1]:
                break
            if row == self.row-1 and direction in [4]:
                break

        self.new_tile() 

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        allpos = [(x,y) for x in range(self.row) for y in range(self.col)]
        available = False
        for apos, bpos in allpos:
            if self.get_tile(apos, bpos) == 0:
                available = True
        if not available:
            return
        newvalue = randint(1, 10)
        if newvalue !=9:
            newvalue = 2
        else:
            newvalue = 4
        random_row_pos = randint(0, self.row - 1)
        random_col_pos = randint(0, self.col - 1)
        if self.get_tile(random_row_pos, random_col_pos) != 0:
            self.new_tile()
        else:
            self.set_tile(random_row_pos, random_col_pos, newvalue)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

