import pygame
import math
from utils import draw_arc, draw_text

class BottleDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)
        self.radius = min(width, height) // 2 - 20
        
        # Colors
        self.BLUE = (41, 128, 185)
        self.GREEN = (46, 204, 113)
        self.RED = (231, 76, 60)
        self.GRAY = (149, 165, 166)
        
    def draw(self, surface, sensor_data):
        # Draw main circle
        pygame.draw.circle(surface, (240, 240, 240), self.center, self.radius)
        pygame.draw.circle(surface, self.GRAY, self.center, self.radius, 2)
        
        # Draw water level indicator
        water_angle = 360 * (sensor_data.water_level / 100)
        draw_arc(surface, self.BLUE, self.center, self.radius - 10, 0, water_angle)
        
        # Draw battery level
        battery_width = 60
        battery_height = 30
        battery_x = self.center[0] - battery_width // 2
        battery_y = self.center[1] - self.radius + 40
        
        # Battery outline
        pygame.draw.rect(surface, self.GRAY, 
                        (battery_x, battery_y, battery_width, battery_height), 2)
        
        # Battery level fill
        battery_fill_width = (battery_width - 4) * (sensor_data.battery_level / 100)
        battery_color = self.GREEN if sensor_data.battery_level > 20 else self.RED
        pygame.draw.rect(surface, battery_color,
                        (battery_x + 2, battery_y + 2, battery_fill_width, battery_height - 4))
        
        # Draw metrics
        # Water drunk
        draw_text(surface, f"{sensor_data.water_drunk}ml", 
                 (self.center[0], self.center[1] - 40), self.BLUE, 36)
        draw_text(surface, "Water Drunk", 
                 (self.center[0], self.center[1] - 10), self.GRAY, 20)
        
        # Refills
        draw_text(surface, f"{sensor_data.refills}x", 
                 (self.center[0] - 70, self.center[1] + 40), self.GREEN, 24)
        draw_text(surface, "Refills", 
                 (self.center[0] - 70, self.center[1] + 70), self.GRAY, 16)
        
        # Waste saved
        draw_text(surface, f"{sensor_data.waste_saved}g", 
                 (self.center[0] + 70, self.center[1] + 40), self.GREEN, 24)
        draw_text(surface, "Waste Saved", 
                 (self.center[0] + 70, self.center[1] + 70), self.GRAY, 16)
        
        # Battery percentage
        draw_text(surface, f"{sensor_data.battery_level}%", 
                 (self.center[0], battery_y + 50), self.GRAY, 16)
