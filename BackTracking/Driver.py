from BackTracking.BackTrackingSearch import BackTrackingSearch
from BackTracking.Node import Node
from BackTracking.Map import Map
import time
import sys

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
    # print(sys.argv[1:])
    # This path is gonna be messed up on windows
    map, positionDict = readMaze(sys.argv[1])
    useColorHeuristic = False
    usePathHeuristic = False

    if sys.argv[2] == "True":
        useColorHeuristic = True
    elif sys.argv[2] == "False":
        useColorHeuristic = False
    else:
        print("Invalid command line argument for color heuristic")


    if sys.argv[3] == "True":
        usePathHeuristic = True
    elif sys.argv[3] == "False":
        usePathHeuristic = False
    else:
        print("Invalid command line argument for path heuristic")

    graphState = Map(map)
    graphState.addNeighbors()
    startTime = time.time()

    backtrack = BackTrackingSearch(graphState, positionDict, useColorHeuristic, usePathHeuristic)
    backtrack.startBacktrack()
    endTime = time.time()
    print("run time: %.3f" %(endTime - startTime))
    print("time spent on color heuristic: %.3f \n" %backtrack.timeSpentFindingPaths)
    print("number of edges traversed:", backtrack.numEdges, "\n")
    backtrack.graphState.printMap()