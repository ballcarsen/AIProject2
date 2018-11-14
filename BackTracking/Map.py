import matplotlib.pyplot as plt
import numpy as np
colorDict = {
    "D": [189, 183,107],
    "B": [0,0,255],
    "O":[139,37,0],
    "K": [205,193,197],
    "R":[255, 0, 0],
    "Q":[135,206,255],
    "P":[93,71,139],
    "Y":[255,255,0],
    "G":[0,100,0],
    "A":[138,51,36],
    "W":[255,20,147],
    "_":[255, 255, 255]
    }

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

    def hasBlankSpots(self):
        for row in self.map:
            for node in row:
                if node.char == '_':
                    return True
        return False
    def printColorMap(self):
        x = []
        y = []
        color = []
        for row in self.map:
            for node in row:
                x.append(node.xCoor)
                y.append(-node.yCoor)
                color.append(colorDict[node.char])
        x = np.array(x)
        y = np.array(y)
        color = np.array(color)
        # to make a side by side comparison we set the boundaries and aspect
        # of the second plot to mimic imshow's


        # and finally plot the data --- the size of dots `s=900` was by trial and error
        plt.scatter(x, y, s=900, c=color/255)
        plt.show()