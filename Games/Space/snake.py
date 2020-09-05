import random
import math
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()


def drawGrid(w, rows, surface):
    sizeBtwn = w / rows

    x = -1
    y = -1
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (254, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (254, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global rows, width
    width = 500
    rows = 20
    win = pygame.display.set_mode((500, 500))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
