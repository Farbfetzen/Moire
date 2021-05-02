import pygame


class Pattern:
    def __init__(self, background, foreground, magnification):
        self.background = background
        self.foreground = foreground
        self.foreground_original = foreground.copy()
        self.window_size = pygame.display.get_window_size()
        self.foreground_center = pygame.Vector2(self.window_size) * magnification / 2
        self.foreground_rect = self.foreground.get_rect(center=self.foreground_center)
        self.big_surface = pygame.Surface(self.background.get_size())
        self.angle = 0
        self.magnification = magnification

    def move(self, motion):
        self.foreground_center += motion * self.magnification
        self.foreground_rect.center = self.foreground_center

    def rotate(self, mouse_move_events, keyboard_angle):
        center = self.foreground_center / self.magnification
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
        pygame.transform.smoothscale(self.big_surface, self.window_size, target_surface)
