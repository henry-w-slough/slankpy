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
        self.focus_x = (self.screen_width//2) - (target.viewport_width//2)
        self.focus_y = (self.screen_height//2) - (target.viewport_height//2)

        self.zoom = 1

        self.target = target
        self.focus_target()


    def focus_target(self) -> None:
        """Change the screen position of the target to the middle of the screen."""

        #updates the focus based on the zoom of the camera, needed for constant target focus when function run
        self.focus_x = (self.screen_width//2) - ((self.target.viewport_width*self.zoom)//2)
        self.focus_y = (self.screen_height//2) - ((self.target.viewport_height*self.zoom)//2)

        self.target.viewport_x = round(self.focus_x)
        self.target.viewport_y = round(self.focus_y)

    def unfocus_target(self) -> None:
        """Reset the target's screen-relative position to it's actual world position."""
        self.target.viewport_x = self.target.rect.x
        self.target.viewport_y = self.target.rect.y
        

    def set_target(self, target:GameObject.GameObject) -> None:
        """Set the target that this camera focuses on."""
        self.target = target
    

    def set_zoom(self, zoom: float) -> None:
        """Sets the zoom level. 1.0 is normal, >1.0 zooms in, <1.0 zooms out."""
        self.zoom = zoom
        #setting focus so the target stays center after zoom changes
        self.focus_target()


    def apply_offset(self, *layers: pygame.sprite.Group) -> None:

        for layer in layers:
            for s in layer:
                if s != self.target:
                    s.viewport_x = (s.rect.x - self.target.rect.x) * self.zoom + self.focus_x
                    s.viewport_y = (s.rect.y - self.target.rect.y) * self.zoom + self.focus_y

                s.viewport_width = round(s.rect.width * self.zoom)
                s.viewport_height = round(s.rect.height * self.zoom)


    def cull_layers(self, *layers:pygame.sprite.Group) -> pygame.sprite.Group:
        
        visible = pygame.sprite.Group()

        for layer in layers:
            #every sprite in every unpackaged layer given
            for s in layer:
                #checking x axis
                if s.viewport_x + s.viewport_width < 0 or s.viewport_x > self.screen_width:
                    continue
                #checking y axis
                if s.viewport_y + s.viewport_height < 0 or s.viewport_y > self.screen_height:
                    continue

                visible.add(s)

        return visible
                


            
