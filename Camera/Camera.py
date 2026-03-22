import pygame

from ..Objects import KinematicObject


class Camera:


    def __init__(self) -> None:
        """Handles all world to viewport calculations and translations."""
        
        self.viewport_rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())


    def get_visible(self, layer:pygame.sprite.Group) -> None:
        """Used for object view culling. Goes through the given Group and removes sprites that aren't """
        for s in layer:
            if not s.rect.collide_rect(self.viewport_rect):
                layer.remove(s)
            
