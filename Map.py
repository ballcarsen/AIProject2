from Node import Node
class Map:
    def __init__(self, baseMap, path, char = None):
        self.map = []
        for row in range(len(baseMap)):
            temp = []
            for position in baseMap[row]:
                temp.append(Node(position.char, position.xCoor, position.yCoor))
            self.map.append(temp)
        if char != None:
            for position in path:
                self.map[position[1]][position[0]].char = char

    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()