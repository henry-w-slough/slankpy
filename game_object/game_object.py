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

        #type hints are needed here for proper refs in methods
        self.image: pygame.Surface = pygame.Surface((width, height))
        self.rect: pygame.Rect = self.image.get_rect()

        self._transform = Transform()

        self.sprite = Sprite(width, height)


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
        self.image, self.rect = self._transform.get_rotated_surface(self.sprite.sprite, self.rect)




