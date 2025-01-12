import pygame
from config import *

pygame.font.init()
FONT = pygame.font.Font("res/fonts/m5x7.ttf", 16)

def draw_centered_text(text, screen, color = "black", antialias = False):
    text = FONT.render(text, antialias, color)
    text_rect = text.get_rect(center=(GAME_WIDTH / 2, GAME_HEIGHT / 2))
    screen.blit(text, text_rect)

def draw_text(text, screen, pos = pygame.Vector2(0, 0), color = "black", antialias = False):
    text = FONT.render(text, antialias, color)
    text_pos = (pos.x, pos.y - 4)
    screen.blit(text, text_pos)