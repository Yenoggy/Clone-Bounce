from fastapi import FastAPI, Request
from pygame.color import THECOLORS
import uvicorn, json, pygame

app = FastAPI()

objects = []
Map = []
PlayerList = {}

def Join():
    if len(PlayerList) == 0:
        PlayerList['1'] = {'pos':StartPos}
    else:
        PlayerList[str(int(list(PlayerList.keys())[-1])+1)] = {'pos':StartPos}
    return str(list(PlayerList.keys())[-1])

@app.post('/GetInfo')
def GetInfo(x, y, nickname):
    if nickname in PlayerList:
        PlayerList[nickname] = {'pos':(int(x),int(y))}
        objects = PlayerList.copy()
        objects.pop(nickname)
        return objects
    return []

@app.post('/Connect')
def Connect():
    resp = Join()
    return {'map':Map, 'nickname':resp, 'pos':StartPos}

@app.get('/Disconnect')
def Disconnect(nickname):
    PlayerList.pop(nickname)
    return ''

def Start():
    global Map, StartPos
    with open('Config.json', 'r') as f:
        CFG = json.load(f)
        Map = CFG['map']
        StartPos = CFG['startpos']





if __name__ == '__main__':
    Start()
    uvicorn.run(app, host='0.0.0.0', port=12345)
    # uvicorn.run(app, host='37.143.12.148', port=34567)