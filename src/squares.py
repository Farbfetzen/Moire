from math import ceil

import pygame

from src.pattern import Pattern


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
LINE_COLOR = pygame.Color(16, 16, 16)
LINE_WIDTH = 2
LINE_DISTANCE = 4


class SquarePattern(Pattern):
    def __init__(self):
        width, height = pygame.display.get_window_size()
        magnification = 1.5
        background = pygame.Surface((width * magnification, height * magnification))
        background.fill(BACKGROUND_COLOR)

        line_width_magnified = int(LINE_WIDTH * magnification)
        line_distance_magnified = LINE_DISTANCE * magnification
        half_width = line_width_magnified // 2
        height_magnified = height * magnification
        width_magnified = width * magnification
        n = ceil(max(width, height) / LINE_DISTANCE)
        for i in range(n):
            xy = half_width + line_distance_magnified * i
            pygame.draw.line(
                background,
                LINE_COLOR,
                (xy, 0),
                (xy, height_magnified),
                line_width_magnified
            )
            pygame.draw.line(
                background,
                LINE_COLOR,
                (0, xy),
                (width_magnified, xy),
                line_width_magnified
            )

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground, magnification)
