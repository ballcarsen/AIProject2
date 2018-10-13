from BackTracking.BackTrackingSearch import BackTrackingSearch


if __name__ == '__main__':
    # TODO: read in graphState, and fill in color character array

    mockColors = ["R", "G", "B"] # just a list of the colors to connect

    # In actuality, I think the graph state will be a Map data type from your code
    mockGraphState = [["B","_", "G"],
                      ["_", "R", "_"],
                      ["B", "R", "G"]]

    backtrack = BackTrackingSearch(mockGraphState, mockColors)
    backtrack.startBacktrack()