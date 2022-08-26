import pygame

from consts import *
from Node import *

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("A* Algorithm Visualisation")


def draw_grid_lines():
    for i in range(NUMBER_OF_NODES_IN_A_ROW):
        pygame.draw.line(window, GREY, (0, i * NODE_SIZE), (WIDTH, i * NODE_SIZE))
    for j in range(NUMBER_OF_NODES_IN_A_ROW):
        pygame.draw.line(window, GREY, (j * NODE_SIZE, 0), (j * NODE_SIZE, WIDTH))


draw_grid_lines()
pygame.display.update()
