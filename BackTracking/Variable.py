class Variable:
    def __init__(self, _color):
        self.color = _color # character to indicate color e.g. R = red
        self.compareValue = -1 # value to compare different variables for ordering search

    def __lt__(self, other):
        return self.compareValue < other.compareValue

    # implement heuristic hin this method
    def setCompareVal(self, graphState):
        self.compareValue = 100
        # TODO: set compare value equal to the number of paths (values) that can be generated for this variable