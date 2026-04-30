
import json
import pygame
from ..GameObject import GameObject


def load_map(src:str) -> dict:
    """Loads the JSON map file provided and returns a dictionary of the data in it."""
    try:
        with open(src) as data:
            return json.load(data)
    except Exception as e:
        print(f"ERROR: MapLoader: load_map: {e}")
        return {}
    

def map_to_group(map:dict, tile_spritesheet_src:str, tile_animation_name:str, tile_rows:int, tile_columns:int, tile_filter:list[int]=[]) -> pygame.sprite.Group:
    """Takes in a dictionary of map data and returns a Group of loaded tiles. index_filter arg will not allow the given values to be added if any values are given."""

    group = pygame.sprite.Group()

    for layer in map["layers"]:
        for index, tile_id in enumerate(layer["data"]):


            if tile_id in tile_filter:
                continue
        
                    
            x = (index % layer["width"]) * (map["tilewidth"])
            y = (index // layer["height"]) * (map["tileheight"])

            if tile_id != 0:
                t = GameObject.GameObject(map["tilewidth"], map["tileheight"], group)
                t.set_position(x, y)
                t.sprite.add_sprites(tile_spritesheet_src, tile_animation_name, tile_rows, tile_columns)
                t.set_sprite(tile_animation_name, tile_id-1)


    return group

