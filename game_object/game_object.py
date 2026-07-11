import pygame

from .transform import Transform
from .sprite import Sprite


class GameObject(pygame.sprite.Sprite):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        """The base class for all objects within a game that need to be controlled or displayed.
        
        **Documentation:**

        * All positional, rotational, and scale-based values are stored as floats for precise calculation, but are
        rounded using round() for any rendering done to the Screen.

        ***Position***:
            * Value correlating to the GameObject's position on the Screen (x, y).
            Should be accessed through the GameObject's separate x and y properties.

        ***Rotation***:
            * A single float representing the degree angle at which the GameObject is rotated.
            Note that in order to keep a consistent image size, the size of the GameObject pulsates
            at the speed of rotation and does not rotate itself.
        """
        super().__init__(*groups)

        self._transform = Transform(width, height)
        self._sprite = Sprite(width, height)

        self.image: pygame.Surface = self._sprite.image
        self.rect: pygame.Rect = self.image.get_rect()


    def _update_image_rect(self) -> None:
        """Refreshes the image and rect to match eachother."""
        self.image = self._sprite.image
        self.rect = self.image.get_rect(center=self.rect.center)
        


    @property
    def x(self) -> float:
        return self._transform.x
    

    @x.setter
    def x(self, x: float) -> None:
        self._transform.x = x
        self.rect.x = round(x)
    

    @property
    def y(self) -> float:
        return self._transform.y
    

    @y.setter
    def y(self, y: float) -> None:
        self._transform.y = y
        self.rect.y = round(y)
    

    @property
    def width(self) -> float:
        return self._transform.width
    

    @width.setter
    def width(self, width: float) -> None:
        self._transform.width = width
        self._sprite.width = width
        self._update_image_rect()
    

    @property
    def height(self) -> float:
        return self._transform.height
    

    @height.setter
    def height(self, height: float) -> None:
        self._transform.height = height
        self._sprite.height = height
        self._update_image_rect()


    @property
    def rotation(self) -> float:
        return self._transform.rotation
    

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        self._transform.rotation = rotation
        self._sprite.rotation = rotation
        self._update_image_rect()


    def add_animation(self, animation_name: str, src: str, sprite_rows: int, sprite_columns: int) -> None:
        """Adds a new animation to the GameObject's sprite. Sprites are added with a spritesheet from the given source image. 
        
        Note:
            The width and height of the sprites are determined based on the given 
            number of sprite rows and columns, meaning uneven-sized sprites can 
            mean the image will not look as it's meant to."""
        self._sprite.add_animation(animation_name, src, sprite_rows, sprite_columns)


    def set_sprite(self, animation_name: str, sprite_index: int) -> None:
        """Sets the image of the GameObject to the given animation sprite."""
        self._sprite.set_sprite(animation_name, sprite_index)
        self.image = self._sprite.image


