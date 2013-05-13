import pygame
import tiledtmxloader
from util import *

class Level:
    name = "Level_0"
    counter = 0
    speed = 2.0
    
    def __init__(self):
        self.world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode("maps/" + self.name + ".tmx")
        resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
        resources.load(self.world_map)

        self.renderer = tiledtmxloader.helperspygame.RendererPygame()
        self.renderer.set_camera_position_and_size(0, self.world_map.pixel_height, SCREEN_WIDTH, SCREEN_HEIGHT, "topleft")
        self.sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(resources)

    def tick(self, time):
        self.counter += self.speed * time
        
    def draw(self, screen):       
        self.renderer.set_camera_position(0, self.world_map.pixel_height - self.counter - SCREEN_HEIGHT, "topleft")
        for sprite_layer in self.sprite_layers:
            if sprite_layer.is_object_group:
                # we dont draw the object group layers
                # you should filter them out if not needed
                continue
            else:
                self.renderer.render_layer(screen, sprite_layer)

        
