from math import ceil

import pygame

from src.pattern import Pattern


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
DOT_COLOR = pygame.Color(16, 16, 16)
DOT_RADIUS = 5
DOT_DISTANCE = 10


class DotsSquarePattern(Pattern):
    def __init__(self):
        width, height = pygame.display.get_window_size()
        magnification = 1.5
        background = pygame.Surface((width * magnification, height * magnification))
        background.fill(BACKGROUND_COLOR)

        n_horizontal = ceil(width / DOT_DISTANCE)
        n_vertical = ceil(height / DOT_DISTANCE)
        dot_radius_magnified = DOT_RADIUS * magnification
        dot_distance_magnified = DOT_DISTANCE * magnification
        for i in range(n_horizontal):
            x = dot_radius_magnified + dot_distance_magnified * i
            for j in range(n_vertical):
                y = dot_radius_magnified + dot_distance_magnified * j
                pygame.draw.circle(
                    background,
                    DOT_COLOR,
                    (x, y),
                    dot_radius_magnified
                )

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground, magnification)