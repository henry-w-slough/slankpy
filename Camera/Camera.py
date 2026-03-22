import pygame

from ..Objects import KinematicObject


class Camera:


    def __init__(self) -> None:
        """Handles all world to viewport calculations and translations."""
        
        #note: because the position will always be (0, 0), unchanging from player movement,
        #this doesn't need to be moved as long as scale isn't changed
        self.viewport_rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())

        self.target:KinematicObject.KinematicObject
        
        self.last_x = 0
        self.last_y = 0

        self.offset_x = 0
        self.offset_y = 0

        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()


    def add_offset(self, layer:pygame.sprite.Group) -> None:
        """Adds the offset of the Camera to the given object's position."""



    def get_visible(self, layer:pygame.sprite.Group) -> pygame.sprite.Group:
        """Used for object view culling. Goes through the given Group and removes sprites that aren't visible on the screen."""
        for s in layer:
            if not s.rect.colliderect(self.viewport_rect):
                layer.remove(s)
        return layer
            
