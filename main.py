from Math import Normalize
import pygame
from pygame.threads import Thread
from Objects import objects as objs
from Objects import THECOLORS
from MultiplayerAPI import ServerAPI
from numba import jit, cuda
from time import time
from Cfg import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clone Bounce')
pygame.display.set_icon(pygame.image.load("icon.bmp"))

player = objs[0]

def Update():
    global objs
    from Objects import objects as objs


def CreateMove():
    tickrate = pygame.time.Clock()
    while True:
        # CreateMove
        player.movement()
        for obj in objs[2].copy():
            objs[2][obj].movement()
        for booster in player.booster.copy():
            if int(time()) - player.booster[booster]['time'] > 5:
                player.booster.pop(booster)
        tickrate.tick(40)

 
def Renderer():
    global screen
    Clock = pygame.time.Clock()
    while True:
        # World Render
        screen.fill(THECOLORS['lightblue'])
        room = player.room
        for obj in objs[3].copy():
            if objs[3][obj].room == room:
                objs[3][obj].draw(screen)
        for MAP in objs[1][room]:
            for obj in MAP.copy():
                obj.draw(screen)
        for obj in objs[2].copy():
            if objs[2][obj].room == room:
                objs[2][obj].draw(screen)
        for Room in objs[1].copy():
            for obj in Room[4]:
                if not obj.alive:
                    obj.Use()
        
        player.draw(screen)

        # HUD Render
        pygame.font.init()
        hpHud = pygame.font.SysFont("Open Sans", 24)
        hpHudRender = hpHud.render(
        'HP:' + str(player.hp), True, (0, 0, 0))
        placeHp = hpHudRender.get_rect(left=10, bottom=794)
        screen.blit(hpHudRender, placeHp)

        coinHud = pygame.font.SysFont("Open Sans", 24)
        coinHudRender = coinHud.render(
            'Score: ' + str(player.score), True, (0, 0, 0))
        placeCoin = coinHudRender.get_rect(right=790, bottom=794)
        screen.blit(coinHudRender, placeCoin)

        FPSHud = pygame.font.SysFont("Open Sans", 24)
        FPSHudRender = FPSHud.render(
            'FPS: ' + str(int(Clock.get_fps())), True, (0, 0, 0))
        FPSPlace = coinHudRender.get_rect(right=400, bottom=794)
        screen.blit(FPSHudRender, FPSPlace)


        # Weapon vector Render
        vector = Normalize(pygame.math.Vector2(
                            player.x - pygame.mouse.get_pos()[0],
                            player.y - pygame.mouse.get_pos()[1] ))

        pygame.draw.line(screen, THECOLORS['black'], (player.x - vector.x*10, player.y - vector.y*10), (player.x - vector.x*18, player.y - vector.y*18), 3)
        pygame.display.flip()
        Clock.tick(144)


def BulletMove():
    Cock = pygame.time.Clock()
    while True:
        for obj in objs[3].copy():
            objs[3][obj].movement()
        Cock.tick(144)

Thread(target=BulletMove).start()
Thread(target=CreateMove).start()
Thread(target=Renderer).start()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if player.connected:
                from Player import disc, Server
                disc()
                Server.Disconnect(player.nickname)
            exit()
    clock.tick(144)

