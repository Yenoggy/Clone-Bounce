from Player import player, Object, upd
from Cfg import *
from pygame.color import THECOLORS

pl = player()
world = Object(THECOLORS['yellow'], 0, Height // 2 + 370, Width, Height)

objects = [pl, [world,

Object(THECOLORS['yellow'], 0, 0, 800, 20),#граница 1
Object(THECOLORS['yellow'], 0, 0, 20, 600),#граница 1
Object(THECOLORS['yellow'], 780, 0, 20, 600),#граница 1
Object(THECOLORS['yellow'], 0, 200, 150, 20), #ступенька л1
Object(THECOLORS['yellow'], 0, 300, 200, 20),#ступенька л2
Object(THECOLORS['yellow'], 650, 500, 150, 20), #ступенька пр2
Object(THECOLORS['yellow'], 640, 600, 160, 20),#ступенька пр1
Object(THECOLORS['yellow'], 200, 600, 300, 20),
Object(THECOLORS['yellow'], 200, 400, 20, 370),#столбик середина
Object(THECOLORS['yellow'], 0, 600, 110, 20),
Object(THECOLORS['yellow'], 140, 400, 60, 20),
Object(THECOLORS['yellow'], 350, 620, 20, 50),#ворота низ
Object(THECOLORS['yellow'], 350, 725, 20, 50),#ворота низ
Object(THECOLORS['yellow'], 500, 200, 450, 20), #ступенька пр3
Object(THECOLORS['yellow'], 500, 350, 200, 20), #ступенька пр4
Object(THECOLORS['yellow'], 665, 350, 20, 60),#ворота право
Object(THECOLORS['yellow'], 665, 460, 20, 60),#ворота право
Object(THECOLORS['yellow'], 500, 350, 20, 40),
Object(THECOLORS['yellow'], 300, 0, 20, 200), #столбик верх
Object(THECOLORS['yellow'], 90, 80, 220, 20), #ступенька л3
Object(THECOLORS['yellow'], 105, 100, 20, 25), #ворота лево
Object(THECOLORS['yellow'], 105, 175, 20, 25), #ворота лево
Object(THECOLORS['yellow'], 550, 0, 20, 80),#ворота верх
Object(THECOLORS['yellow'], 550, 140, 20, 60),#ворота верх

], []]
upd()