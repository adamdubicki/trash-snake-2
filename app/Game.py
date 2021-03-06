from BoardEntityEnum import BoardEntityEnum
import BoardHelper


class Game():
    def __init__(self, board):
        self.board = board
        self.food = []
        self.snakes = {}
        self.ourId = None
        self.ateFoodLastTurn = False

    def getNextMove(self):
        food = BoardHelper.pickFood(self.ourId, self.snakes, self.food)
        if (food != None):
            path = BoardHelper.shortestPath(self.board, self.snakes[self.ourId], food)
            if (path != None):
                return path[0]
            else:
                return 'up'
        else:
            return 'up'

    def updateBoardFromJson(self, gameJson):
        self.__updateFood(gameJson["food"])
        self.__updateSnakes(gameJson["snakes"])

    def __updateSnakes(self, snakes):
        for snake in snakes:
            newCoords = [(s[0], s[1]) for s in snake["coords"]]
            add = [s for s in newCoords if s not in self.snakes[snake["id"]]]
            remove = filter(lambda x: x not in newCoords, self.snakes[snake["id"]])
            if (len(self.snakes[snake["id"]])):
                self.board.insert(self.snakes[snake["id"]][0], BoardEntityEnum.OBSTACLE)
            for s in add:
                self.board.insert(s, BoardEntityEnum.OBSTACLE)
                self.snakes[snake["id"]].append(s)
            for s in remove:
                self.board.insert(s, BoardEntityEnum.EMPTY)
                self.snakes[snake["id"]].remove(s)
            if (snake["id"] == self.ourId):
                if (self.ateFoodLastTurn):
                    self.board.insert(newCoords[len(newCoords) - 1], BoardEntityEnum.OBSTACLE)
                elif (len(newCoords) - 1 > 2):
                    self.board.insert(newCoords[len(newCoords) - 1], BoardEntityEnum.EMPTY)
                self.board.insert(newCoords[0], BoardEntityEnum.HEAD)
            self.snakes[snake["id"]] = newCoords

    def __updateFood(self, food):
        newFood = [(f[0], f[1]) for f in food]
        add = [f for f in newFood if f not in self.food]
        remove = [f for f in self.food if f not in newFood]
        for f in add:
            self.board.insert(f, BoardEntityEnum.FOOD)
            self.food.append(f)
        for f in remove:
            self.board.insert(f, BoardEntityEnum.EMPTY)
            self.food.remove(f)
