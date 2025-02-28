# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)
        myfont = pygame.font.Font("FreeMono.ttf", 50, bold=True, italic=True)
        draw_text(screen, 'Sample text!', myfont, config.BLACK, 350, 200)

        pygame.display.flip()

        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

def draw_text(screen, text, myfont, color, x, y):
    mytext = myfont.render(text, True, color)
    screen.blit(mytext, (x, y))

if __name__ == '__main__':
    main()