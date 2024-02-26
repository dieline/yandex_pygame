from settings import *
import pygame

text_map = [
    'wwwwwwwwwwww',
    'w..........w',
    'w...w......w',
    'w...w......w',
    'w...w......w',
    'w.......wwww',
    'wwww.......w',
    'wwwwwwwwwwww'
]
world_map = set()
mini_map = set()
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'w':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
