import pygame

import src.dots
import src.lines


CURSOR_MODES = ("move", "rotate")
PATTERNS = {
    "dots": src.dots.DotsPattern,
    "lines": src.lines.LinePattern
}


def run(pattern_name, window_size):
    pygame.init()
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Particles")
    clock = pygame.time.Clock()

    movement_mouse = pygame.Vector2()
    rotation_mouse = []
    pattern = PATTERNS[pattern_name](window_size)
    pattern.draw(window)

    while True:
        dt = clock.tick(60) / 1000  # in seconds
        draw = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    pattern.reset()
                    draw = True
                # elif event.key == pygame.K_F1:
                #     show_info = not show_info
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                movement_mouse += event.rel
            elif event.type == pygame.MOUSEMOTION and event.buttons[2]:
                end_position = pygame.Vector2(event.pos)
                start_position = end_position - event.rel
                rotation_mouse.append((start_position, end_position))

        if movement_mouse != (0, 0):
            pattern.move(movement_mouse)
            movement_mouse.update(0, 0)
            draw = True
        if rotation_mouse:
            pattern.rotate(rotation_mouse)
            rotation_mouse.clear()
            draw = True

        if draw:
            pattern.draw(window)

        # if show_info:
        #     font.render_to(
        #         window,
        #         text_margin,
        #         sim_name
        #     )
        #     font.render_to(
        #         window,
        #         text_margin + line_spacing,
        #         f"updates per second: {clock.get_fps():.0f}"
        #     )
        #     font.render_to(
        #         window,
        #         text_margin + line_spacing * 2,
        #         f"number of particles: {len(sim.particles)}"
        #     )
        #     if sim_name == "fireballs":
        #         font.render_to(
        #             window,
        #             text_margin + line_spacing * 3,
        #             f"number of emitters: {len(sim.emitters)}"
        #         )

        pygame.display.flip()
