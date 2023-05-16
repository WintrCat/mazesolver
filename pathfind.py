from time import sleep

import board

class State:
    def __init__(self, x, y, parent = None):
        self.x = x
        self.y = y
        self.parent = parent

goalState = State(board.size() - 2, board.size() - 2)
goalRoute: list[State] = []
def isGoalRoute(checkstate: State):
    for state in goalRoute:
        if state.x == checkstate.x and state.y == checkstate.y:
            return True
    return False

frontier: list[State] = []
explored: list[State] = []
def isExplored(checkstate: State) -> bool:
    for state in explored:
        if state.x == checkstate.x and state.y == checkstate.y:
            return True
    return False

frontier.append(State(1, 1))

def findpath():
    print("Pathfinding...")

    reachedGoalState = None
    while reachedGoalState == None:
        currentState = frontier[0]

        if currentState.x == goalState.x and currentState.y == goalState.y:
            reachedGoalState = currentState

        x = currentState.x
        y = currentState.y

        right = State(x + 1, y, currentState)
        left = State(x - 1, y, currentState)
        up = State(x, y - 1, currentState)
        down = State(x, y + 1, currentState)

        if board.at(x + 1, y) == "-" and not isExplored(right):
            frontier.append(right)
            explored.append(right)
        if board.at(x - 1, y) == "-" and not isExplored(left):
            frontier.append(left)
            explored.append(left)
        if board.at(x, y - 1) == "-" and not isExplored(up):
            frontier.append(up)
            explored.append(up)
        if board.at(x, y + 1) == "-" and not isExplored(down):
            frontier.append(down)
            explored.append(down)
        frontier.remove(currentState)

    currentState = reachedGoalState
    while currentState.parent != None:
        goalRoute.append(currentState)
        currentState = currentState.parent

    print("Goal found!")