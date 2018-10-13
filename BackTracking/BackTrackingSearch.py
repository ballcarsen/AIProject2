from queue import PriorityQueue
from BackTracking.Variable import Variable


# note: in this csp, the "variables" are the connections that need to be made
# and the "values" are the paths that are assigned to those variables
class BackTrackingSearch:

    # the search takes in the initial state of the graph/map, and list of colored paths
    def __init__(self, _graphState, _colorCharacters):
        self.graphState = _graphState # map of paths
        self.colorCharacters = _colorCharacters # list of strings


    # wrapper method
    def startBacktrack(self):
        # priority queue of variables (connections) that need to be assigned
        # note: in basic backtrack, the ordering of the queue won't actually matter
        varPQ = PriorityQueue()
        # create variables and add them to the priority queue
        for color in self.colorCharacters:
            var = Variable(color)
            var.setCompareVal(self.graphState) # this is where a heuristic could order the queue
            varPQ.put(var)
        # start the backtrack algorithm
        self.recursiveBacktrack(varPQ)


    # returns a boolean
    def recursiveBacktrack(self, varPQ):
        # base case: if we've assigned every variable, then return true
        if varPQ.empty():
            return True
        # otherwise keep assigning variables
        var = varPQ.get()
        # get all possible values (Paths) for the variable, ordered by some heuristic
        pathPQ = self.getOrderedValues(var)
        # while there are still values left to try
        while not pathPQ.empty():
            path = pathPQ.get() # get path from PQ
            # if the path is valid, assign it to the graph
            if(self.pathIsValid(path)):
                self.assignPathToGraph(path)
                # also update variable priority queue based on new graph state (if using heuristic)
                varPQ = self.updateVarPQ(varPQ)
                # recursively call this method to see if it reaches the base case (a solution)
                viableBranch = self.recursiveBacktrack(varPQ)
                # if solution was found, keep returning true
                if viableBranch:
                    return True
                else:
                    # remove path if it's not part of a viable solution
                    self.removePathFromGraph()
        # if no viable branches were found, return false
        return False


    # update priority queue for variables given the current self.graphState
    def updateVarPQ(self, oldPQ):
        newPQ = PriorityQueue()
        for var in oldPQ:
            var.setCompareVal(self.graphState)
            newPQ.put(var)
        return newPQ


    def assignPathToGraph(self, path):
        pass
        # TODO: draws given path on self.graphState

    def removePathFromGraph(self):
        pass
        # TODO: remove path from self.graphState


    # returns a boolean
    def pathIsValid(self, path):
        pass
        # TODO: check path validity against the self.graphState


    # returns a PriorityQueue of Paths
    def getOrderedValues(self, var):
        pathPQ = PriorityQueue()
        # TODO: fill priority queue with Paths that were found
        return pathPQ

    def printGraphState(self):
        pass
        # TODO: method for printing state of graph