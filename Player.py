import pygame
from Cfg import *
from pygame.color import THECOLORS


def upd():
    global objects
    from Objects import objects


objects = []


class player:
    def __init__(self):
        self.radius = player_radius
        self.x, self.y = player_pos
        self.rect = [
            (self.x, self.y),
            (self.x + self.radius * 2, self.y + self.radius * 2),
        ]
        self.look = player_look
        self.in_air = 0
        self.is_death = is_death
        self.death_count = death_count
        self.is_reborn = is_reborn
        self.reborn_count = reborn_count
        self.boost = 0

    @property
    def pos(self):
        return self.x, self.y

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
        for obj in objects[1]:
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
        return speed

    def draw(self, screen):
        pygame.draw.circle(
            screen, THECOLORS["brown"], (int(self.x), int(self.y)), self.radius
        )

    def movement(self):
        key = pygame.key.get_pressed()
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
        elif self.x < 0:
            self.x = Width


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

    # def Collide(self, obj):
    #     for point in obj.rect:
    #         if point > self.x and point < self.x + self.offsets[0] and point > self.y and point < self.y + self.offsets[1]:
    #             return True
    #     return False
