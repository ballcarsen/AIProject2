import time
import math
from BackTracking.VariableInterface import VariableInterface

class DistHeuristicVariable(VariableInterface):
    def __init__(self, _color, startCoor, endCoor):
        self.color = _color # character to indicate color e.g. R = red
        self.compareValue = self.getManhattDist(startCoor, endCoor) # value to compare different variables for ordering search
        self.startCoor = startCoor # list: [x, y]
        self.endCoor = endCoor

    # prioritize larger distance
    def __lt__(self, other):
        return self.compareValue < other.compareValue

    # implement heuristic hin this method
    def setCompareVal(self, bts):
        pass

    def getManhattDist(self, point1, point2):
        deltaX = math.fabs(point1[0] - point2[0])
        deltaY = math.fabs(point1[1] - point2[1])
        return deltaX + deltaY