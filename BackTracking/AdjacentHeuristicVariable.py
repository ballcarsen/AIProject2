import time
import math
from BackTracking.VariableInterface import VariableInterface

class AdjacentHeuristicVariable(VariableInterface):
    def __init__(self, _color, startCoor, endCoor):
        self.color = _color # character to indicate color e.g. R = red
        self.compareValue = 0
        self.startCoor = startCoor # list: [x, y]
        self.endCoor = endCoor

    # prioritize larger distance
    def __lt__(self, other):
        return self.compareValue > other.compareValue

    # implement heuristic hin this method
    def setCompareVal(self, bts):
        validAssignment = True
        startNode = bts.graphState.map[self.startCoor[1]][self.startCoor[0]]
        endNode = bts.graphState.map[self.endCoor[1]][self.endCoor[0]]
        startColNeighbors = self.getNumColoredNeighbors(startNode)
        endColNeighbors = self.getNumColoredNeighbors(endNode)
        if startColNeighbors >= 4:
            self.compareValue = 10
            #print("trapped start variable:", self.color)
            validAssignment = False
            #bts.graphState.printMap()
        elif endColNeighbors >= 4:
            self.compareValue = 10
            validAssignment = False
            #print("trapped end variable:", self.color)
            #bts.graphState.printMap()
        else:
            self.compareValue = self.getNumColoredNeighbors(startNode) + self.getNumColoredNeighbors(endNode)
        #print(self.compareValue)
        return validAssignment

    def getNumColoredNeighbors(self, node):
        numColoredNeighbors = 4 - len(node.neighbors)
        #print(numColoredNeighbors)
        #numColoredNeighbors = 0
        for neighbor in node.neighbors:
            if neighbor.char != '_':
                numColoredNeighbors += 1
        return numColoredNeighbors

    # def getManhattDist(self, point1, point2):
    #     deltaX = math.fabs(point1[0] - point2[0])
    #     deltaY = math.fabs(point1[1] - point2[1])
    #     return deltaX + deltaY