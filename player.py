import pygame as pg
from helper import SpriteSheet
from pygame.math import Vector2


class Player(pg.sprite.Sprite):
    """Класс для хранения атрибутов связанных с игроком."""
    speed = 5
    def __init__(self, sheet_path, pos):
        super().__init__()
        self.sheet = SpriteSheet(sheet_path, 2)
        self.load_image()
        self.image = self.down_vector[0]
        self.rect = self.image.get_rect(center=pos)
        self.frame = 0
        self.velocity = Vector2(0, 0) #движение по векторам
        self.anim_update = 0

    def update(self):
        self.move()
        self.animation()
    
    def move(self):
        """Изменяет вектор движения игрока. Двигает игрока в направлении относительно нажатия клавиш."""
        self.velocity.update(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_d]:
            self.velocity.x = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        if keys[pg.K_s]:
            self.velocity.y = 1

        if self.velocity.length() > 1: #избежание движения по диагонали
            self.velocity.y = 0

        self.velocity *= Player.speed
        self.rect.center += self.velocity

    def load_image(self):
        """Подгружает обрезанные по сторонам векторов картинки игрока."""
        self.up_vector = []
        self.left_vector = []
        self.right_vector = []
        self.down_vector = []

        w, h = self.sheet.w // 4, self.sheet.h // 4
        
        for x in range(0, w * 4, w):
            self.down_vector.append(self.sheet.cut_image(x, 0, w, h))
            self.left_vector.append(self.sheet.cut_image(x, h, w, h))
            self.right_vector.append(self.sheet.cut_image(x, h*2, w, h))
            self.up_vector.append(self.sheet.cut_image(x, h*3, w, h))

    def animation(self, frame_len=100):
        """Анимация кадров для каждого направления."""
        time = pg.time.get_ticks()
        if time - self.anim_update > frame_len and self.velocity.length() > 0:
            self.anim_update = time

            if self.velocity.y > 0:
                self.anim_list = self.down_vector
            if self.velocity.y < 0:
                self.anim_list = self.up_vector
            if self.velocity.x > 0:
                self.anim_list = self.right_vector
            if self.velocity.x < 0:
                self.anim_list = self.left_vector
            
            self.frame = (self.frame + 1) % 4
            self.image = self.anim_list[self.frame]
