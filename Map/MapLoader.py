
import json
import pygame
from ..GameObject import KinematicObject


def load_map(src:str) -> dict:
    try:
        with open(src) as data:
            return json.load(data)
    except Exception as e:
        print(f"ERROR: MapLoader: load_map: {e}")
        return {}
    

def map_to_group(map:dict) -> pygame.sprite.Group:

    group = pygame.sprite.Group()

    for layer in map["layers"]:
        for index, tile_id in enumerate(layer["data"]):

            x = (index % layer["width"]) * (map["tilewidth"])
            y = (index // layer["height"]) * (map["tileheight"])

            t = KinematicObject.KinematicObject(map["tilewidth"], map["tileheight"], group)
            t.set_position(x, y)
            t.sprite.add_sprites("tiles.png", "tiles", 2, 2)
            t.set_sprite("tiles", tile_id-1)


    return group

