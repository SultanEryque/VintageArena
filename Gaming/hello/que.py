#! usr/bin/env python

background_image_filename = 'Er.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = pygame.image.load(background_image_filename).convert()

font = pygame.font.SysFont("Arial", 16);
font_height = font.get_linesize()
event_text = []

while True:

    srn = 600
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[int(-srn / font_height):]

    if event.type == QUIT:
        exit()

    screen.blit(background, (0,0))

    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (255,131,250)), (0, y) )
        y -= font_height

    pygame.display.update()
