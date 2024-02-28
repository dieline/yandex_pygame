from settings import *
import pygame

text_map = [[1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
            [1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
            [1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
            [1, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]]
world_map = dict()
mini_map = set()
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != 0:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
            elif char == 5:
                world_map[(i * TILE, j * TILE)] = 5
