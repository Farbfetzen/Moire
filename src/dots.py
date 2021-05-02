from math import ceil

import pygame


BACKGROUND_COLOR = pygame.Color(16, 16, 16)
CIRCLE_COLOR = pygame.Color(220, 220, 220)
CIRCLE_RADIUS = 3
CIRCLE_DISTANCE = 10


class DotsPattern:
    def __init__(self, window_size):
        width, height = window_size
        self.background = pygame.Surface(window_size)
        self.background.fill(BACKGROUND_COLOR)

        n_horizontal = ceil(width / CIRCLE_DISTANCE)
        n_vertical = ceil(height / CIRCLE_DISTANCE)
        for i in range(n_horizontal):
            x = CIRCLE_RADIUS + CIRCLE_DISTANCE * i
            for j in range(n_vertical):
                y = CIRCLE_RADIUS + CIRCLE_DISTANCE * j
                pygame.draw.circle(self.background, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

        self.foreground_original = self.background.copy()
        self.foreground_original.set_colorkey(BACKGROUND_COLOR)
        self.foreground = self.foreground_original.copy()

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
        self.foreground = self.foreground_original.copy()
        self.foreground_rect = self.foreground.get_rect()
        self.foreground_position.update(self.foreground_rect.topleft)
        self.angle = 0

    def draw(self, target_surface):
        target_surface.blit(self.background, (0, 0))
        target_surface.blit(self.foreground, self.foreground_rect)
