def readMaze(file_name):
    lines = [line.rstrip('\n') for line in open(file_name)]

if __name__ == '__main__':
    readMaze('5x5maze.txt')