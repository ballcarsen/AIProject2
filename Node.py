class Node:
    def __init__(self,char,yCoor,xCoor):
        # Character at the position in the map
        self.char = char
        # X coordinate of the position in the maze
        self.xCoor = xCoor
        # Y coordinate of the position in the maze
        self.yCoor = yCoor
        # List of the references to the nodes neighbors
        self.neighbors = []

    # Adds reference to neighbor node
    def addNeighbor(self, newNeighbor):
        self.neighbors.append(newNeighbor)

