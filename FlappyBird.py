import pygame
import os
import random

WIDTH_SCREEN = 500
HEIGHT_SCREEN = 800

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'pipe.png')))
FLOOR_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'base.png')))
BACKGROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'bg.png')))
BIRDS_IMG = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('FB_img', 'bird3.png'))),
]
pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)



