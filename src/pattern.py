import pygame


class Pattern:
    def __init__(self, background, foreground):
        self.background = background
        self.foreground = foreground
        self.foreground_original = foreground.copy()
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
