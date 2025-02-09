import pygame
import math

def draw_arc(surface, color, center, radius, start_angle, end_angle, thickness=10):
    """Draw an arc on the surface."""
    rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
    # Convert angles to radians and adjust for pygame's coordinate system
    start_angle = math.radians(start_angle - 90)
    end_angle = math.radians(end_angle - 90)
    pygame.draw.arc(surface, color, rect, start_angle, end_angle, thickness)

def draw_text(surface, text, position, color, size):
    """Draw text on the surface."""
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    surface.blit(text_surface, text_rect)
