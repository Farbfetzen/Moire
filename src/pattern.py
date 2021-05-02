import pygame


class Pattern:
    def __init__(self, background, foreground, magnification):
        self.background = background
        self.foreground = foreground
        self.foreground_original = foreground.copy()
        self.foreground_position = pygame.Vector2()
        self.foreground_rect = self.foreground.get_rect()
        self.big_surface = pygame.Surface(self.background.get_size())
        self.angle = 0
        self.window_size = pygame.display.get_window_size()
        self.magnification = magnification

    def move(self, motion):
        self.foreground_position += motion * self.magnification
        self.foreground_rect.topleft = self.foreground_position

    def rotate(self, mouse_movement):
        center = pygame.Vector2(self.foreground_rect.center) / self.magnification
        for start, end in mouse_movement:
            start -= center
            end -= center
            self.angle += end.angle_to(start)
        self.angle %= 360
        self.foreground = pygame.transform.rotate(self.foreground_original, self.angle)
        self.foreground_rect = self.foreground.get_rect(center=center * self.magnification)
        self.foreground_position.update(self.foreground_rect.topleft)

    def reset(self):
        self.foreground = self.foreground_original.copy()
        self.foreground_rect = self.foreground.get_rect()
        self.foreground_position.update(self.foreground_rect.topleft)
        self.angle = 0

    def draw(self, target_surface):
        self.big_surface.blit(self.background, (0, 0))
        self.big_surface.blit(self.foreground, self.foreground_rect)
        pygame.transform.smoothscale(self.big_surface, self.window_size, target_surface)
