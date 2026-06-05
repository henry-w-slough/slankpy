from collections.abc import Iterable
import pygame


class GameObject(pygame.sprite.Sprite):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        """The base class for all objects in a game that need to be controlled and rendered on a Screen.
        
        Position:
            Positions are 
        """
        super().__init__(*groups)

        #type hints are needed here for proper type-hinting in functions
        self.image: pygame.Surface = pygame.Surface((width, height))
        self.rect: pygame.Rect = self.image.get_rect()

        #The entire purpose of
        self._x: float = 0.0
        self._y: float = 0.0


    def fill_color(self, color: tuple[int, int, int]) -> None:
        """Sets the color that is filled onto the image of this GameObject. Colors used are in RGB.
        
        Useful for debugging or testing where a sprite addition is not necessary.
        """
        self.image.fill(color)


    @property
    def x(self) -> int:
        """The x coordinate of the GameObject relative to the world position."""
        return self.rect.x
    

    @property
    def y(self) -> int:
        "The y coordinate of the GameObject relative to the world position."
        return self.rect.y 
