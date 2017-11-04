from Board import Board
from Game import Game

# The game cache holds game objects, indexed by game_id
# Its job is to return game objects in correct state
class GameManager():

    # Constructor
    def __init__(self):
        self.gameCache = {}

    # Return a game object from the game json
    # Using the game cache speeds this up.
    def getGame(self, gameJson):
        gid = gameJson["you"]
        if (gid not in self.gameCache.keys()):
            game = Game(Board(gameJson["width"], gameJson["height"]))
            game.ourId = gameJson["you"]
            for s in gameJson["snakes"]:
                game.snakes[s["id"]] = []
            self.gameCache[gid] = game
        else:
            game = self.gameCache[gid]
        game.updateBoardFromJson(gameJson)
        return game
