from fastapi import FastAPI, Request
from threading import Thread
import traceback

import uvicorn, json, pygame

from Objects import objects
from Cfg import *
from Player import Bullet, Object, ObjectPlayer, THECOLORS, pygame, upd

app = FastAPI()

PlayerList = {}
Map = objects[1]
upd()
objects[0].y = -1000
# objects[1] = eval(objects[1])


def Join():
    if len(objects[2]) == 0:
        objects[2]['1'] = ObjectPlayer(player_pos, '1')
    else:
        objects[2][str(int(list(objects[2].keys())[-1])+1)] = ObjectPlayer(player_pos, str(int(list(objects[2].keys())[-1])+1))
    return str(list(objects[2].keys())[-1])

@app.post('/GetInfo')
def GetInfo(x, y, boost, room, nickname):
    objs = []
    if nickname in objects[2]:
        objects[2][nickname].x, objects[2][nickname].y     =   (int(x),int(y))
        objects[2][nickname].boost         =   int(boost)
        objects[2][nickname].nickname      =   nickname
        objects[2][nickname].room          =   int(room)
        objs.append(objects[2].copy())
        for obj in objects[2]:
            st = str(objects[2][obj])

            objs[0][obj] = json.loads(st)
        objs.append(objects[3].copy())
        for obj in objects.copy()[3]:
            objs[1][obj] = json.loads(str(objects[3][obj]))
        objs[0].pop(nickname)
        return objs
    return []

@app.post('/SendKeys')
def SendKeys(a, w, d, nickname):
    if nickname in objects[2]:
        objects[2][nickname].keys    =   [int(a),int(w),int(d)]

@app.post('/Connect')
def Connect():
    resp = Join()
    return {'map':Map, 'nickname':resp, 'pos':player_pos, 'room':0}

@app.post('/CreateShot')
def CreateShot(nickname, room, posx, posy, vecx, vecy):
    Id = int(list(objects[3].keys())[-1])+1 if len(objects[3]) > 0 else 1
    objects[3][str(Id)] = Bullet(
        Id,
        nickname,
        int(room),
        (float(posx), float(posy)), 
        pygame.math.Vector2(float(vecx), float(vecy)))
    return ''

@app.get('/Disconnect')
def Disconnect(nickname):
    if nickname in objects[2]:
        objects[2].pop(nickname)
        return 'Disconnected'
    else:
        return 'Player not found'

def BulletMove():
    Clock = pygame.time.Clock()
    while True:
        try:
            for obj in objects[3].copy():
                objects[3][obj].movement()
            Clock.tick(144)
        except:
            traceback.print_exception()

def Start():
    global Map, StartPos, Bullets
    Bullets = {}
    Thread(target=BulletMove).start()
    

if __name__ == '__main__':
    Start()
    uvicorn.run(app, host='0.0.0.0', port=12345)
    # uvicorn.run(app, host='37.143.12.148', port=34567)