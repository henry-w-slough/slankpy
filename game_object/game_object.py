import pygame

from .transform import Transform
from .sprite import Sprite


class GameObject(pygame.sprite.Sprite):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        """The base class for all objects in a game that need to be controlled and rendered on a Screen.
        
        Position:
            Positions are float-based values for accurate calculations, but they are
            rounded during rendering. This means that though the values are accurate, 
            the on-screen result of the GameObject position may not be truly where it is.
        """
        super().__init__(*groups)


        self._transform = Transform(width, height)
        self._sprite = Sprite(width, height)

        #type hints are needed here for proper refs in methods
        self.image: pygame.Surface = self._sprite.image
        self.rect: pygame.Rect = self.image.get_rect()


    def fill_color(self, color: tuple[int, int, int]) -> None:
        """Fills the image of the GameObject with the given color (R, G, B).
        
        Useful for debugging or basic game-making where sprites aren't necessary.
        """
        self._sprite.fill_color(color)
        self.image = self._sprite.image 


    def add_animation(self, name: str, src: str, sprite_rows: int, sprite_columns: int) -> None:
        """Adds a new animation dict of sprites derived from the given spritesheet image.
        
        Sprite sizes are calculated based on the number of sprite rows and columns provided."""
        self._sprite.add_animation(name, src, sprite_rows, sprite_columns)


    def set_sprite(self, animation_name: str, sprite_index: int) -> None:
        """Sets the sprite to the given animation frame.
        
        Animations can be added with add_animation() of GameObject."""
        self._sprite.set_sprite(animation_name, sprite_index)
        self.image = self._sprite.image


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
        self.image = pygame.transform.scale(self.image, (width, self.height))
    
    
    @property
    def height(self) -> float:
        return self._transform.height
    

    @height.setter
    def height(self, height: float) -> None:
        self._transform.height = height 
        self.image = pygame.transform.scale(self.image, (self.width, height))


    @property
    def rotation(self) -> float:
        return self._transform.rotation
    

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        self._transform.rotation = rotation
        self._sprite.image, self.rect = self._transform.get_rotated_surface(self._sprite.image_unmodified)
        self.image = self._sprite.image




