import pygame
import random

from ..Objects import KinematicObject


class Camera:


    def __init__(self, target:KinematicObject.KinematicObject) -> None:
        """Handles all world to viewport calculations and translations."""
        
        self.viewport_image = pygame.Surface((pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
        self.viewport_rect = self.viewport_image.get_rect()

        self.viewport_image.fill((255, 255, 255, 100))

        self.target = target
        self.focus_target()


    def focus_target(self) -> None:
        self.target.viewport_x = pygame.display.get_surface().get_width()//2
        self.target.viewport_y = pygame.display.get_surface().get_height()//2


    def unfocus_target(self) -> None:
        self.target.viewport_x = self.target.rect.x
        self.target.viewport_y = self.target.rect.y
        

    def set_target(self, target:KinematicObject.KinematicObject) -> None:
        self.unfocus_target()
        self.target = target
        self.focus_target()
    

    def apply_camera_offset(self, *layers:pygame.sprite.Group) -> None:
        for layer in layers:
            for s in layer:
                if s != self.target:
                    s.viewport_x = s.rect.x - self.target.rect.x
                    s.viewport_y = s.rect.y - self.target.rect.y
            
