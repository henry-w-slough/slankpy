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
        self.mask_rect = Collision.get_mask_rect(self.rect, self.mask)

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
        self.mask_rect.x = x
        self.mask_rect.y = y


    def add_position(self, x:float, y:float) -> None:
        """Adds the given values to the position."""
        self.rect.x += round(x)
        self.rect.y += round(y)


    def set_size(self, width: int, height: int) -> None:
        """Sets the size of the GameObject, including rect and sprite sizes."""
        self.viewport_width *= (width / self.rect.width)
        self.viewport_height *= (height / self.rect.height)

        self.sprite.set_size(width, height)
        self.image = self.sprite.texture

        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = Collision.get_mask_rect(self.rect, self.mask)

    

    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Changes the sprite to the given Sprite animation and the specific frame index.
            Sprites must be added through the Sprite of this object in order to be used."""
        self.sprite.set_sprite(animation_name, sprite_index)
        self.image = self.sprite.texture
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_rect = Collision.get_mask_rect(self.rect, self.mask)
    
