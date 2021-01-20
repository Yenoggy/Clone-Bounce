from requests import get, post, Session
from json import loads, load
from queue import Queue

class ServerAPI:
    def __init__(self, address):
        self.address = "http://"+address
        self.Info = Queue()
    
    def Connect(self):
        global session
        session = Session()
        resp = session.post(self.address+"/Connect")
        return resp

    def Disconnect(self, nickname):
        session.get(self.address+"/Disconnect", params={'nickname':nickname})
        session.close()

    def GetInfo(self, pos, boost, room, nickname):
        Data = {'x':pos[0], 'y':pos[1],'boost':boost,"room":room, "nickname":nickname}
        resp = session.post(self.address+"/GetInfo", params=Data, timeout=25)
        # self.Info.put(loads(resp.text))
        return loads(resp.text)

    def SendKeys(self, pressed, nickname):
        keys = {'a':0,'w':0,'d':0}
        if pressed[0] or pressed[1]:
            keys['a'] = 1
        if pressed[2] or pressed[3]:
            keys['w'] = 1
        if pressed[4] or pressed[5]:
            keys['d'] = 1
        keys['nickname'] = nickname
        session.post(self.address+"/SendKeys", params=keys, timeout=25)