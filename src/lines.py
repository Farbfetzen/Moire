from math import ceil

import pygame

from src.pattern import Pattern


LINE_COLOR = pygame.Color(220, 220, 220)
BACKGROUND_COLOR = pygame.Color(16, 16, 16)
LINE_WIDTH = 3
LINE_DISTANCE = 9


class LinePattern(Pattern):
    def __init__(self, window_size):
        background = pygame.Surface(window_size)
        background.fill(BACKGROUND_COLOR)

        width, height = window_size
        half_width = LINE_WIDTH // 2
        n_horizontal = ceil(width / LINE_DISTANCE)
        for i in range(n_horizontal):
            x = half_width + LINE_DISTANCE * i
            pygame.draw.line(background, LINE_COLOR, (x, 0), (x, height), LINE_WIDTH)

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground)
