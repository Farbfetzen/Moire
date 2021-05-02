from math import ceil

import pygame

from src.pattern import Pattern


BACKGROUND_COLOR = pygame.Color(16, 16, 16)
CIRCLE_COLOR = pygame.Color(220, 220, 220)
CIRCLE_RADIUS = 3
CIRCLE_DISTANCE = 10


class DotsPattern(Pattern):
    def __init__(self, window_size):
        background = pygame.Surface(window_size)
        background.fill(BACKGROUND_COLOR)

        width, height = window_size
        n_horizontal = ceil(width / CIRCLE_DISTANCE)
        n_vertical = ceil(height / CIRCLE_DISTANCE)
        for i in range(n_horizontal):
            x = CIRCLE_RADIUS + CIRCLE_DISTANCE * i
            for j in range(n_vertical):
                y = CIRCLE_RADIUS + CIRCLE_DISTANCE * j
                pygame.draw.circle(background, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground)
