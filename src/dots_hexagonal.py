from math import ceil, sqrt

import pygame

from src.pattern import Pattern
import src.shared_constants as sc


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
DOT_COLOR = pygame.Color(16, 16, 16)
DOT_RADIUS = 4
DOT_DISTANCE = 12


class DotsHexagonalPattern(Pattern):
    def __init__(self):
        width, height = sc.WINDOW_SIZE
        background = pygame.Surface((width * sc.MAGNIFICATION, height * sc.MAGNIFICATION))
        background.fill(BACKGROUND_COLOR)

        dot_radius_magnified = DOT_RADIUS * sc.MAGNIFICATION
        dot_distance_magnified = DOT_DISTANCE * sc.MAGNIFICATION
        column_spacing = sqrt(3) / 2 * dot_distance_magnified  # height of equilateral triangle
        shifted_column_offset = dot_distance_magnified / 2
        n_horizontal = ceil((width * 1.5) / column_spacing) + 1
        n_vertical = ceil(height / DOT_DISTANCE) + 1

        # Make it so that there is a dot at the center of rotation:
        width_half = width * sc.MAGNIFICATION / 2
        height_half = height * sc.MAGNIFICATION / 2
        center_column_index, x_offset = divmod(
            (width_half - dot_radius_magnified),
            column_spacing
        )
        if center_column_index % 2 == 0:
            y_offset = ((height_half - dot_radius_magnified - shifted_column_offset)
                        % dot_distance_magnified)
        else:
            y_offset = (height_half - dot_radius_magnified) % dot_distance_magnified

        # Pre-compute y-coordinates because they repeat.
        y_const = dot_radius_magnified + y_offset - dot_distance_magnified
        y_coordinates = [(i * dot_distance_magnified + y_const) for i in range(n_vertical)]
        y_coordinates_shifted = [y + shifted_column_offset for y in y_coordinates]

        column_is_shifted = False
        x_const = dot_radius_magnified + x_offset - column_spacing
        for i in range(n_horizontal):
            x = i * column_spacing + x_const
            y_coords = y_coordinates_shifted if column_is_shifted else y_coordinates
            for y in y_coords:
                pygame.draw.circle(
                    background,
                    DOT_COLOR,
                    (x, y),
                    dot_radius_magnified
                )
            column_is_shifted = not column_is_shifted

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground)
