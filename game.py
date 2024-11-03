import pygame
import sys  # Import sys to handle exiting

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Catch Me")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Ensure the program fully exits

    # Fill the screen with a color
    screen.fill((250, 160, 160))

    # Update the display
    pygame.display.flip()
