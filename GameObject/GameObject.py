import pygame
from . import Sprite

class GameObject(pygame.sprite.Sprite):


    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        """Represents any object thats in a game. Holds a Rect and Sprite for use."""
        super().__init__(*groups)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()

        self.sprite = Sprite.Sprite(width, height)


    def set_position(self, x:int, y:int) -> None:
        """Sets this object's position to the given values"""
        self.rect.topleft = (x, y)


    def add_position(self, x:float, y:float) -> None:
        """Adds the given values to this object's position"""
        self.rect.x += round(x)
        self.rect.y += round(y)


    def add_size(self, width:int, height:int) -> None:
        """Adds the given values to the size of the object."""
        self.rect.width += width
        self.rect.height += height


    def set_size(self, width:int, height:int) -> None:
        """Sets the width and height of the GameObject."""
        #setting rectangle size for the object
        self.rect.width = width
        self.rect.height = height
        #sets the sprite size, which updates it's texture, and updates the object image
        self.sprite.set_size(width, height)
        self.image = self.sprite.texture


    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Changes the sprite to the correlating animation frame."""
        #getting sprite
        sprite = self.sprite.get_sprite(animation_name, sprite_index)
        #updating this image
        self.image = sprite
        #this isn't done inside Sprite because it may be optional for some use cases
        self.sprite.texture = sprite