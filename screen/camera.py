from ..game_object import GameObject
import pygame


class Camera:


    def __init__(self, target: GameObject) -> None:

        self._target: GameObject
        self.target = target

        self.zoom: int = 1


    @property
    def target(self) -> GameObject:
        """The focus of the Camera, which all perspective-based transformations are done relative to."""
        return self._target


    @target.setter
    def target(self, target: GameObject) -> None:

        self._target = target

        screen_surface = pygame.display.get_surface()
        if screen_surface is not None:
            self._target.view_x = int(screen_surface.get_width() // 2 - (self._target.width // 2))
            self._target.view_y = int(screen_surface.get_height() // 2 - (self._target.height // 2))


    def apply_transformation(self, object: GameObject) -> None:

        object.view_width = object.rect.width * self.zoom
        object.view_height = object.rect.width * self.zoom

        if object is self._target:
            return

        object.view_x = -(self._target.rect.x - object.rect.x) * self.zoom
        object.view_y = -(self._target.rect.y - object.rect.y) * self.zoom