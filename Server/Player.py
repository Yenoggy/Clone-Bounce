import pygame, time, os
from Cfg import *
from json import loads
from pygame.color import THECOLORS
from threading import Thread
from random import random
Coins = {}

def upd():
    global objects, Coins
    from Objects import objects
    objects[1] = eval(objects[1])
    n=0
    for i in objects[1]:
        Coins[str(n)] = i[2].copy()
        n += 1 

def disc():
    player.connected = 0

def ConnectServer():
    global Server
    os.system(
        'mshta "javascript:var sh=new ActiveXObject( \'WScript.Shell\' ); sh.Popup( \'Введи IP:PORT в консоли!\', 10, \'Подключение к серверу\', 64 );close()"')
    address = input('IP:PORT\n>>> ')
    print(f'Подключение к {address}')
    if address != '':
        Server = ServerAPI(address)
    else:
        print('Отмена соединения')
        player.connected = 0
        return
    resp = Server.Connect()
    if resp.status_code == 200:
        global objects
        resp = loads(resp.text)
        objects[1] = eval(resp['map'])
        objects[0].nickname = resp['nickname']
        objects[0].x, objects[0].y = resp['pos']
        objects[0].room = resp['room']
        Tickrate = pygame.time.Clock()
        player.connected = 1
        while player.connected:
            try:
                Info = Server.GetInfo((objects[0].x, objects[0].y), objects[0].boost, objects[0].room, objects[0].nickname)
                players = objects[2].copy()
                for i in players:
                    if i not in Info:
                        objects[2].pop(i)
                for i in Info:
                    if i in objects[2]:
                        objects[2][i].x, objects[2][i].y = Info[i]['pos']
                        objects[2][i].boost = Info[i]['boost']
                        objects[2][i].room = Info[i]['room']
                        objects[2][i].keys = Info[i]['keys']
                    else:
                        objects[2][i] = ObjectPlayer(Info[i]['pos'], Info[i]['nickname'])
            except:
                pass
            Tickrate.tick(144)

    else:
        player.connected = 0
        os.system(
            f'mshta "javascript:var sh=new ActiveXObject( \'WScript.Shell\' ); sh.Popup( \'Соединение прервано! Код ошибки: {resp.status}\', 10, \'Ошибка при подключении\', 64 );close()"')



objects = []


class player:
    connected = 0
    pressed = [0,0,0,0,0,0]
    oldpressed = [0,0,0,0,0,0]
    def __init__(self):
        self.nickname = 'player'
        self.radius = player_radius
        self.x, self.y = player_pos
        self.rect = []
        self.look = player_look
        self.last_shot = 0
        self.in_air = 0
        self.boost = 0
        self.life = 1
        self.score = 0
        self.hp = hp
        self.last_d = 0
        self.room = 0

    def __str__(self):
        return "{'pos':"+str(list(self.pos))+", 'boost':"+str(self.boost)+", 'room': "+str(self.room)+", 'keys':"+str(self.keys)+", 'nickname':"+str(self.nickname)+"}"

    @property
    def pos(self):
        return self.x, self.y

    def Get_rect(self):
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]
        return self.rect

    def Collide(self, direction, speed):

        if direction in ["D", "U", "L"]:
            speed *= -1
        if direction in ["R", "L"]:
            self.rect = [
                self.x - self.radius + speed,
                self.y - self.radius,
                self.x + self.radius + speed,
                self.y + self.radius,
                self.x + speed,
                self.y
            ]
        elif direction in ["U", "D"]:
            self.rect = [
                self.x - self.radius,
                self.y - self.radius + speed,
                self.x + self.radius,
                self.y + self.radius + speed,
                self.x,
                self.y + speed,
            ]
        dots = [
            (self.rect[0], self.rect[1]),
            (self.rect[0], self.rect[3]),
            (self.rect[2], self.rect[1]),
            (self.rect[2], self.rect[3]),
            (self.rect[4], self.rect[1]),
            (self.rect[4], self.rect[3]),
            (self.rect[0], self.rect[5]),
            (self.rect[2], self.rect[5]),
        ]
        for obj in objects[1][self.room][0]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["U", "D"]:
                        self.boost = 0
                    if direction == 'R':
                        return point[0] - (self.x + self.radius)
                    elif direction == 'L':
                        return point[2] - (self.x - self.radius)
                    elif direction == 'U':
                        return point[3] - (self.y - self.radius)
                    elif direction == 'D':
                        self.in_air = 0
                        return point[1] - (self.y + self.radius)

        for obj in objects[2]:
            if objects[2][obj].room == self.room:
                for x, y in dots:
                    point = objects[2][obj].Get_rect()
                    if (x > point[0] and x < point[2]) and (
                            y > point[1] and y < point[3]
                    ):
                        if direction in ["U", "D"]:
                            self.boost = 0
                        if direction == 'R':
                            return point[0] - (self.x + self.radius)
                        elif direction == 'L':
                            return point[2] - (self.x - self.radius)
                        elif direction == 'U':
                            return point[3] - (self.y - self.radius)
                        elif direction == 'D':
                            self.in_air = 0
                            return point[1] - (self.y + self.radius)

        for obj in objects[1][self.room][1]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["U", "D"]:
                        self.boost = 0
                    self.die(time.time())

        for obj in objects[1][self.room][2]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    self.score += 1
                    objects[1][self.room][2].remove(obj)
                    print(self.score, '++++SCORE++++')
                    return speed


        for obj in objects[1][self.room][3]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["D"]:
                        self.boost = 0

        return speed

    def draw(self, screen):
        if self.life:
            pygame.draw.circle(
                screen, THECOLORS["brown"], (int(self.x), int(self.y)), self.radius
            )
        else:
            self.life = 1

    def die(self, time):
        global objects
        self.x, self.y = player_pos
        self.room = 0
        if time - self.last_d > 1:
            self.life = 0
            
            self.last_d = time
            self.hp -= 1
            
            if self.hp < 0:
                for i in Coins: 
                    objects[1][int(i)][2] = Coins[i].copy()
                self.hp = 3
                self.score = 0
            print(self.hp, "====HP====")

    def movement(self):
        if self.life:
            key = pygame.key.get_pressed()
            if player.connected:
                player.pressed = [key[pygame.K_LEFT], key[pygame.K_a], key[pygame.K_UP], key[pygame.K_w], key[pygame.K_RIGHT], key[pygame.K_d]]
                if player.pressed != player.oldpressed:
                    player.oldpressed = player.pressed
                    Server.SendKeys(player.pressed, self.nickname)

            if pygame.mouse.get_pressed()[0]:
                if time.time() - self.last_shot > 0.05 and self.pos !=pygame.mouse.get_pos():
                    self.last_shot = time.time()
                    vector = Normalize( pygame.math.Vector2(
                            self.x - pygame.mouse.get_pos()[0],
                            self.y - pygame.mouse.get_pos()[1] ))
                    if not self.connected:
                        Id = int(list(objects[3].keys())[-1])+1 if len(objects[3]) > 0 else 1
                        objects[3][str(Id)] = Bullet(
                            Id,
                            self.nickname,
                            self.room,
                            (self.x - vector.x*15, self.y - vector.y*15), 
                            pygame.math.Vector2(vector.x*(-6) + random()*0.3, vector.y*(-6) + random()*0.3))
                    else:
                        Server.CreateShot(
                            self.nickname,
                            self.room,
                            (self.x - vector.x*15, self.y - vector.y*15), 
                            pygame.math.Vector2(vector.x*(-6) + random()*0.3, vector.y*(-6) + random()*0.3))
            
            if key[pygame.K_F6]:
                if not player.connected:
                    player.connected = 1
                    Thread(target=ConnectServer).start()

            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.speed = self.Collide("L", player_speed)
                if self.speed:
                    self.x += self.speed
                    self.look = 0
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.speed = self.Collide("R", player_speed)
                if self.speed:
                    self.x += self.speed
                    self.look = 1
            if key[pygame.K_UP] or key[pygame.K_w]:
                if not self.in_air:
                    self.boost = jump_impulse
                    self.in_air = 1

            if self.boost > 0:
                self.speed = self.Collide("U", self.boost)
                if self.speed:
                    self.y += self.speed
                    self.boost -= gravity
                else:
                    self.boost -= gravity
            elif self.boost <= 0:
                if self.boost <= -18:
                    self.boost = -18
                self.in_air = 1

                self.speed = self.Collide("D", self.boost)

                if self.speed:
                    self.y += self.speed
                    self.boost -= gravity
                else:
                    self.boost -= gravity

            if self.x > Width:
                self.x = self.x // Width
                self.room += 1
            elif self.x < 0:
                self.x = Width
                self.room -= 1
    

class Object:
    def __init__(self, color, x1: int, y1: int, x2: int, y2: int):
        self.x, self.y = (x1, y1)
        self.offsets = (x2, y2)
        self.color = color
        self.rect = [self.x, self.y, self.x + self.offsets[0], self.y + self.offsets[1]]

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.offsets[0], self.offsets[1])
        )

    @property
    def pos(self):
        return self.x, self.y


class Coin:
    def __init__(self, x1: int, y1: int):
        self.x, self.y = (x1, y1)
        self.radius = 8
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]

    def draw(self, screen):
        pygame.draw.circle(
            screen, THECOLORS["yellow"], (int(self.x), int(self.y)), self.radius
        )

    @property
    def pos(self):
        return self.x, self.y

class ObjectPlayer:
    pygame.font.init()
    Nickfont = pygame.font.SysFont("Open Sans", 24)
    def __init__(self, pos, nick):
        self.x, self.y = pos
        self.radius = player_radius
        self.nickname = nick
        self.boost = 0
        self.in_air = 0
        self.room = 0
        self.keys = [0,0,0]
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]
        self.text = self.Nickfont.render(
            self.nickname, True, (0, 0, 0))
    
    def __str__(self):
        return '{"pos":'+str(list(self.pos))+', "boost":'+str(self.boost)+', "room": '+str(self.room)+', "keys":'+str(self.keys)+', "nickname":'+str(self.nickname)+'}'

    @property
    def pos(self):
        return self.x, self.y

    def die(self, time):
        global objects
        self.x, self.y = player_pos
        self.room = 0
        if time - self.last_d > 1:
            self.life = 0
            
            self.last_d = time
            self.hp -= 1
            
            if self.hp < 0:
                for i in Coins: 
                    objects[1][int(i)][2] = Coins[i].copy()
                self.hp = 3
                self.score = 0


    def draw(self, screen):
        pygame.draw.circle(
            screen, THECOLORS["blue"], (int(self.x), int(self.y)), self.radius
        )
        place = self.text.get_rect(center=(self.x, self.y + 18))
        screen.blit(self.text, place)

    def Get_rect(self):
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]
        return self.rect
    
    def Collide(self, direction, speed):

        if direction in ["D", "U", "L"]:
            speed *= -1
        if direction in ["R", "L"]:
            self.rect = [
                self.x - self.radius + speed,
                self.y - self.radius,
                self.x + self.radius + speed,
                self.y + self.radius,
                self.x + speed,
                self.y
            ]
        elif direction in ["U", "D"]:
            self.rect = [
                self.x - self.radius,
                self.y - self.radius + speed,
                self.x + self.radius,
                self.y + self.radius + speed,
                self.x,
                self.y + speed,
            ]
        dots = [
            (self.rect[0], self.rect[1]),
            (self.rect[0], self.rect[3]),
            (self.rect[2], self.rect[1]),
            (self.rect[2], self.rect[3]),
            (self.rect[4], self.rect[1]),
            (self.rect[4], self.rect[3]),
            (self.rect[0], self.rect[5]),
            (self.rect[2], self.rect[5]),
        ]
        for obj in objects[1][self.room][0]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["U", "D"]:
                        self.boost = 0
                    if direction == 'R':
                        return point[0] - (self.x + self.radius)
                    elif direction == 'L':
                        return point[2] - (self.x - self.radius)
                    elif direction == 'U':
                        return point[3] - (self.y - self.radius)
                    elif direction == 'D':
                        self.in_air = 0
                        return point[1] - (self.y + self.radius)
        for obj in objects[2]:
            if objects[2][obj] != self:
                for x, y in dots:
                    point = objects[2][obj].Get_rect()
                    if (x > point[0] and x < point[2]) and (
                            y > point[1] and y < point[3]
                    ):
                        if direction in ["U", "D"]:
                            self.boost = 0
                        if direction == 'R':
                            return point[0] - (self.x + self.radius)
                        elif direction == 'L':
                            return point[2] - (self.x - self.radius)
                        elif direction == 'U':
                            return point[3] - (self.y - self.radius)
                        elif direction == 'D':
                            self.in_air = 0
                            return point[1] - (self.y + self.radius)
        for obj in objects[1][self.room][1]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["U", "D"]:
                        self.boost = 0
                    if direction == 'R':
                        return point[0] - (self.x + self.radius)
                    elif direction == 'L':
                        return point[2] - (self.x - self.radius)
                    elif direction == 'U':
                        return point[3] - (self.y - self.radius)
                    elif direction == 'D':
                        self.in_air = 0
                        return point[1] - (self.y + self.radius)

        for obj in objects[1][self.room][3]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if direction in ["D"]:
                        self.boost = 0
        return speed
        
    def movement(self):
        if self.keys[0]:
            self.speed = self.Collide("L", player_speed)
            if self.speed:
                self.x += self.speed
                self.look = 0
        if self.keys[2]:
            self.speed = self.Collide("R", player_speed)
            if self.speed:
                self.x += self.speed
                self.look = 1
        if self.keys[1]:
            if not self.in_air:
                self.boost = jump_impulse
                self.in_air = 1
        
        if self.boost > 0:
            self.speed = self.Collide("U", self.boost)
            if self.speed:
                self.y += self.speed
                self.boost -= gravity
            else:
                self.boost -= gravity
        elif self.boost <= 0:
            if self.boost <= -18:
                self.boost = -18
            self.in_air = 1

            self.speed = self.Collide("D", self.boost)

            if self.speed:
                self.y += self.speed
                self.boost -= gravity
            else:
                self.boost -= gravity

        if self.x > Width:
            self.x = self.x // Width
        elif self.x < 0:
            self.x = Width

class Bullet:
    pygame.font.init()
    Nickfont = pygame.font.SysFont("Open Sans", 24)
    def __init__(self, Id, shooter, room, pos, vector):
        self.x, self.y = pos
        self.shooter = shooter
        self.Id = Id
        self.alive = True
        self.vector = vector
        self.radius = 2
        self.room = room
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]
    
    def __str__(self):
        return '{"Id":'+str(self.Id)+', "shooter":'+str(self.shooter)+', "room": '+str(self.room)+', "pos":'+str(list(self.pos))+', "vector":'+str(self.vector)+'}'
        
    def draw(self, screen):
        pygame.draw.circle(
            screen, THECOLORS["blue"], (int(self.x), int(self.y)), self.radius
        )
    
    @property
    def pos(self):
        return self.x, self.y

    def Get_rect(self):
        self.rect = [
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        ]
        return self.rect

    def Collide(self, vector):
        self.rect = [
            self.x - self.radius + vector.x,
            self.y - self.radius + vector.y,
            self.x + self.radius + vector.x,
            self.y + self.radius + vector.y,
            self.x + vector.x,
            self.y + vector.y,
        ]
        dots = [
            (self.rect[0], self.rect[1]),
            (self.rect[0], self.rect[3]),
            (self.rect[2], self.rect[1]),
            (self.rect[2], self.rect[3]),
            (self.rect[4], self.rect[1]),
            (self.rect[4], self.rect[3]),
            (self.rect[0], self.rect[5]),
            (self.rect[2], self.rect[5]),
        ]
        for obj in objects[1][self.room][0]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    return False

        for obj in objects[2]:
            for x, y in dots:
                point = objects[2][obj].rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    if self.shooter != objects[2][obj].nickname:
                        # objects[2][obj].die(time.time())
                        print('dead')
                        return False
        for obj in objects[1][self.room][1]:
            for x, y in dots:
                point = obj.rect
                if (x > point[0] and x < point[2]) and (
                        y > point[1] and y < point[3]
                ):
                    return False
        return True
        
    def movement(self):
        if self.Collide(self.vector) and self.alive:
            self.x += self.vector.x
            self.y += self.vector.y
            if self.x > Width:
                self.x = self.x // Width
                self.room += 1
            elif self.x < 0:
                self.x = Width
                self.room -= 1
            self.vector.y += gravity*3/144
        else:
            try:
                self.alive = False
                objects[3].pop(str(self.Id))
            except:
                pass