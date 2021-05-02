import pygame
import pygame.freetype

import src.dots
import src.lines


CURSOR_MODES = ("move", "rotate")
PATTERNS = {
    "dots": src.dots.DotsPattern,
    "lines": src.lines.LinePattern
}


class App:
    def __init__(self, pattern_name, window_size):
        pygame.init()
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Particles")
        self.clock = pygame.time.Clock()

        self.pattern_name = pattern_name
        self.pattern = PATTERNS[pattern_name]()
        self.pattern.draw(self.window)

        self.window_center = pygame.Vector2(self.window.get_rect().center)
        self.show_info = True
        self.font = pygame.freetype.SysFont(("consolas", "inconsolata", "monospace"), 16)
        self.font.fgcolor = pygame.Color((220, 220, 220))
        self.font.bgcolor = pygame.Color((16, 16, 16))
        self.font.pad = True
        self.line_spacing = pygame.Vector2(0, self.font.get_sized_height())
        self.text_margin = pygame.Vector2(5, 5)
        _, self.info_rect = self.font.render(
            f" translation: -{window_size[0]}, -{window_size[1]} "  # maximum width
        )
        self.info_rect.height = self.text_margin.y * 2 + self.line_spacing.y * 3
        self.info_rect.topleft = self.text_margin
        self.info_surface = pygame.Surface(self.info_rect.size)
        self.update_info()

    def run(self):
        movement_mouse = pygame.Vector2()
        rotation_mouse = []

        while True:
            dt = self.clock.tick(60) / 1000  # in seconds
            draw_pattern = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        self.pattern.reset()
                        draw_pattern = True
                    elif event.key == pygame.K_F1:
                        self.show_info = not self.show_info
                        draw_pattern = True
                elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                    movement_mouse += event.rel
                elif event.type == pygame.MOUSEMOTION and event.buttons[2]:
                    end_position = pygame.Vector2(event.pos)
                    start_position = end_position - event.rel
                    rotation_mouse.append((start_position, end_position))

            if movement_mouse != (0, 0):
                self.pattern.move(movement_mouse)
                movement_mouse.update(0, 0)
                draw_pattern = True
            if rotation_mouse:
                self.pattern.rotate(rotation_mouse)
                rotation_mouse.clear()
                draw_pattern = True

            if draw_pattern:
                self.pattern.draw(self.window)
                self.update_info()

            if self.show_info:
                self.window.blit(self.info_surface, self.info_rect)

            pygame.display.flip()

    def update_info(self):
        self.info_surface.fill(self.font.bgcolor)
        pygame.draw.rect(
            self.info_surface,
            self.font.fgcolor,
            self.info_surface.get_rect(),
            1
        )
        self.font.render_to(
            self.info_surface,
            self.text_margin,
            f"name: {self.pattern_name}"
        )
        translation = (pygame.Vector2(self.pattern.foreground_rect.center)
                       / self.pattern.magnification
                       - self.window_center)
        self.font.render_to(
            self.info_surface,
            self.text_margin + self.line_spacing,
            f"translation: {int(translation.x)}, {int(translation.y)}"
        )
        self.font.render_to(
            self.info_surface,
            self.text_margin + self.line_spacing * 2,
            f"angle: {self.pattern.angle:.1f}°"
        )
