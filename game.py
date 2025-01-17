import sys
from utils import *


class Game: # Create Game Class
    def __init__(self):
        # All things needed to setup in the beginning
        # Resizable: scales game but keeps game resolution so coords are still pixel perfect!
        self.game_screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
        pygame.display.set_caption("Pixel Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def run(self):
        # Do all the updates
        while self.running:

            # pygame events handling
            for event in pygame.event.get():

                # Make game closable
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Main game loop


            # Draw loop
            self.draw()

            # Ending loop
            self.clock.tick(FPS)  # Sets FPS
            self.dt = self.clock.tick(FPS)


    def draw(self):
        # Draw loop
        self.game_screen.fill("white") # Cleaning screen to be able to draw new things!

        # First message!:
        draw_centered_text("Hello, Game!", self.game_screen) # the second argument tells Pygame on which so called surface the text is drawn on to

        # Updating screen and clock
        pygame.display.update()
