board = [list(row) for row in open("altmap.txt", "r").read().split("\n")]
if len(board[-1]) == 1: board.pop()

def get(): 
    return board


def at(x, y):
    return board[y][x]


def size():
    return len(board)