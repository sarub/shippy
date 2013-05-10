import pygame
from util import *

class Level:
    name = "Level - "
    background = None
    counter = 0
    speed = 2.0
    
    def __init__(self):
        self.background = pygame.Surface((WIDTH, HEIGHT + 32)).convert()

    def tick(self, time):
        self.counter += self.speed * time
        tile = tileAt((0, 0, 32, 32), "art/tileset.png")    
        
        self.background.fill((0, 0, 0))
        for x in range(WIDTH/32):
            for y in range(HEIGHT/32 + 2):
                self.background.blit(tile, (x*32, (y-1)*32 + (self.counter % 16)))


