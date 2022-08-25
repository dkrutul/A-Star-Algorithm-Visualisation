import pygame

from consts import *
from Node import *

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("A* Algorithm Visualisation")


def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))



draw_grid_lines(window,50,WIDTH)
pygame.display.update()