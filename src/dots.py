from math import ceil

import pygame

from src.pattern import Pattern


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
CIRCLE_COLOR = pygame.Color(16, 16, 16)
CIRCLE_RADIUS = 5
CIRCLE_DISTANCE = 10


class DotsPattern(Pattern):
    def __init__(self):
        width, height = pygame.display.get_window_size()
        magnification = 1.5  # good compromise between speed and smoothness
        background = pygame.Surface((width * magnification, height * magnification))
        background.fill(BACKGROUND_COLOR)

        n_horizontal = ceil(width / CIRCLE_DISTANCE)
        n_vertical = ceil(height / CIRCLE_DISTANCE)
        circle_radius_magnified = CIRCLE_RADIUS * magnification
        circle_distance_magnified = CIRCLE_DISTANCE * magnification
        for i in range(n_horizontal):
            x = circle_radius_magnified + circle_distance_magnified * i
            for j in range(n_vertical):
                y = circle_radius_magnified + circle_distance_magnified * j
                pygame.draw.circle(
                    background,
                    CIRCLE_COLOR,
                    (x, y),
                    circle_radius_magnified
                )

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground, magnification)
