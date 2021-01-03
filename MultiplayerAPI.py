from requests import get, post
from json import loads, load

class ServerAPI:
    def __init__(self, address):
        self.address = "http://"+address
    
    def Connect(self):
        resp = post(self.address+"/Connect")
        return resp

    def Disconnect(self, nickname):
        get(self.address+"/Disconnect", params={'nickname':nickname})

    def GetInfo(self, pos, nickname):
        Data = {'x':pos[0], 'y':pos[1], "nickname":nickname}
        resp = post(self.address+"/GetInfo", params=Data)
        return loads(resp.text)


