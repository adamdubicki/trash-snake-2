import bottle
import os
import random
from GameManager import GameManager
import BoardHelper

gameManager = GameManager()


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': "rgb(255, 255, 255)",
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'head_type': 'sand-worm',
        'tail_type': 'frechked',
        'name': 'Trash_snek'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    #
    # # TODO: Do things with data
    # directions = ['up', 'down', 'left', 'right']

    global gameManager
    game = gameManager.getGame(data)
    move = 'up'
    if (game != None):
        move = game.getNextMove()
    else:
        print "Snake == Dead"

    return {
        'move': move,
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
