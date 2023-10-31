import pygame as pg
import pygame.freetype as ft
from settings import *


class NPC(pg.sprite.Sprite):
    """Класс неигровых персонажей."""
    def __init__(self, game, image, pos, text):
        self._layer = BG_LAYER
        groups = game.all_sprites, game.walls
        super().__init__(groups)
        self.game = game
        self.image = image
        self.text = text
        self.rect = image.get_rect(center=pos)
        self.message = Message(game, text, (pos[0]+85, pos[1]-40))

    def update(self):
        """Отображает сообщение при столкновении."""
        if self.rect.colliderect(self.game.player):
            self.message.send()
        elif self.message.groups():
            self.message.delete()


    
class Message(pg.sprite.Sprite):
    """Класс сообщений."""
    def __init__(self, game, text, pos, font=None):
        self._layer = MS_LAYER
        super().__init__()
        self.game = game
        self.text = text
        self.font = ft.Font(font, 18)
        text_surf, text_rect = self.font.render(self.text)
        self.image = pg.Surface((text_rect.w + 20, text_rect.h + 20), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.border = pg.Rect((0, 0), self.rect.size)
        self.text_pos = (10, 10)
        self.screen_text = ''
        self.frame = 0

    def send(self):
        """Отрисовывает сообщение и пишет текст."""
        self.frame += 0.3
        self.screen_text = self.text[:int(self.frame)]
        self.add(self.game.all_sprites)
        text_surf, text_rect = self.font.render(self.screen_text, (100, 46, 122))
        self.image.fill((0, 0, 0, 0))
        self.image.blit(text_surf, self.text_pos)
        pg.draw.rect(self.image, (100, 46, 122), self.border, width=5, border_radius=10)
        
    def delete(self):
        self.screen_text = ''
        self.frame = 0
        self.kill()