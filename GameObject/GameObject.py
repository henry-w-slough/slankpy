import pygame
from ..GameObject import Sprite


class GameObject(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any object with a position, rectangle, and sprite."""
        super().__init__(*groups)

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.sprite = Sprite.Sprite(width, height)

        self.mask = pygame.mask.from_surface(self.image)

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
        self.mask = pygame.mask.from_surface(self.image)


    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Changes the sprite to the given Sprite animation and the specific frame index.
            Sprites must be added through the Sprite of this object in order to be used."""
        self.sprite.set_sprite(animation_name, sprite_index)
        self.image = self.sprite.texture
        self.mask = pygame.mask.from_surface(self.image)


    def collision_check(self, *layers):
        collisions = {"top": False, "bottom": False, "left": False, "right": False}

        for layer in layers:
            for obj in pygame.sprite.spritecollide(self, layer, False, pygame.sprite.collide_mask): # type: ignore (this error is bs)

                overlap_x = min(self.rect.right, obj.rect.right) - max(self.rect.left, obj.rect.left)
                overlap_y = min(self.rect.bottom, obj.rect.bottom) - max(self.rect.top, obj.rect.top)

                if overlap_x < overlap_y:
                    if self.rect.centerx < obj.rect.centerx:
                        self.rect.right = obj.rect.left
                        collisions["right"] = True
                    else:
                        self.rect.left = obj.rect.right
                        collisions["left"] = True
                else:
                    if self.rect.centery < obj.rect.centery:
                        self.rect.bottom = obj.rect.top
                        collisions["bottom"] = True
                    else:
                        self.rect.top = obj.rect.bottom
                        collisions["top"] = True

        return collisions
    
