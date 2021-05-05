from math import ceil

import pygame

from src.pattern import Pattern
import src.shared_constants as sc


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
LINE_COLOR = pygame.Color(16, 16, 16)
LINE_WIDTH = 4
LINE_DISTANCE = 8


class LinePattern(Pattern):
    def __init__(self):
        width, height = sc.WINDOW_SIZE
        background = pygame.Surface((width * sc.MAGNIFICATION, height * sc.MAGNIFICATION))
        background.fill(BACKGROUND_COLOR)

        line_width_magnified = int(LINE_WIDTH * sc.MAGNIFICATION)
        line_distance_magnified = LINE_DISTANCE * sc.MAGNIFICATION
        half_width = line_width_magnified // 2
        n_horizontal = ceil(width / LINE_DISTANCE)
        height_magnified = height * sc.MAGNIFICATION
        for i in range(n_horizontal):
            x = half_width + line_distance_magnified * i
            pygame.draw.line(
                background,
                LINE_COLOR,
                (x, 0),
                (x, height_magnified),
                line_width_magnified
            )

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground)
