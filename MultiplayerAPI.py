from requests import get, post
from json import loads, load
from queue import Queue

class ServerAPI:
    def __init__(self, address):
        self.address = "http://"+address
        self.Info = Queue()
    
    def Connect(self):
        resp = post(self.address+"/Connect")
        return resp

    def Disconnect(self, nickname):
        get(self.address+"/Disconnect", params={'nickname':nickname})

    def GetInfo(self, pos, nickname):
        Data = {'x':pos[0], 'y':pos[1], "nickname":nickname}
        resp = post(self.address+"/GetInfo", params=Data)
        # self.Info.put(loads(resp.text))
        return loads(resp.text)



