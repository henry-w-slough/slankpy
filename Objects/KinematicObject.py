from ..GameObject import GameObject
from ..GameObject import Collision

import pygame

class KinematicObject(GameObject.GameObject):

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any GameObject that requires collision use."""
        super().__init__(width, height, *groups)




            
