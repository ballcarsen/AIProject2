

class Path:

    # each path has a color, and a list of the coordinates that make up the path
    def __init__(self, _pathColor, _coordinateList):
        self.pathColor = _pathColor # character
        self.coordList = _coordinateList
        self.length = len(self.coordinateList) # using length of path as a heuristic for value ordering

    # this may need to be tested, greater lengths should be less priority in the queue
    def __lt__(self, other):
        return self.length > other.length