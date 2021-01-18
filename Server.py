from fastapi import FastAPI, Request
import uvicorn, json, pygame

app = FastAPI()

objects = []
Map = []
spikes = []
coins = []
mud = []
PlayerList = {}

def Join():
    if len(PlayerList) == 0:
        PlayerList['1'] = {'pos':StartPos, 'boost':0, 'nickname':'1', 'room':0}
    else:
        PlayerList[str(int(list(PlayerList.keys())[-1])+1)] = {'pos':StartPos, 'boost':0, 'nickname':str(int(list(PlayerList.keys())[-1])+1), 'room':0}
    return str(list(PlayerList.keys())[-1])

@app.post('/GetInfo')
def GetInfo(x, y, boost, room, nickname):
    if nickname in PlayerList:
        PlayerList[nickname] = {'pos':(int(x),int(y)), 'boost':int(boost), 'nickname':nickname, 'room':int(room)}
        objects = PlayerList.copy()
        objects.pop(nickname)
        return objects
    return []

@app.post('/Connect')
def Connect():
    resp = Join()
    return {'map':Map, 'nickname':resp, 'pos':StartPos, 'room':0}

@app.get('/Disconnect')
def Disconnect(nickname):
    PlayerList.pop(nickname)
    return ''

def Start():
    global Map, StartPos
    with open('Config.json', 'r') as f:
        CFG = json.load(f)
        Map = CFG['MAP']
        StartPos = CFG['startpos']

if __name__ == '__main__':
    Start()
    uvicorn.run(app, host='0.0.0.0', port=12345)
    # uvicorn.run(app, host='37.143.12.148', port=34567)