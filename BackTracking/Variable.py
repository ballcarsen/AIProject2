class Variable:
    def __init__(self, _color, startCoor, endCoor):
        self.color = _color # character to indicate color e.g. R = red
        self.compareValue = -1 # value to compare different variables for ordering search
        self.startCoor = startCoor # list: [x, y]
        self.endCoor = endCoor

    # may need to test this, if compare value is smaller when there are fewer possible paths,
    # then this smaller value should be higher priority in the queue
    def __lt__(self, other):
        return self.compareValue < other.compareValue

    # implement heuristic hin this method
    def setCompareVal(self, newValue):
        self.compareValue = newValue
        # TODO: set compare value equal to the number of paths (values) that can be generated for this variable