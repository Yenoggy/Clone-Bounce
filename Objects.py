from Player import player, Object, ObjectPlayer, upd, THECOLORS
from Cfg import *
# from main import Update as ObjUpdate

pl = player()
world = Object(THECOLORS["slateblue3"], 0, Height // 2 + 370, Width, Height)

objects = [
    pl,
    [world,
        Object(THECOLORS["slateblue3"], 0, 0, 800, 20),
        Object(THECOLORS["slateblue3"], 0, 0, 20, 600),
        Object(THECOLORS["slateblue3"], 780, 0, 20, 600),
        Object(THECOLORS["slateblue3"], 0, 200, 150, 20),
        Object(THECOLORS["slateblue3"], 0, 300, 200, 20),
        Object(THECOLORS["slateblue3"], 650, 500, 150, 20),
        Object(THECOLORS["slateblue3"], 640, 600, 160, 20),
        Object(THECOLORS["slateblue3"], 200, 600, 300, 20),
        Object(THECOLORS["slateblue3"], 200, 400, 20, 370),
        Object(THECOLORS["slateblue3"], 0, 600, 110, 20),
        Object(THECOLORS["slateblue3"], 140, 400, 60, 20),
        Object(THECOLORS["slateblue3"], 350, 620, 20, 50),
        Object(THECOLORS["slateblue3"], 350, 725, 20, 50),
        Object(THECOLORS["slateblue3"], 500, 200, 450, 20),
        Object(THECOLORS["slateblue3"], 500, 350, 200, 20),
        Object(THECOLORS["slateblue3"], 665, 350, 20, 60),
        Object(THECOLORS["slateblue3"], 665, 460, 20, 60),
        Object(THECOLORS["slateblue3"], 500, 350, 20, 40),
        Object(THECOLORS["slateblue3"], 300, 0, 20, 200),
        Object(THECOLORS["slateblue3"], 90, 80, 220, 20),
        Object(THECOLORS["slateblue3"], 105, 100, 20, 25),
        Object(THECOLORS["slateblue3"], 105, 175, 20, 25),
        Object(THECOLORS["slateblue3"], 550, 0, 20, 80),
        Object(THECOLORS["slateblue3"], 550, 140, 20, 60),
    ],
    {},
    [
        Object(THECOLORS["hotpink3"], 260, 560, 20, 40),
        Object(THECOLORS["hotpink3"], 600, 160, 20, 40),
        Object(THECOLORS["hotpink3"], 50, 560, 20, 40),
        Object(THECOLORS["hotpink3"], 740, 570, 40, 20), # wall
        Object(THECOLORS["hotpink3"], 740, 535, 40, 20), # wall
        Object(THECOLORS["hotpink3"], 20, 235, 40, 20),  # wall_l
        Object(THECOLORS["hotpink3"], 20, 270, 40, 20),  # wall_l
        Object(THECOLORS["hotpink3"], 490, 730, 20, 40),
        Object(THECOLORS["hotpink3"], 540, 730, 20, 40),
        Object(THECOLORS["hotpink3"], 590, 730, 20, 40),
        Object(THECOLORS["hotpink3"], 640, 730, 20, 40),
    ],
    [
        Object(THECOLORS["yellow"], 715, 552, 20, 20),
        Object(THECOLORS["yellow"], 75, 252, 20, 20),
        Object(THECOLORS["yellow"], 700, 160, 20, 20),
        Object(THECOLORS["yellow"], 740, 160, 20, 20),
        Object(THECOLORS["yellow"], 400, 100, 20, 20),
        Object(THECOLORS["yellow"], 250, 40, 20, 20),
        Object(THECOLORS["yellow"], 240, 730, 20, 20),
        Object(THECOLORS["yellow"], 280, 730, 20, 20),
    ],
    [
        Object(THECOLORS["white"], 500, 600, 140, 20),
    ],
]
upd()
