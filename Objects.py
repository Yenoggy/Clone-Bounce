from Player import player, Object, ObjectPlayer, upd, THECOLORS
from Cfg import *
# from main import Update as ObjUpdate

pl = player()
world = Object(THECOLORS["yellow"], 0, Height // 2 + 370, Width, Height)

objects = [
    pl,
    [world,
        Object(THECOLORS["yellow"], 0, 0, 800, 20),
        Object(THECOLORS["yellow"], 0, 0, 20, 600),
        Object(THECOLORS["yellow"], 780, 0, 20, 600),
        Object(THECOLORS["yellow"], 0, 200, 150, 20),
        Object(THECOLORS["yellow"], 0, 300, 200, 20),
        Object(THECOLORS["yellow"], 650, 500, 150, 20),
        Object(THECOLORS["yellow"], 640, 600, 160, 20),
        Object(THECOLORS["yellow"], 200, 600, 300, 20),
        Object(THECOLORS["yellow"], 200, 400, 20, 370),
        Object(THECOLORS["yellow"], 0, 600, 110, 20),
        Object(THECOLORS["yellow"], 140, 400, 60, 20),
        Object(THECOLORS["yellow"], 350, 620, 20, 50),
        Object(THECOLORS["yellow"], 350, 725, 20, 50),
        Object(THECOLORS["yellow"], 500, 200, 450, 20),
        Object(THECOLORS["yellow"], 500, 350, 200, 20),
        Object(THECOLORS["yellow"], 665, 350, 20, 60), 
        Object(THECOLORS["yellow"], 665, 460, 20, 60), 
        Object(THECOLORS["yellow"], 500, 350, 20, 40),
        Object(THECOLORS["yellow"], 300, 0, 20, 200),
        Object(THECOLORS["yellow"], 90, 80, 220, 20),
        Object(THECOLORS["yellow"], 105, 100, 20, 25),
        Object(THECOLORS["yellow"], 105, 175, 20, 25),
        Object(THECOLORS["yellow"], 550, 0, 20, 80),
        Object(THECOLORS["yellow"], 550, 140, 20, 60),
    ],
    {},
    [
        Object(THECOLORS["red"], 260, 560, 20, 40),
        Object(THECOLORS["red"], 600, 160, 20, 40),
        Object(THECOLORS["red"], 50, 560, 20, 40),
        Object(THECOLORS["red"], 740, 570, 40, 20), # wall
        Object(THECOLORS["red"], 740, 535, 40, 20), # wall
        Object(THECOLORS["red"], 20, 235, 40, 20),  # wall_l
        Object(THECOLORS["red"], 20, 270, 40, 20),  # wall_l
        Object(THECOLORS["red"], 540, 730, 20, 40),
        Object(THECOLORS["red"], 590, 730, 20, 40),
        Object(THECOLORS["red"], 640, 730, 20, 40),
    ],
]
upd()
