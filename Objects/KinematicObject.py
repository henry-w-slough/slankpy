from ..GameObject import GameObject
from ..GameObject import Collision

import pygame

class KinematicObject(GameObject.GameObject):

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any GameObject that requires collision use."""
        super().__init__(width, height, *groups)


    def collision_check(self, *layers) -> None:
        """Checks for collision with the objects within the given layers. collision_type can be used to change between pixel-perfect (mask) and rectangle (rect) collision."""
        
        for layer in layers:
            
            collides = Collision.get_mask_collision(self, layer, [self])


            if collides["top"]:
                self.rect.y = collides["top"].mask_rect.y + self.mask_rect.height

            if collides["bottom"]:
                self.rect.y = collides["bottom"].mask_rect.y - self.mask_rect.height

            if collides["left"]:
                self.rect.x = collides["left"].mask_rect.x + self.mask_rect.width

            if collides["right"]:
                self.rect.x = collides["right"].mask_rect.x - self.mask_rect.width




            
