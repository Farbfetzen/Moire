import pygame

import src.shared_constants as sc


class Pattern:
    def __init__(self, background, foreground):
        self.background = background
        self.foreground = foreground
        self.foreground_original = foreground.copy()
        self.foreground_center = pygame.Vector2(sc.WINDOW_SIZE) * sc.MAGNIFICATION / 2
        self.foreground_rect = self.foreground.get_rect(center=self.foreground_center)
        self.big_surface = pygame.Surface(self.background.get_size())
        self.angle = 0

    def move(self, motion):
        self.foreground_center += motion * sc.MAGNIFICATION
        self.foreground_rect.center = self.foreground_center

    def rotate(self, mouse_move_events, keyboard_angle):
        center = self.foreground_center / sc.MAGNIFICATION
        for event in mouse_move_events:
            end = pygame.Vector2(event.pos) - center
            start = end - event.rel
            self.angle += end.angle_to(start)
        self.angle += keyboard_angle
        self.angle %= 360
        self.foreground = pygame.transform.rotate(self.foreground_original, self.angle)
        self.foreground_rect = self.foreground.get_rect(center=self.foreground_center)

    def reset(self):
        self.foreground = self.foreground_original.copy()
        self.foreground_rect = self.foreground.get_rect()
        self.foreground_center.update(self.foreground_rect.center)
        self.angle = 0

    def draw(self, target_surface):
        self.big_surface.blit(self.background, (0, 0))
        self.big_surface.blit(self.foreground, self.foreground_rect)
        pygame.transform.smoothscale(self.big_surface, sc.WINDOW_SIZE, target_surface)
        # Here's why I decided to use smoothscale and enlarged surfaces:
        # I want antialiased pictures. Normally that means I have to use pixel
        # alpha. However, when blitting an image with per pixel alpha onto
        # another, there are edge artifacts because the antialiased edges
        # contain part of the background. My solution: Use enlarged images
        # with colorkey and no per pixel alpha. Rotate and combine the big
        # images and then smoothscale them down to window size, thus blurring
        # the staircase edges. Rotating the larger images is noticeably slower
        # but the performance hit is not too important in this app. I found
        # that a magnification of 1.5 works well for this purpose. More than
        # 1.2 is required for a good looking result and a magnification of 2
        # makes it too slow.
