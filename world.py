import pygame as pg
import csv


class Map():
    def __init__(self):
        pass

    def import_csv(self, csv_path):
        with open(csv_path) as file:
            read_file = csv.reader(csv_path)
            data = list(read_file)
        return data
    
    def load_images(self, image_path):
        images_list = []
        image_map = pg.image.load(image_path).convert()
        w, h = image_map.get_size()
        

