import pygame as pg
from settings import *
from player import Player

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RPG GAME')
pg.display.set_icon(pg.image.load('png/icon.png'))

player = Player('png/player_sheet.png', (100, 100))
all_sprites = pg.sprite.Group()
all_sprites.add(player)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False
    
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    
    clock.tick(60)
    pg.display.flip()

