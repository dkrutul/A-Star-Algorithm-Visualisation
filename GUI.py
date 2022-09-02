import pygame
from consts import *
from Node import *
from algorithm import *

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("A* Algorithm Visualisation")


def draw_grid_lines():
    for i in range(NUMBER_OF_NODES_IN_A_ROW):
        pygame.draw.line(window, GREY, (0, i * NODE_SIZE), (WIDTH, i * NODE_SIZE))
    for j in range(NUMBER_OF_NODES_IN_A_ROW):
        pygame.draw.line(window, GREY, (j * NODE_SIZE, 0), (j * NODE_SIZE, WIDTH))


def draw(grid):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw_node(window)

    draw_grid_lines()
    pygame.display.update()


def main():
    main_grid = create_list_of_nodes()

    start = None
    end = None
    run = True

    started = False

    while run:
        draw(main_grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)
            node = main_grid[row][col]

            if pygame.mouse.get_pressed()[0]:

                if not start and node is not end:
                    start = node
                    start.set_start()

                elif not end and node is not start:
                    end = node
                    end.set_end()

                elif node is not start and node is not end:
                    node.set_wall()

            if pygame.mouse.get_pressed()[2]:
                if node is start:
                    start = None
                elif node is end:
                    end = None
                node.set_reset_color()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in main_grid:
                        for node in row:
                            node.update_neighbors(main_grid)

                    a_star_alg(lambda: draw(main_grid), main_grid, start, end)

                if event.key is pygame.K_c:
                    start = None
                    end = None
                    started = False
                    main_grid = create_list_of_nodes()

    pygame.quit()


if __name__ == '__main__':
    main()
