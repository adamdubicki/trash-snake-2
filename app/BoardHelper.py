from Game import Game
from Board import Board
from BoardEntityEnum import BoardEntityEnum
import collections


def reconstructShortestPath(cameFrom, current):
    path = []
    while current in cameFrom.keys():
        current = cameFrom[current]
        path.append(current)
    path.pop()
    return list(reversed(path))


# Return the shortest path [t1,t2,tn] between start and goal
# else return none if no paths exist
# A* algorithm (improved Dijkstra
def shortestPath(board, start, goal):
    closedSet = []
    openSet = [start]
    cameFrom = {}

    # Actual best shortest path distance score
    gScore = [[100000 for x in xrange(board.width)] for y in xrange(board.height)]
    gScore[start[0]][start[1]] = 0

    # Score given as distance between two tiles, priority is to check tiles closer to goal
    fScore = [[100000 for x in xrange(board.width)] for y in xrange(board.height)]
    fScore[start[0]][start[1]] = getDistanceBetweenTiles(start, goal)

    while (len(openSet) > 0):
        current = min(openSet, key=lambda p: fScore[p[0]][p[1]])
        if (current == goal):
            return reconstructShortestPath(cameFrom, goal)
        openSet.remove(current)
        openSet.append(current)
        neighbors = getValidNeighbords(board, current)
        for neighbor in neighbors:
            if neighbor in closedSet:
                continue
            gscore = gScore[current[0]][current[1]] + getDistanceBetweenTiles(current, neighbor)
            if neighbor not in openSet:
                openSet.append(neighbor)
            elif gscore >= gScore[current[0]][current[1]]:
                continue
            cameFrom[neighbor] = current
            gScore[neighbor[0]][neighbor[1]] = gscore
            fScore[neighbor[0]][neighbor[1]] = gScore + getDistanceBetweenTiles(neighbor, goal)
    return None


# Get all adjacent tiles that are in the board
def getInBoundNeighbors(board, tile):
    possibleTiles = [
        (tile[0] - 1, tile[1]),
        (tile[0] + 1, tile[1]),
        (tile[0], tile[1] - 1),
        (tile[0], tile[1] + 1)
    ]
    return filter(lambda x: board.tileInBounds(x), possibleTiles)


# Return all adjacent tiles which our snake could move to
def getValidNeighbords(board, tile):
    possibleTiles = getInBoundNeighbors(board, tile)
    return filter(lambda x: board.getEntityAtTile() == BoardEntityEnum.EMPTY, possibleTiles)


# Get manhatten distance between tile1(x,y) and tile2(x,y)
def getDistanceBetweenTiles(tile1, tile2):
    return abs(tile1[0] - tile2[0]) + abs(tile1[1] - tile2[1])


def pickFood(ourSnakeId, snakes, food):
    goal = (9999, (-1, -1))
    foodDistances = collections.OrderedDict()
    for f in food:
        foodDistances[tuple(food)] = goal
        for s in snakes.keys():
            distance = getDistanceBetweenTiles(f, snakes[s][0])
            if distance < foodDistances[tuple(food)][0]:
                foodDistances[tuple(food)] = (distance, (snakes[s][0][0], snakes[s][0][1]))
    goalChoices = []
    for food in foodDistances:
        if (foodDistances[food][1] == ourSnakeId):
            goalChoices.append(food)
    if (len(goalChoices) > 0):
        return min(goalChoices, key=lambda p: foodDistances[p][0])
    else:
        return None
