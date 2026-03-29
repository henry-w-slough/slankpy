from ..GameObject import GameObject
from ..GameObject import Collision

import pygame

class KinematicObject(GameObject.GameObject):

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any GameObject that requires collision use."""
        super().__init__(width, height, *groups)


    def collision_check(self, *layers) -> dict:
        """Checks for collision with the objects within the given layers. collision_type can be used to change between pixel-perfect (mask) and rectangle (rect) collision."""

        collisions = {"top": False, "bottom": False, "left": False, "right": False}
        
        for layer in layers:
        
            #checks if there is rect overlap before the less efficient mask checks
            if not pygame.sprite.spritecollide(self, layer, False): #type: ignore
                continue

            for obj in pygame.sprite.spritecollide(self, layer, False, pygame.sprite.collide_mask):  # type: ignore

                if obj == self:
                    continue

                mask_rect = Collision.get_mask_rect(self.rect, self.mask)
                obj_mask_rect = Collision.get_mask_rect(obj.rect, obj.mask)

                overlap_x, overlap_y = Collision.get_mask_overlap(mask_rect, obj_mask_rect)

                if overlap_x <= 0 or overlap_y <= 0:
                    continue

                if overlap_x < overlap_y:
                    if self.rect.centerx < obj.rect.centerx:
                        self.rect.x = obj_mask_rect.left - mask_rect.right + self.rect.x
                        collisions["right"] = True
                    else:
                        self.rect.x = obj_mask_rect.right - mask_rect.left + self.rect.x
                        collisions["left"] = True
                else:
                    if self.rect.centery < obj.rect.centery:
                        self.rect.y = obj_mask_rect.top - mask_rect.bottom + self.rect.y
                        collisions["bottom"] = True
                    else:
                        self.rect.y = obj_mask_rect.bottom - mask_rect.top + self.rect.y
                        collisions["top"] = True

        return collisions