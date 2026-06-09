import pygame


class Sprite():
    def __init__(self, width:float, height:float) -> None:
        #right now this is just for SOC, I need to reference an original unchanged image in 
        #game_object.transform, and so I wanted to add this class to start the sprite additions
        self.sprite = pygame.Surface((width, height))