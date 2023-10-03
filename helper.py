import pygame as pg

"""Класс для помощи в обрезке картинки. Подготавливает листок, увеличивает масштаб и обрезает по координатам."""
class SpriteSheet:
    def __init__(self, file_path, scale=1):
        sheet = pg.image.load(file_path).convert_alpha() #создание пикселей главной поверхности
        w, h = sheet.get_size() #получение размера
        target_size = (int(w * scale), int(h * scale)) #подготовка к увеличению масштаба
        self.sheet = pg.transform.scale(sheet, target_size) #увеличение масштаба
        self.w, self.h = self.sheet.get_size() 

    def cut_image(self, x, y, w, h):
        return self.sheet.subsurface(x, y, w, h) #обрезка картинки по параметрам
