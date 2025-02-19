import pygame
import sys
from bottle_display import BottleDisplay
from sensor_mock import SensorData

def get_weight_input():
    # Initialize pygame if not already initialized
    if not pygame.get_init():
        pygame.init()

    # Set up the input screen
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Weight Input")

    # Initialize font
    try:
        font = pygame.font.SysFont('Arial', 32)
    except:
        font = pygame.font.Font(None, 32)  # Fallback to default font

    weight = ""
    input_active = True
    clock = pygame.time.Clock()

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and weight:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    weight = weight[:-1]
                elif event.unicode.isnumeric() and len(weight) < 3:
                    weight += event.unicode

        # Draw everything
        screen.fill((255, 255, 255))

        # Draw prompt
        prompt = font.render("Enter your weight (lbs):", True, (0, 0, 0))
        screen.blit(prompt, (50, 50))

        # Draw input
        weight_text = font.render(weight + "_" if weight else "_", True, (0, 0, 0))
        screen.blit(weight_text, (50, 100))

        pygame.display.flip()
        clock.tick(30)

    # Clean up
    pygame.display.quit()
    pygame.display.init()

    return int(weight) if weight else 150  # Default to 150 if no input

def main():
    # Get weight input first
    weight = get_weight_input()

    # Initialize Pygame
    WIDTH = 400
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Water Bottle Display")

    # Initialize components
    clock = pygame.time.Clock()
    sensor_data = SensorData()
    sensor_data.calculate_daily_target(weight)
    bottle_display = BottleDisplay(WIDTH, HEIGHT)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update sensor data
        sensor_data.update()

        # Clear screen
        screen.fill((255, 255, 255))

        # Draw bottle display
        bottle_display.draw(screen, sensor_data)

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()