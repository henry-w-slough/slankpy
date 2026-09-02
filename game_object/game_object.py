import pygame

from .sprite import Sprite


class GameObject(pygame.sprite.Sprite):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        """The base class for all objects within a game that need to be controlled or displayed.
        
        **Notes:**

        * All positional, rotational, and scale-based values are stored as floats for precise calculation, but are
        rounded using round() for any rendering done to the Screen.

        ***Position***:
            * The position of the GameObject within the world. Represented as x and y, and are relative to the GameObject's center.
            Should be accessed through the GameObject's separate x and y properties.

        ***Rotation***:
            * A single float representing the degree angle at which the GameObject is rotated.
            Note that in order to keep a consistent image size, the rect size of the GameObject pulsates
            at the speed of rotation.

        **Scale**:
            * The size of the GameObject in width and height properties.
            When scale is changed, it is changed relative to the x and y position, not from the center.
        """
        super().__init__(*groups)

        self._sprite = Sprite(width, height)

        self.image: pygame.Surface = self._sprite.image
        self.rect: pygame.Rect = self.image.get_rect()

        self._position = pygame.math.Vector2()


    @property
    def position(self) -> pygame.math.Vector2:
        return self._position


    @position.setter
    def position(self, position: pygame.math.Vector2) -> None:
        self._position = position
        self.rect.x = round(position.x)
        self.rect.y = round(position.y)


    def add_animation(self, src: str, name: str, rows: int, columns: int) -> None:
        """Adds a new animation to the GameObject, which can be accessed by using GameObject.set_sprite()
        with the new animation's name.
        """
        self._sprite.add_animation(name, src, rows, columns)


    def set_animation(self, name: str, frame: int) -> None:
        """Sets the image of the GameObject to the given animation at the given frame."""
        self._sprite.set_animation(name, frame)
        self.image = self._sprite.image


    @property
    def animations(self) -> dict[str, dict[int, pygame.Surface]]:
        return self._sprite.animations