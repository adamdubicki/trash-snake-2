from BoardEntityEnum import BoardEntityEnum
from itertools import product


class Game():
    def __init__(self, board):
        self.board = board
        self.food = []
        self.snakes = {}
        self.ourId = None
        self.ateFoodLastTurn = False

    def updateBoardFromJson(self, gameJson):
        self.__updateFood(gameJson["food"])
        self.__updateSnakes(gameJson["snakes"])

    def __updateSnakes(self, snakes):
        for snake in snakes:
            newCoords = [(s[0], s[1]) for s in snake["coords"]]
            add = [s for s in newCoords if s not in self.snakes[snake["id"]]]
            remove = [s for s in self.snakes[snake["id"]] if s not in newCoords]
            self.board.insert(self.snakes[snake["id"]][0], BoardEntityEnum.OBSTACLE)
            for s in add:
                self.board.insert(s, BoardEntityEnum.OBSTACLE)
                self.snakes[snake["id"]].append(s)
            for s in remove:
                self.board.insert(s, BoardEntityEnum.EMPTY)
                self.snakes[snake["id"]].remove(s)
            if(snake["id"] == self.ourId):
                self.board.insert(newCoords[0], BoardEntityEnum.HEAD)
                if(self.ateFoodLastTurn):
                    self.board.insert(newCoords[len(newCoords)-1], BoardEntityEnum.OBSTACLE)
                else:
                    self.board.insert(newCoords[len(newCoords) - 1], BoardEntityEnum.EMPTY)
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
