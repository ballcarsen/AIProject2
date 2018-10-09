from Node import Node
from Map import Map
maps = []
initMap = None
def printMap(map):
    for row in map:
        for node in row:
            print(node.char, end='')
        print()

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
                temp.append(node)
                positionDict[char] = temp
            # append to row of map
            row.append(node)
        map.append(row)
    return map, positionDict

def addNeighbors(map):
    for row in map:
        for node in row:
            # add neighbors
            x = node.xCoor
            y = node.yCoor

            # if we are not using the coordinates of the center node, and it's in bounds, and it's not a wall
            # then add it's neighbor to it
            i = y
            j = x - 1
            if(i >= 0 and j >= 0 and i < len(map) and j < len(row)):
                node.addNeighbor(map[i][j])
            i = y
            j = x + 1
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row)):
                node.addNeighbor(map[i][j])
            i = y - 1
            j = x
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row)):
                node.addNeighbor(map[i][j])
            i = y + 1
            j = x
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row)):
                node.addNeighbor(map[i][j])

def findPath(map, node, path, goal, char):
    print("exploring %d %d" % (node.xCoor, node.yCoor))
    print('length %d' % len(node.neighbors))
    for neighbor in node.neighbors:
        valid = 0
        position = (neighbor.xCoor, neighbor.yCoor)
        print(position)
        if position == goal:
            print('goal')
            print(path)
            m = Map(initMap, path, char)
            maps.append(m)
        if neighbor.char == '_' and (neighbor.xCoor, neighbor.yCoor) not in path:
            # If the neighbor is the start node
            if (neighbor.xCoor, neighbor.yCoor) == path[0]:
                valid += 1
            if (neighbor.xCoor - 1, neighbor.yCoor) in path:
                valid += 1
            if (neighbor.xCoor + 1, neighbor.yCoor) in path:
                valid += 1
            if (neighbor.xCoor, neighbor.yCoor + 1) in path:
                valid += 1
            if (neighbor.xCoor, neighbor.yCoor - 1) in path:
                valid += 1

            if valid < 2:
                print('valid')
                copy = [pos for pos in path]
                copy.append(position)
                findPath(map, neighbor, copy, goal, char)
            else:
                print('invalid')

def findPaths(map, startNode, endNode, char):
    paths = []
    count = 0
    for neighbor in startNode.neighbors:
        if neighbor.char == '_':
            position = (neighbor.xCoor, neighbor.yCoor)
            print(position)
            findPath(map, neighbor, [(startNode.xCoor, startNode.yCoor),position], (endNode.xCoor, endNode.yCoor), char)
            print("count %d" % count)
            count += 1
            print(paths)
    return paths


if __name__ == '__main__':
    map, positionDict = readMaze('5x5maze.txt')
    initMap = map
    addNeighbors(map)
    printMap(map)
    findPaths(map, positionDict['B'][0], positionDict['B'][1], 'B')
    for m in maps:
        m.printMap()
        print()
