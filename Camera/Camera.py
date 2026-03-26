import pygame
import random

from ..GameObject import GameObject


class Camera:


    def __init__(self, target:GameObject.GameObject) -> None:
        """Handles all viewport positional calculations and translations. Holds a target, which is the object in focus on the screen. Utilizes viewport positions of Objects to draw them on the screen, instead of direct world-position change."""

        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        #used top adjust the viewport position. Because the target's VP is adjusted to the middle of the screen,
        #each transformation has to be adjusted to compensate
        self.focus_x = (self.screen_width//2) - (target.rect.width//2)
        self.focus_y = (self.screen_height//2) - (target.rect.height//2)

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
        

    def set_target(self, target:GameObject.GameObject) -> None:
        """Set the target that this camera focuses on."""
        self.target = target
    

    def apply_offset(self, *layers:pygame.sprite.Group) -> None:
        """Applies the transformations neccessary to the given group to follow the target. Note: This function is NECCESSARY in order to follow a target using a Camera object."""
        for layer in layers:
            for s in layer:
                #sets the viewport position of the sprite to the axis distance of the sprite and
                #the target added to the compensation for the target being in the middle of the screen
                s.viewport_x = s.rect.x - self.target.rect.x + self.focus_x
                s.viewport_y = s.rect.y - self.target.rect.y + self.focus_y


    def cull_layers(self, *layers:pygame.sprite.Group) -> pygame.sprite.Group:
        
        visible = pygame.sprite.Group()

        for layer in layers:
            #every sprite in every unpackaged layer given
            for s in layer:
                #checking x axis
                if s.viewport_x + s.rect.width < 0 or s.viewport_x > self.screen_width:
                    continue
                #checking y axis
                if s.viewport_y + s.rect.height < 0 or s.viewport_y > self.screen_height:
                    continue
                visible.add(s)

        return visible
                


            
