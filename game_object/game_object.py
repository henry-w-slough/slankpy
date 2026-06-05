import pygame

from .transform import Transform


class GameObject(pygame.sprite.Sprite):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        """The base class for all objects in a game that need to be controlled and rendered on a Screen.
        
        Position:
            Positions are float-based values for accurate calculations, but they are
            rounded during rendering. This means that though the values are accurate, 
            the on-screen result of the GameObject position may not be truly where it is.
        """
        super().__init__(*groups)

        #type hints are needed here for proper type-hinting in functions
        self.image: pygame.Surface = pygame.Surface((width, height))
        self.rect: pygame.Rect = self.image.get_rect()

        self.transform = Transform()


    def fill_color(self, color: tuple[int, int, int]) -> None:
        """Sets the color that is filled onto the image of this GameObject. Colors used are in RGB.
        
        Useful for debugging or testing where a sprite addition is not necessary.
        """
        self.image.fill(color)
    

    def set_position(self, x: float, y: float) -> None:
        """Changes the position of the GameObject.

        Note:
            Changes to GameObject.x and GameObject.y will be rounded during rendering,
            any changes made to float position are purely calculation-based for accuracy.
        """
        #setting class float position
        self.transform.x = x
        self.transform.y = y
        #setting rect pygame position
        self.rect.x = round(x)
        self.rect.y = round(y)
