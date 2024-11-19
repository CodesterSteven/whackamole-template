import pygame
import random


def main():
    try:

        mole_x_coordinate = 0
        mole_y_coordinate = 0
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.dQUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    user_x_coordinate, user_y_coordinate = event.pos
                    cell_x = user_x_coordinate // 32
                    cell_y = user_y_coordinate // 32
                    if cell_x ==  mole_x_coordinate // 32 and cell_y == mole_y_coordinate // 32:
                        mole_x_coordinate = random.randrange(0, 640, 32)
                        mole_y_coordinate = random.randrange(0, 512, 32)

            screen.fill("light green")
            x_coordinate = 32
            y_coordinate = 32
            for i in range(20):
                pygame.draw.line(screen, 'black', (x_coordinate, 0), (x_coordinate, 512)) #starting position and ending position
                x_coordinate += 32

            for j in range(16):
                    pygame.draw.line(screen, 'black', (0, y_coordinate), (640, y_coordinate))
                    y_coordinate += 32

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x_coordinate, mole_y_coordinate)))

            pygame.display.flip()
        
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
