#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

WIDTH = 50
HEIGHT = 50
COLOR = "#FF6262"
SUN_MASS = 360000

class Sun(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.startX = x  # Начальная позиция солнышка
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load("pictures/sun.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))