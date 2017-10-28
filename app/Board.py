from BoardEntityEnum import BoardEntityEnum
from itertools import product

# Holds objects in a width x height 2D array
class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[BoardEntityEnum.EMPTY for x in range(height)] for y in range(width)]

    # Returns true if the xpos is in the width boundary
    def __xInbounds(self, xpos):
        return True if 0 < xpos <= (self.width - 1) else False

    # Returns true if the ypos is in the height boundary
    def __yInBounds(self, ypos):
        return True if 0 < ypos <= (self.height - 1) else False

    # Returns true if a tile (x,y) is in bounds
    def tileInBounds(self, tile):
        return True if (self.__xInbounds(tile[0]) and self.__yInBounds(tile[1])) else False

    # Adds an entity to tile (x,y) if it is in bounds
    def insert(self, tile, entity):
        if self.tileInBounds(tile):
            self.tiles[tile[0]][tile[1]] = entity

    # Casts the board to a String
    def __str__(self):
        divider = " --- " * self.width + "\n"
        return divider + "".join(
            ["".join(
                ["| " + self.tiles[i][j].value + " |" for i in range(self.width)]
            ) + "\n" + divider for j in range(self.height)]
        )