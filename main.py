import pygame as pg
from settings import *
from player import Player

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
        self.player = Player('png/player_sheet.png', (100, 100))
        self.all_sprites = pg.sprite.Group() 
        self.all_sprites.add(self.player)
    
    def events(self):
        """Отслеживание событий игры."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                    and event.key == pg.K_ESCAPE):
                self.running = False
    
    def draw(self):
        """Отрисовка игры."""
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def update(self):
        """Обновление."""
        self.all_sprites.update()
    
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
