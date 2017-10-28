from datetime import datetime

from GameManager import GameManager

b = {
    "you": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
    "width": 9,
    "height": 4,
    "turn": 0,
    "snakes": [
        {
            "taunt": "git gud",
            "name": "my-snake",
            "id": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
            "health_points": 93,
            "coords": [
                [
                    8,
                    0
                ],
                [
                    8,
                    1
                ],
                [
                    8,
                    2
                ]
            ]
        }
    ],
    "game_id": "870d6d79-93bf-4941-8d9e-944bee131167",
    "food": [
        [
            3,
            2
        ],
        [
            3,
            3
        ]
    ],
    "dead_snakes": [
        {
            "taunt": "gotta go fast",
            "name": "other-snake",
            "id": "c4e48602-197e-40b2-80af-8f89ba005ee9",
            "health_points": 50,
            "coords": [
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ]
            ]
        }
    ]
}
gm = GameManager()

startTime= datetime.now()

game = gm.getGame(b)

timeElapsed=datetime.now()-startTime
print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))
# print game.board

b = {
    "you": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
    "width": 9,
    "height": 4,
    "turn": 0,
    "snakes": [
        {
            "taunt": "git gud",
            "name": "my-snake",
            "id": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
            "health_points": 93,
            "coords": [
                [
                    8,
                    0
                ],
                [
                    8,
                    1
                ],
                [
                    8,
                    2
                ]
            ]
        }
    ],
    "game_id": "870d6d79-93bf-4941-8d9e-944bee131167",
    "food": [
        [
            3,
            2
        ],
        [
            8,
            3
        ]
    ],
    "dead_snakes": [
        {
            "taunt": "gotta go fast",
            "name": "other-snake",
            "id": "c4e48602-197e-40b2-80af-8f89ba005ee9",
            "health_points": 50,
            "coords": [
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ]
            ]
        }
    ]
}
game = gm.getGame(b)
timeElapsed=datetime.now()-startTime
print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))


b = {
    "you": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
    "width": 9,
    "height": 4,
    "turn": 0,
    "snakes": [
        {
            "taunt": "git gud",
            "name": "my-snake",
            "id": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
            "health_points": 93,
            "coords": [
                [
                    7,
                    0
                ],
                [
                    8,
                    0
                ],
                [
                    8,
                    1
                ]
            ]
        }
    ],
    "game_id": "870d6d79-93bf-4941-8d9e-944bee131167",
    "food": [
        [
            8,
            2
        ],
        [
            8,
            3
        ]
    ],
    "dead_snakes": [
        {
            "taunt": "gotta go fast",
            "name": "other-snake",
            "id": "c4e48602-197e-40b2-80af-8f89ba005ee9",
            "health_points": 50,
            "coords": [
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ],
                [
                    5,
                    0
                ]
            ]
        }
    ]
}
game = gm.getGame(b)
timeElapsed=datetime.now()-startTime
print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))

