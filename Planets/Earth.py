#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *


WIDTH = 50
HEIGHT = 50
COLOR = "#FF6262"
EARTH_MASS = 360



class Earth(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        self.xvel = 0  # начальная скорость(проекция X)
        self.yvel = 20  # начальная скорость(проекция Y)
        self.xacc = 0  # начальное ускорение(проекция X)
        self.yacc = 0  # начальное ускорение(проекция Y)

        self.startX = x  # Начальная позиция земли
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))

        self.image = image.load("pictures/earth.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self):   # Обновляет картинку
        xx = float(self.rect.x - 560)   # Здесь описаны законы движения земли(сила притяжения) !!!!!
        yy = float(self.rect.y - 320)   # расстояние от солнышка до земли по у координате
        R = (xx * xx + yy * yy) ** 0.5  # Очевидно, расстояние
        r = int(R)

        xacc = -100000 * xx / R ** 3    # Закон изменения ускорения
        yacc = -100000 * yy / R ** 3

        self.xvel += xacc   # Изменение скорости
        self.yvel += yacc

        self.rect.x += self.xvel    # Изменение координаты
        self.rect.y += self.yvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
