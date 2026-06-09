import pygame


class Sprite():


    def __init__(self, width:float, height:float) -> None:
        """Handles all animation and sprite-related operations to a GameObject.
        
        Holds a Sprite image, which is the image drawn on the GameObject image on the screen."""

        self.image = pygame.Surface((width, height))
        self._image_unmodified = pygame.Surface((width, height))
    

    @property
    def image_unmodified(self) -> pygame.Surface:
        """The image of the sprite without transformations such as rotation."""
        return self._image_unmodified


    def fill_color(self, color:tuple[int, int, int]) -> None:
        """Fills the image with the given color."""
        self.image.fill(color)
        self._image_unmodified.fill(color)
    