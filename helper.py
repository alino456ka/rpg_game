import pygame as pg


class SpriteSheet:
    def __init__(self, file_path):
        self.sheet = pg.image.load(file_path).convert_alpha()
        
    def cut_image(self, x, y, w, h):
        return self.sheet.subsurface(x, y, w, h)