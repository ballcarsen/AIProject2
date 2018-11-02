from queue import PriorityQueue
from BackTracking.ConstrainedHeuristicVariable import ConstrainedHeuristicVariable
from BackTracking.SimpleVariable import SimpleVariable
from BackTracking.HeuristicPath import HeuristicPath
from BackTracking.SimplePath import SimplePath
from BackTracking.DistHeurisitcVariable import DistHeuristicVariable
import time

# note: in this csp, the "variables" are the connections that need to be made
# and the "values" are the paths that are assigned to those variables
class BackTrackingSearch:

    # the search takes in the initial state of the graph/map, and list of colored paths
    def __init__(self, _graphState, _colorCharacters, colorHeuristic, pathHeuristic):
        self.graphState = _graphState # map of paths
        self.colorCharacters = _colorCharacters # dictionary of colors and the start and end coordinates
        self.timeSpentFindingPaths = 0
        self.useVariableHeuristic = colorHeuristic
        self.usePathHeuristic = pathHeuristic
        print("variable (color choice) heuristic:", self.useVariableHeuristic)
        print("value (path choice) heuristic:", self.usePathHeuristic, "\n")
        self.numEdges = 0


    # wrapper method
    def startBacktrack(self):
        # priority queue of variables (connections) that need to be assigned
        # note: in basic backtrack, the ordering of the queue won't actually matter
        varPQ = PriorityQueue()
        # create variables and add them to the priority queue
        for color in self.colorCharacters.keys():
            if  self.useVariableHeuristic:
                var = ConstrainedHeuristicVariable(color, self.colorCharacters[color][0], self.colorCharacters[color][1])
            else:
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
            return True, varPQ
        # otherwise keep assigning variables
        var = varPQ.get()
        #print("****  on variable: ", var.color)

        # get all possible values (Paths) for the variable, ordered by some heuristic
        pathPQ = self.getOrderedValues(var)
        # while there are still values left to try
        while not pathPQ.empty():
            self.numEdges += 1
            path = pathPQ.get() # get path from PQ
            # if the path is valid, assign it to the graph
            self.assignPathToGraph(path)
            # also update variable priority queue based on new graph state (if using heuristic)
            varPQ = self.updateVarPQ(varPQ)
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
        return False, varPQ


    # update priority queue for variables given the current self.graphState
    def updateVarPQ(self, oldPQ):
        #return oldPQ
        #print("old queue length: ", oldPQ.qsize())
        newPQ = PriorityQueue()
        while oldPQ.empty() == False:
            var = oldPQ.get()
            # this will update the compare values in other priority queues as well, we might want to make new vars as well
            # im not sure how this will effect it.
            var.setCompareVal(self)
            newPQ.put(var)
        #print("new queue length: ", newPQ.qsize())
        return newPQ


    def assignPathToGraph(self, path):
        for position in path.coordList:
            self.graphState.map[position[1]][position[0]].char = path.pathColor


    def removePathFromGraph(self, path):
        for position in path.coordList[1:-1]:
            self.graphState.map[position[1]][position[0]].char = '_'

    # returns a boolean
    def pathIsValid(self, path):
        pass
        # TODO: check path validity against the self.graphState


    # returns a PriorityQueue of Paths
    def getOrderedValues(self, var):
        pathPQ = PriorityQueue()
        startNode = self.graphState.map[var.startCoor[1]][var.startCoor[0]]
        endNode = self.graphState.map[var.endCoor[1]][var.endCoor[0]]
        self.findPath(startNode, [var.startCoor], endNode, pathPQ)
        return pathPQ

    def printGraphState(self):
        self.graphState.printMap()
        # TODO: method for printing state of graph

    def findPath(self, node, path, goal, pqRef):

        #print("exploring %d %d" % (node.xCoor, node.yCoor))
        #print('length %d' % len(node.neighbors))
        for neighbor in node.neighbors:
            valid = 0
            position = (neighbor.xCoor, neighbor.yCoor)
            #print(position)
            #print(neighbor.char)
            if position == (goal.xCoor, goal.yCoor):
                #print('goal')
                path.append((goal.xCoor, goal.yCoor))
                #print('found full path')
                #print(path)
                if(self.usePathHeuristic):
                    p = HeuristicPath(goal.char, path)
                else:
                    p = SimplePath(goal.char, path)
                pqRef.put(p)
            else:
                if neighbor.char == '_' and (neighbor.xCoor, neighbor.yCoor) not in path:
                    copy = []
                    # If the neighbor is the start node
                    if (neighbor.xCoor, neighbor.yCoor) == path[0]:
                        valid += 1
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

                    # TODO check and make sure it wont go zig zag with end node too

                    if valid < 2:
                        #print('valid, path so far')

                        copy.append(position)
                        #print(copy)
                        self.findPath(neighbor, copy, goal, pqRef)