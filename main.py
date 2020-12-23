import pygame
from pygame.color import THECOLORS

from Objects import objects as objs
from Cfg import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

player = objs[0]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(THECOLORS["grey"])

    for obj in objs[1]:
        obj.draw(screen)
    player.draw(screen)
    player.movement()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption(str(round(clock.get_fps(), 2)))
