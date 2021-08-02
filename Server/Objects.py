from Player import player, Object, ObjectPlayer, upd, THECOLORS, Coin
from Cfg import *

# from main import Update as ObjUpdate

pl = player()

objects = [
    pl,
    """[
        [
        [   Object(THECOLORS["lightgoldenrod"], 0, Height // 2 + 370, Width, Height),
            Object(THECOLORS["slateblue3"], 0, 0, 800, 20),
            Object(THECOLORS["slateblue3"], 0, 0, 20, 770),
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
            Object(THECOLORS["slateblue3"], 350, 720, 20, 50),
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
        [
            Object(THECOLORS["hotpink3"], 250, 560, 20, 40),
            Object(THECOLORS["hotpink3"], 300, 560, 20, 40),
            Object(THECOLORS["hotpink3"], 350, 560, 20, 40),
            Object(THECOLORS["hotpink3"], 600, 160, 20, 40),
            Object(THECOLORS["hotpink3"], 50, 560, 20, 40),
            Object(THECOLORS["hotpink3"], 740, 570, 40, 20),
            Object(THECOLORS["hotpink3"], 740, 535, 40, 20),
            Object(THECOLORS["hotpink3"], 20, 235, 40, 20),
            Object(THECOLORS["hotpink3"], 20, 270, 40, 20),
            Object(THECOLORS["hotpink3"], 490, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 540, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 590, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 640, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 90, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 140, 730, 20, 40),
            Object(THECOLORS["hotpink3"], 320, 125, 40, 20),
            Object(THECOLORS["hotpink3"], 320, 160, 40, 20),
        ],
        [
            Object(THECOLORS["yellow"], 715, 552, 20, 20),
            Object(THECOLORS["yellow"], 65, 252, 20, 20),
            Object(THECOLORS["yellow"], 700, 160, 20, 20),
            Object(THECOLORS["yellow"], 740, 160, 20, 20),
            Object(THECOLORS["yellow"], 400, 100, 20, 20),
            Object(THECOLORS["yellow"], 260, 42, 20, 20),
            Object(THECOLORS["yellow"], 240, 730, 20, 20),
            Object(THECOLORS["yellow"], 280, 730, 20, 20),
            Object(THECOLORS["yellow"], 40, 730, 20, 20),
        ],
        [
            Object(THECOLORS["mediumseagreen"], 480, 580, 180, 20),
            Object(THECOLORS["mediumseagreen"], 120, 380, 120, 20),
            Object(THECOLORS["mediumseagreen"], 470, 180, 80, 20),
            Object(THECOLORS["mediumseagreen"], 550, 340, 120, 10),
            Object(THECOLORS["mediumseagreen"], 100, 70, 100, 10),
            Object(THECOLORS["mediumseagreen"], 70, 580, 130, 20),
        ],
        [

        ]],
        [
        [   Object(THECOLORS["lightgoldenrod"], 0, Height // 2 + 370, Width, Height),
            Object(THECOLORS["slateblue3"], 0, 0, 800, 20),
            Object(THECOLORS["slateblue3"], 0, 0, 20, 600),
            Object(THECOLORS["slateblue3"], 780, 0, 20, 770),
            Object(THECOLORS["slateblue3"], 0, 600, 140, 20),
            Object(THECOLORS["slateblue3"], 200, 470, 20, 300),
            Object(THECOLORS["slateblue3"], 80, 470, 120, 20),
            Object(THECOLORS["slateblue3"], 300, 350, 20, 300),
            Object(THECOLORS["slateblue3"], 200, 350, 100, 20),
            Object(THECOLORS["slateblue3"], 320, 630, 360, 20),
            Object(THECOLORS["slateblue3"], 500, 450, 30, 20),
            Object(THECOLORS["slateblue3"], 750, 400, 30, 20),
            Object(THECOLORS["slateblue3"], 550, 220, 130, 20),
            Object(THECOLORS["slateblue3"], 320, 30, 230, 20),
            Object(THECOLORS["slateblue3"], 0, 250, 340, 20),
            Object(THECOLORS["slateblue3"], 230, 160, 20, 110),
            Object(THECOLORS["slateblue3"], 230, 0, 20, 110),
            Object(THECOLORS["slateblue3"], 230, 160, 110, 20),
            Object(THECOLORS["slateblue3"], 670, 30, 130, 20),
            Object(THECOLORS["slateblue3"], 700, 130, 100, 20),
            Object(THECOLORS["slateblue3"], 0, 80, 100, 20),
            Object(THECOLORS["slateblue3"], 0, 180, 130, 20),
            Object(THECOLORS["slateblue3"], 320, 160, 20, 110),
        ],
        [
            Object(THECOLORS["hotpink3"], 80, 560, 20, 40),
            Object(THECOLORS["hotpink3"], 330, 710, 20, 60),
            Object(THECOLORS["hotpink3"], 430, 710, 20, 60),
            Object(THECOLORS["hotpink3"], 530, 710, 20, 60),
            Object(THECOLORS["hotpink3"], 630, 710, 20, 60),
            Object(THECOLORS["hotpink3"], 340, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 380, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 420, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 460, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 500, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 540, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 580, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 620, 595, 20, 35),
            Object(THECOLORS["hotpink3"], 20, 115, 40, 20),
            Object(THECOLORS["hotpink3"], 20, 150, 40, 20),
            Object(THECOLORS["hotpink3"], 740, 65, 40, 20),
            Object(THECOLORS["hotpink3"], 740, 100, 40, 20),

        ],
        [
            Object(THECOLORS["yellow"], 380, 730, 20, 20),
            Object(THECOLORS["yellow"], 480, 730, 20, 20),
            Object(THECOLORS["yellow"], 580, 730, 20, 20),
            Object(THECOLORS["yellow"], 750, 370, 20, 20),
            Object(THECOLORS["yellow"], 750, 430, 20, 20),
            Object(THECOLORS["yellow"], 65, 132, 20, 20),
            Object(THECOLORS["yellow"], 715, 82, 20, 20),
            Object(THECOLORS["yellow"], 40, 40, 20, 20),
        ],
        [
            Object(THECOLORS["mediumseagreen"], 80, 490, 80, 20),
            Object(THECOLORS["mediumseagreen"], 320, 350, 140, 20),
            Object(THECOLORS["mediumseagreen"], 350, 650, 280, 20),
            Object(THECOLORS["mediumseagreen"], 570, 240, 100, 20),
            Object(THECOLORS["mediumseagreen"], 340, 50, 190, 20),
        ],
        [
            
        ]]]""",
    {},
    {}
]