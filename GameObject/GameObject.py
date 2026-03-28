import pygame
from ..GameObject import Sprite


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
        
        self.viewport_x = self.rect.x
        self.viewport_y = self.rect.y


    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Changes the sprite to the given Sprite animation and the specific frame index.
            Sprites must be added through the Sprite of this object in order to be used."""
        self.sprite.set_sprite(animation_name, sprite_index)
        self.image = self.sprite.texture


    def collision_check(self, *layers) -> dict:

        collisions = {"top": False, "bottom": False, "left": False, "right": False}
        
        for layer in layers:

            if not pygame.sprite.spritecollide(self, layer, False):  # type: ignore
                continue

            for obj in pygame.sprite.spritecollide(self, layer, False, pygame.sprite.collide_mask):  # type: ignore
                if obj == self:
                    continue

                # Get mask bounds in world space
                self_bounds: list[pygame.Rect] = self.mask.get_bounding_rects() #type: ignore
                obj_bounds: list[pygame.Rect] = obj.mask.get_bounding_rects()

                #if the bounds are empty, skip
                if not self_bounds or not obj_bounds:
                    continue


                #the first rect for the mask rect building
                mask_rect = pygame.Rect(self_bounds[0])
                obj_mask_rect = pygame.Rect(obj_bounds[0])

                #building the mask rect for self mask
                for r in self_bounds[1:]: 
                    mask_rect.union_ip(r)
                #building mask rect for object
                for r in obj_bounds[1:]: 
                    obj_mask_rect.union_ip(r)

                # Offset to world space
                mask_rect.move_ip(self.rect.topleft)
                obj_mask_rect.move_ip(obj.rect.topleft)

                overlap_x = min(mask_rect.right, obj_mask_rect.right) - max(mask_rect.left, mask_rect.left)
                overlap_y = min(mask_rect.bottom, obj_mask_rect.bottom) - max(mask_rect.top, obj_mask_rect.top)

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
    
