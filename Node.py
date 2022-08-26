import pygame
from consts import *


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * NODE_SIZE
        self.y = col * NODE_SIZE
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_checked(self):
        return self.color == RED

    def is_inside_queue(self):
        return self.color == GREEN

    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def set_reset_color(self):
        self.color = WHITE

    def set_checked(self):
        self.color = RED

    def set_in_queue(self):
        self.color = GREEN

    def set_wall(self):
        self.color = BLACK

    def set_start(self):
        self.color = ORANGE

    def set_end(self):
        self.color = TURQUOISE

    def set_path(self):
        self.color = PURPLE

    def update_neighbors(self, grid):
        pass

    def draw_node(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, NODE_SIZE, NODE_SIZE))

    def __lt__(self, other):
        return False


def heuristic_function(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    return abs(x1 - x2) + abs(y1 - y2)


def create_list_of_nodes():
    grid = []

    for i in range(NUMBER_OF_NODES_IN_A_ROW):
        grid.append([])
        for j in range(NUMBER_OF_NODES_IN_A_ROW):
            node = Node(i, j)
            grid[i].append(node)

    return grid


def get_clicked_pos(pos):
    y, x = pos

    row = y // NODE_SIZE
    col = x // NODE_SIZE

    return row, col













