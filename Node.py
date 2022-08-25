from consts import *
from GUI import *


class Node:
    def __init__(self, row, col, node_size, total_rows):
        self.row = row
        self.col = col
        self.x = row * WIDTH
        self.y = col * HEIGHT
        self.color = WHITE
        self.neighbors = []
        self.node_size = node_size
        self.total_rows = total_rows

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

    def draw_node(self, win: window):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.node_size, self.node_size))

    def __lt__(self, other):
        return False


def h_func(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def create_list_of_nodes(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid








