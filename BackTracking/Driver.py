from BackTracking.BackTrackingSearch import BackTrackingSearch
from BackTracking.Node import Node
from BackTracking.Map import Map

def readMaze(file_name):
    lines = [line.rstrip('\n') for line in open(file_name)]
    map = []
    positionDict = {}
    for i in range(len(lines)):
        row = []
        # iterate through characters
        for j in range(len(lines[i])):
            # create node
            char = lines[i][j]
            node = Node(char, i, j)
            # if start node, append to frontier
            if(lines[i][j] != '_'):
                temp = positionDict.get(char, [])
                temp.append([node.xCoor, node.yCoor])
                positionDict[char] = temp
            # append to row of map
            row.append(node)
        map.append(row)
    return map, positionDict


if __name__ == '__main__':
    # TODO: read in graphState, and fill in color character array
    # This path is gonna be messed up on windows
    map, positionDict = readMaze('../5x5maze.txt')
    graphState = Map(map)
    graphState.addNeighbors()

    mockColors = ["R", "G", "B"] # just a list of the colors to connect

    # In actuality, I think the graph state will be a Map data type from your code
    mockGraphState = [["B","_", "G"],
                      ["_", "R", "_"],
                      ["B", "R", "G"]]

    backtrack = BackTrackingSearch(graphState, positionDict)
    backtrack.startBacktrack()
    backtrack.graphState.printMap()