import pygame
import random

from ..Objects import KinematicObject


class Camera:


    def __init__(self) -> None:
        """Handles all world to viewport calculations and translations."""
        

        self.viewport_rect = pygame.Rect(0, 0, pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())

        self.target:KinematicObject.KinematicObject


    def update(self) -> None:
        self.viewport_rect.center = self.target.rect.center


    def apply_offset(self, *layers:pygame.sprite.Group) -> None:
        for layer in layers:
            for s in layer:
                s.viewport_x = s.rect.x - self.target.rect.x
                s.viewport_y = s.rect.y - self.target.rect.y


    def get_visible(self, *layers:pygame.sprite.Group) -> pygame.sprite.Group:
        """Used for object view culling. Goes through the given Groups and removes sprites that aren't visible on the screen."""
        visible = pygame.sprite.Group()

        for layer in layers:
            for s in layer:
                if s.rect.colliderect(self.viewport_rect):
                    visible.add(s)

        return visible
            
