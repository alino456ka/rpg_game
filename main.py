import pygame as pg
from settings import *
from player import Player
from world import Camera, Map
from npc import NPC


class Game():
    """Основной класс для работы игры."""
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('RPG GAME')
        pg.display.set_icon(pg.image.load('png/icon.png')) #добавление иконки у окна
        self.running = True
    
    def objects(self):
        """Добавление объектов в игру."""
        self.player = Player(self, 'png/player_sheet.png', (100, 100))
        self.walls = pg.sprite.Group()
        self.all_sprites = pg.sprite.LayeredUpdates() 
        self.all_sprites.add(self.player)
        self.map = Map(self, 'map/map.csv', 'map/rpg_tileset.png', 16)
        self.camera = Camera(self.map.w, self.map.h)
        self.npc = NPC(self, self.map.image_list[125], (440, 310), 'Как у тебя дела?')
    
    def events(self):
        """Отслеживание событий игры."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                    and event.key == pg.K_ESCAPE):
                self.running = False
    
    def draw(self):
        """Отрисовка игры."""
        self.screen.fill((255, 255, 255))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite.rect))
        # self.draw_hitbox()
        pg.display.flip()
    
    def update(self):
        """Обновление."""
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_hitbox(self):
        pg.draw.rect(self.screen, (255, 255, 255), self.camera.apply(self.player.rect))
        pg.draw.rect(self.screen, (0, 0, 0), self.camera.apply(self.player.hitbox))

    
    def run(self):
        """Игровой цикл."""
        while self.running:
            self.clock.tick(60)
            self.events()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.objects()
    game.run()
