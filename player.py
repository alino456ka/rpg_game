import pygame as pg
from helper import SpriteSheet


class Player(pg.sprite.Sprite):
    def __init__(self, sheet_path, pos):
        super().__init__()
        self.sheet = SpriteSheet(sheet_path)
        self.image = self.sheet.cut_image(0, 0, 32, 32)
        self.rect = self.image.get_rect(center=pos)
        