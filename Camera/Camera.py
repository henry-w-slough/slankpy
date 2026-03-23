import pygame

from ..Objects import KinematicObject


class Camera:


    def __init__(self) -> None:
        """Handles all world to viewport calculations and translations."""
        
        #note: because the position will always be (0, 0), unchanging from player movement,
        #this doesn't need to be moved as long as scale isn't changed
        self.viewport_rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())

        self.target:KinematicObject.KinematicObject


    def update(self) -> None:
        self.viewport_rect.center = self.target.rect.center


    def get_visible(self, layer:pygame.sprite.Group) -> pygame.sprite.Group:
        """Used for object view culling. Goes through the given Group and removes sprites that aren't visible on the screen."""
        visible = pygame.sprite.Group()

        for s in layer:
            if s.rect.colliderect(self.viewport_rect):
                visible.add(s)

        return visible
            
