from BackTracking.BackTrackingSearch import BackTrackingSearch
from BackTracking.Node import Node
from BackTracking.Map import Map
import time

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
    print("pos dict: ", positionDict)
    return map, positionDict


if __name__ == '__main__':
    # TODO: read in graphState, and fill in color character array
    # This path is gonna be messed up on windows
    map, positionDict = readMaze('../9x9maze.txt')
    graphState = Map(map)
    graphState.addNeighbors()
    startTime = time.time()
    backtrack = BackTrackingSearch(graphState, positionDict)
    backtrack.startBacktrack()
    endTime = time.time()
    print("run time:", (endTime - startTime))
    print("time spend finding paths", backtrack.timeSpentFindingPaths)
    backtrack.graphState.printMap()