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



