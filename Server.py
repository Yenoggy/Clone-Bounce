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
        PlayerList['1'] = {'pos':StartPos, 'boost':0}
    else:
        PlayerList[str(int(list(PlayerList.keys())[-1])+1)] = {'pos':StartPos, 'boost':0}
    return str(list(PlayerList.keys())[-1])

@app.post('/GetInfo')
def GetInfo(x, y, nickname):
    if nickname in PlayerList:
        PlayerList[nickname] = {'pos':(int(x),int(y)), 'boost':0}
        objects = PlayerList.copy()
        objects.pop(nickname)
        return objects
    return []

@app.post('/Connect')
def Connect():
    resp = Join()
    return {'map':Map, "spikes":spikes, "coins":coins, "mud":mud, 'nickname':resp, 'pos':StartPos}

@app.get('/Disconnect')
def Disconnect(nickname):
    PlayerList.pop(nickname)
    return ''

def Start():
    global Map, StartPos, spikes, coins, mud
    with open('Config.json', 'r') as f:
        CFG = json.load(f)
        Map = CFG['map']
        spikes = CFG['spikes']
        coins = CFG['coins']
        mud = CFG['mud']

        StartPos = CFG['startpos']

if __name__ == '__main__':
    Start()
    uvicorn.run(app, host='0.0.0.0', port=12345)
    # uvicorn.run(app, host='37.143.12.148', port=34567)