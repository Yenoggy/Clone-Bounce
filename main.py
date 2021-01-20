import pygame
from Objects import objects as objs
from Objects import THECOLORS
from MultiplayerAPI import ServerAPI
from Cfg import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Clone Bounce')
pygame.display.set_icon(pygame.image.load("icon.bmp"))

player = objs[0]

def Update():
    global objs
    from Objects import objects as objs

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if player.connected:
                from Player import disc, Server
                disc()
                Server.Disconnect(player.nickname)
            exit()

    screen.fill(THECOLORS['lightblue'])
    room = player.room
    for MAP in objs[1][room]:
        for obj in MAP:
            obj.draw(screen)
    for obj in objs[2]:
        if objs[2][obj].room == player.room:
            objs[2][obj].draw(screen)
    
    player.movement()
    for obj in objs[2]:
        objs[2][obj].movement()
    player.draw(screen)

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


    pygame.display.flip()
    clock.tick(40)