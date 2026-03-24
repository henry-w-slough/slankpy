import pygame
import random

from ..Objects import KinematicObject


class Camera:


    def __init__(self, target:KinematicObject.KinematicObject) -> None:
        """Handles all world to viewport calculations and translations. Holds a target, which is the object in focus on the screen. Utilizes viewport positions of Objects to draw them on the screen, instead of direct world-position change."""

        #used top adjust the viewport position. Because the target's VP is adjusted to the middle of the screen,
        #each transformation has to be adjusted to compensate
        self.focus_x = (pygame.display.get_surface().get_width()//2) - (target.rect.width//2)
        self.focus_y = (pygame.display.get_surface().get_height()//2) - (target.rect.height//2)

        self.target = target
        self.focus_target()


    def focus_target(self) -> None:
        """Change the screen position of the target to the middle of the screen."""
        self.target.viewport_x = self.focus_x
        self.target.viewport_y = self.focus_y


    def unfocus_target(self) -> None:
        """Reset the target's screen-relative position to it's actual world position."""
        self.target.viewport_x = self.target.rect.x
        self.target.viewport_y = self.target.rect.y
        

    def set_target(self, target:KinematicObject.KinematicObject) -> None:
        """Set the target that this camera focuses on."""
        self.target = target
    

    def apply_camera_offset(self, *layers:pygame.sprite.Group) -> None:
        """Applies the transformations neccessary to the given group to follow the target. Note: This function is NECCESSARY in order to follow a target using a Camera object."""
        for layer in layers:
            for s in layer:
                s.viewport_x = s.rect.x - self.target.rect.x + self.focus_x
                s.viewport_y = s.rect.y - self.target.rect.y + self.focus_y
            
