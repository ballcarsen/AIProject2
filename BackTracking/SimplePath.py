from BackTracking.PathInterface import PathInterface

class SimplePath(PathInterface):

    # each path has a color, and a list of the coordinates that make up the path
    def __init__(self, _pathColor, _coordinateList):
        self.pathColor = _pathColor # character
        self.coordList = _coordinateList
        self.compareValue = 10

    # this may need to be tested, shorter lengths should be higher priority in the queue
    def __lt__(self, other):
        return self.compareValue < other.compareValue
