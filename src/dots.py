from math import ceil

import pygame


BACKGROUND_COLOR = pygame.Color(16, 16, 16)
CIRCLE_COLOR = pygame.Color(220, 220, 220)
CIRCLE_RADIUS = 5
CIRCLE_DISTANCE = 20


class DotsPattern:
    def __init__(self, window_size):
        self.background = pygame.Surface(window_size)
        self.background.fill(BACKGROUND_COLOR)

        width, height = window_size
        n_horizontal = ceil(width / CIRCLE_DISTANCE)
        n_vertical = ceil(height / CIRCLE_DISTANCE)
        for i in range(n_horizontal):
            x = CIRCLE_RADIUS + CIRCLE_DISTANCE * i
            for j in range(n_vertical):
                y = CIRCLE_RADIUS + CIRCLE_DISTANCE * j
                pygame.draw.circle(self.background, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

        self.foreground = self.background.copy()
        self.foreground.set_colorkey(BACKGROUND_COLOR)
        self.foreground_original = self.foreground.copy()  # base for rotations

        self.foreground_position = pygame.Vector2()
        self.foreground_rect = self.foreground.get_rect()
        self.angle = 0

    def move(self, motion):
        self.foreground_position += motion
        self.foreground_rect.topleft = self.foreground_position

    def rotate(self, mouse_position_changes):
        center = self.foreground_rect.center
        for start, end in mouse_position_changes:
            start -= center
            end -= center
            self.angle += end.angle_to(start)
        self.foreground = pygame.transform.rotate(self.foreground_original, self.angle)
        self.foreground_rect = self.foreground.get_rect(center=center)
        self.foreground_position.update(self.foreground_rect.topleft)

    def reset(self):
        self.foreground_position.update(0, 0)

    def draw(self, target_surface):
        target_surface.blit(self.background, (0, 0))
        target_surface.blit(self.foreground, self.foreground_rect)
