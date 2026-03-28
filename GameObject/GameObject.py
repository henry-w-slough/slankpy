import pygame
from ..GameObject import Sprite
from ..GameObject import Collision


class GameObject(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any object with a position, rectangle, and sprite."""
        super().__init__(*groups)

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.sprite = Sprite.Sprite(width, height)

        #rect position can work functionally as World position
        #viewport values are relative to the screen
        self.viewport_x = 0
        self.viewport_y = 0

        self.viewport_width = width
        self.viewport_height = height


    def set_position(self, x:int, y:int) -> None:
        """Sets the position to the given values."""
        self.rect.x = x
        self.rect.y = y


    def add_position(self, x:float, y:float) -> None:
        """Adds the given values to the position."""
        self.rect.x += round(x)
        self.rect.y += round(y)


    def set_size(self, width:int, height:int) -> None:
        """Sets the size to the given values."""
        self.sprite.set_size(width, height)

        self.image = self.sprite.texture
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.viewport_x = self.rect.x
        self.viewport_y = self.rect.y


    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Changes the sprite to the given Sprite animation and the specific frame index.
            Sprites must be added through the Sprite of this object in order to be used."""
        self.sprite.set_sprite(animation_name, sprite_index)
        self.image = self.sprite.texture
        self.mask = pygame.mask.from_surface(self.image)


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
    
