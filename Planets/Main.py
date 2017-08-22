#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from Earth import Earth
from Sun import *
from pygame import *
import os

# Объявляем переменные

WIN_WIDTH = 1280  # Ширина создаваемого окна
WIN_HEIGHT = 720  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("ILITA!")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    bg = image.load("%s/pictures/kosmos.jpg" % ICON_DIR)

    sun = Sun(560, 320)     # Объявляем о существовании солнышка с координатами 560, 320
    earth = Earth(860, 320)

    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        sun.draw(screen)    # Солнышко рисуй
        earth.update()      # Обновляй по апдейту землю
        earth.draw(screen)

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()

