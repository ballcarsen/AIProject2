from queue import PriorityQueue
from BackTracking.ConstrainedHeuristicVariable import ConstrainedHeuristicVariable
from BackTracking.SimpleVariable import SimpleVariable
from BackTracking.HeuristicPath import HeuristicPath
from BackTracking.SimplePath import SimplePath
from BackTracking.AdjacentHeuristicVariable import AdjacentHeuristicVariable

from enum import Enum

class VarHeuristicType(Enum):
    NONE = 0
    MOSTCONSTRAINED = 1
    ADJACENTCOLORS = 2


# note: in this csp, the "variables" are the connections that need to be made
# and the "values" are the paths that are assigned to those variables
class BackTrackingSearch:

    # the search takes in the initial state of the graph/map, and list of colored paths
    def __init__(self, _graphState, _colorCharacters, colorHeuristic, pathHeuristic):
        self.graphState = _graphState # map of paths
        self.colorCharacters = _colorCharacters # dictionary of colors and the start and end coordinates
        self.timeSpentFindingPaths = 0
        self.colorHeuristic = colorHeuristic
        self.usePathHeuristic = pathHeuristic
        print("variable (color choice) heuristic:", self.colorHeuristic)
        print("value (path choice) heuristic:", self.usePathHeuristic, "\n")
        self.numEdges = 0
        self.pathsFound = 0


    # wrapper method
    def startBacktrack(self):
        # priority queue of variables (connections) that need to be assigned
        # note: in basic backtrack, the ordering of the queue won't actually matter
        varPQ = PriorityQueue()
        # create variables and add them to the priority queue
        for color in self.colorCharacters.keys():
            var = None
            if  self.colorHeuristic == VarHeuristicType.ADJACENTCOLORS:
                var = AdjacentHeuristicVariable(color, self.colorCharacters[color][0], self.colorCharacters[color][1])
            elif self.colorHeuristic == VarHeuristicType.MOSTCONSTRAINED:
                var = ConstrainedHeuristicVariable(color, self.colorCharacters[color][0], self.colorCharacters[color][1])
            elif self.colorHeuristic == VarHeuristicType.NONE:
                var = SimpleVariable(color, self.colorCharacters[color][0], self.colorCharacters[color][1])

            var.setCompareVal(self) # this is where a heuristic could order the queue
            varPQ.put(var)
        # start the backtrack algorithm
        self.recursiveBacktrack(varPQ)


    # returns a boolean
    def recursiveBacktrack(self, varPQ):

        #print("var pq length: ", varPQ.qsize())
        # base case: if we've assigned every variable, then return true
        if varPQ.empty():
            #print("*** finished!")
            if not self.graphState.hasBlankSpots():
                return True, varPQ
            else:
                return False, varPQ
        # otherwise keep assigning variables
        var = varPQ.get()

        # get all possible values (Paths) for the variable, ordered by some heuristic
        pathPQ = self.getOrderedValues(var)
        # while there are still values left to try
        while not pathPQ.empty():
            self.numEdges += 1
            path = pathPQ.get() # get path from PQ
            # if the path is valid, assign it to the graph
            self.assignPathToGraph(path)
            # also update variable priority queue based on new graph state (if using heuristic)
            varPQ, viableBranch = self.updateVarPQ(varPQ)
            if viableBranch:
                # recursively call this method to see if it reaches the base case (a solution)
                viableBranch, varPQ = self.recursiveBacktrack(varPQ)
            # if solution was found, keep returning true
            if viableBranch:
                return True, varPQ
            else:
                # remove path if it's not part of a viable solution
                self.removePathFromGraph(path)
        # if no viable branches were found, return false
        varPQ.put(var)
        #print("no paths found")
        return False, varPQ


    # update priority queue for variables given the current self.graphState
    def updateVarPQ(self, oldPQ):
        validAssignment = True
        newPQ = PriorityQueue()
        while oldPQ.empty() == False:
            var = oldPQ.get()
            valid = var.setCompareVal(self)
            if not valid:
                validAssignment = False
            newPQ.put(var)
        return newPQ, validAssignment


    def assignPathToGraph(self, path):
        for position in path.coordList:
            self.graphState.map[position[1]][position[0]].char = path.pathColor


    def removePathFromGraph(self, path):
        for position in path.coordList[1:-1]:
            self.graphState.map[position[1]][position[0]].char = '_'


    # returns a PriorityQueue of Paths
    def getOrderedValues(self, var):
        pathPQ = PriorityQueue()
        startNode = self.graphState.map[var.startCoor[1]][var.startCoor[0]]
        endNode = self.graphState.map[var.endCoor[1]][var.endCoor[0]]
        self.findPath(startNode, [var.startCoor], endNode, pathPQ, 0)
        return pathPQ

    def printGraphState(self):
        self.graphState.printMap()
        # TODO: method for printing state of graph

    def findPath(self, node, path, goal, pqRef, pathLength):
        if pathLength > 40:
           return
        neighbor_coordinates = [(neighbor.xCoor, neighbor.yCoor) for neighbor in node.neighbors]
        # If one of the neighbors is the goal, return the path, all other neighbors will result in invalid paths
        if (goal.xCoor, goal.yCoor) in neighbor_coordinates:
            path.append((goal.xCoor, goal.yCoor))
            if (self.usePathHeuristic):
                p = HeuristicPath(goal.char, path)
            else:
                p = SimplePath(goal.char, path)
            pqRef.put(p)
        elif len(path) < 40:
            # Traverse the neighbors
            for neighbor in node.neighbors:
                valid = 0
                position = (neighbor.xCoor, neighbor.yCoor)
                if neighbor.char == '_' and (neighbor.xCoor, neighbor.yCoor) not in path:

                    copy = []
                    # If the neighbor is the start node
                    for coordinate in path:
                        if(coordinate == (neighbor.xCoor - 1, neighbor.yCoor)):
                            valid += 1
                        if (coordinate == (neighbor.xCoor + 1, neighbor.yCoor)):
                            valid += 1
                        if (coordinate == (neighbor.xCoor, neighbor.yCoor - 1)):
                            valid += 1
                        if (coordinate == (neighbor.xCoor, neighbor.yCoor + 1)):
                            valid += 1
                        copy.append(coordinate)
                    # Adding the neighbor to the path will not result in an invalid path so far
                    if valid < 2:
                        copy.append(position)
                        #print(copy)
                        self.findPath(neighbor, copy, goal, pqRef, pathLength + 1)