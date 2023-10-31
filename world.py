import pygame as pg
import csv
from settings import *


class Map():
    """Класс карты. Подготавливает тайлы."""
    ID_TILES = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
                69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 227, 118,
                119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]
    
    def __init__(self, game, csv_path, image_path, image_tile_size, space=0):
        data_list = self.import_csv(csv_path)
        self.image_list = self.load_images(image_path, image_tile_size, space)
        self._load_tiles(game, data_list, self.image_list)
        self.w = len(data_list[0]) * TILE_SIZE
        self.h = len(data_list) * TILE_SIZE

    def import_csv(self, csv_path):
        """Считывает csv файл."""
        with open(csv_path) as file:
            read_file = csv.reader(file)
            data = list(read_file)

        return data
    
    def load_images(self, image_path, image_tile_size, space):
        """Подготавливает картинки для будущих тайлов."""
        images_list = []
        image_map = pg.image.load(image_path).convert()
        if image_tile_size != TILE_SIZE:
            scale = TILE_SIZE // image_tile_size
            space *= scale
            cur_size = image_map.get_size()
            target_size = tuple(i * scale for i in cur_size)
            image_map = pg.transform.scale(image_map, target_size)
        w, h = image_map.get_size()

        for y in range(0, h, TILE_SIZE + space):
            for x in range(0, w, TILE_SIZE + space):
                tile = image_map.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                images_list.append(tile)

        return images_list

    def _load_tiles(self, game, data, image_list):
        """Распределяет тайлы по карте."""
        for y, row in enumerate(data):
            for x, index in enumerate(row):
                collidable = int(index) in Map.ID_TILES
                Tile(game, x, y, image_list[int(index)], collidable)



class Tile(pg.sprite.Sprite):
    """Класс тайлов."""
    def __init__(self, game, x, y, image, wall_check=False):
        self._layer = BG_LAYER
        if wall_check:
            groups = game.all_sprites, game.walls
        else:
            groups = game.all_sprites
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE



class Camera:
    """Класс камеры."""
    def __init__(self, map_w, map_h):
        self.shift = (0, 0)
        self.map_w = map_w
        self.map_h = map_h

    def apply(self, space_rect):
        """Применяет передвижение."""
        return space_rect.move(self.shift)

    def update(self, target):
        """Обновляет координаты для перемещения камеры."""
        x = WIDTH // 2 - target.rect.x
        y = HEIGHT // 2 - target.rect.y

        x = min(x, 0)
        y = min(y, 0)
        x = max(x, WIDTH - self.map_w)
        y = max(y, HEIGHT - self.map_h)

        self.shift = (x, y)
    
