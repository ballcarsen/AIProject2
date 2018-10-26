from BackTracking.Node import Node
class Map:
    def __init__(self, mapArr):
        self.map = mapArr

    def addNeighbors(self):
        for row in self.map:
            for node in row:
                # add neighbors
                x = node.xCoor
                y = node.yCoor

                # if we are not using the coordinates of the center node, and it's in bounds, and it's not a wall
                # then add it's neighbor to it
                i = y
                j = x - 1
                if (i >= 0 and j >= 0 and i < len(self.map) and j < len(row)):
                    node.addNeighbor(self.map[i][j])
                i = y
                j = x + 1
                if (i >= 0 and j >= 0 and i < len(self.map) and j < len(row)):
                    node.addNeighbor(self.map[i][j])
                i = y - 1
                j = x
                if (i >= 0 and j >= 0 and i < len(self.map) and j < len(row)):
                    node.addNeighbor(self.map[i][j])
                i = y + 1
                j = x
                if (i >= 0 and j >= 0 and i < len(self.map) and j < len(row)):
                    node.addNeighbor(self.map[i][j])

    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()