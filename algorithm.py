from GUI import *
from Node import *
from queue import PriorityQueue


def restore_path(came_from, current, draw_end_path):
    while current in came_from:
        current = came_from[current]
        current.set_path()
        draw_end_path()


def a_star_alg(draw_alg, grid, start, end):
    count = 0
    p_queue = PriorityQueue()
    p_queue.put((0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic_function(start.get_pos(), end.get_pos())

    open_set = {start}

    while not p_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = p_queue.get()[2]
        open_set.remove(current)

        if current == end:
            restore_path(came_from, end, draw_alg)
            end.set_end()
            start.set_start()

            return True

        for neighbor in current.neighbors:
            temp_n_score = g_score[current] + 1

            if temp_n_score < g_score[neighbor]:
                g_score[neighbor] = temp_n_score
                f_score[neighbor] = temp_n_score + heuristic_function(neighbor.get_pos(), end.get_pos())
                came_from[neighbor] = current
                if neighbor not in open_set:
                    count += 1
                    p_queue.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    neighbor.set_in_queue()

        draw_alg()

        if current != start:
            current.set_checked()

    return False
