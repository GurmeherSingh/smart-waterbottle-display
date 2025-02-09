import pygame
import sys
from bottle_display import BottleDisplay
from sensor_mock import SensorData

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up display
    WIDTH = 400
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Water Bottle Display")
    
    # Initialize components
    clock = pygame.time.Clock()
    sensor_data = SensorData()
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
