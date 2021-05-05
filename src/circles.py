from math import ceil

import pygame

from src.pattern import Pattern
import src.shared_constants as sc


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
CIRCLE_COLOR = pygame.Color(16, 16, 16)
CIRCLE_WIDTH = 4
CIRCLE_RADIUS_INCREMENT = 8  # difference in radii between two circles


class CirclesPattern(Pattern):
    def __init__(self):
        width, height = sc.WINDOW_SIZE
        background = pygame.Surface((width * sc.MAGNIFICATION, height * sc.MAGNIFICATION))
        background.fill(BACKGROUND_COLOR)
        width_magnified = round(CIRCLE_WIDTH * sc.MAGNIFICATION)
        radius_increment_magnified = CIRCLE_RADIUS_INCREMENT * sc.MAGNIFICATION
        center = (width / 2 * sc.MAGNIFICATION, height / 2 * sc.MAGNIFICATION)
        n_circles = ceil(max(width, height) / CIRCLE_RADIUS_INCREMENT)
        for i in range(n_circles):
            pygame.draw.circle(
                background,
                CIRCLE_COLOR,
                center,
                i * radius_increment_magnified,
                width_magnified
            )

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground)
