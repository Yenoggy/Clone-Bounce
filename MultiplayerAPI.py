from requests import get, post, Session
from json import loads, load
from queue import Queue

class ServerAPI:
    def __init__(self, address):
        self.session = Session()
        self.address = "http://"+address
        self.Info = Queue()
    
    def Connect(self):
        resp = self.session.post(self.address+"/Connect")
        return resp

    def Disconnect(self, nickname):
        self.session.get(self.address+"/Disconnect", params={'nickname':nickname})
        self.session.close()

    def GetInfo(self, pos, boost, room, nickname):
        Data = {'x':pos[0], 'y':pos[1],'boost':boost,"room":room, "nickname":nickname}
        resp = self.session.post(self.address+"/GetInfo", params=Data, timeout=25)
        # self.Info.put(loads(resp.text))
        return loads(resp.text)

    def CreateShot(self, nickname, room, pos, vector):
        Data = {'nickname':nickname, 'room':room,'posx':round(pos[0], 3),"posy":round(pos[1], 3), "vecx":round(vector.x, 3), "vecy":round(vector.y, 3)}
        self.session.post(self.address+"/CreateShot", params=Data, timeout=25)

    def SendKeys(self, pressed, nickname):
        keys = {'a':0,'w':0,'d':0}
        if pressed[0] or pressed[1]:
            keys['a'] = 1
        if pressed[2] or pressed[3]:
            keys['w'] = 1
        if pressed[4] or pressed[5]:
            keys['d'] = 1
        keys['nickname'] = nickname
        self.session.post(self.address+"/SendKeys", params=keys, timeout=25)