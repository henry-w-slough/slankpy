import pygame

from ..GameObject import GameObject

class Camera:


    def __init__(self) -> None:
        
        #target is by default not defined, but can be set through setter function
        self.target:GameObject.GameObject

        self.fov_x = 300
        self.fov_y = 300


    def set_target(self, target:GameObject.GameObject) -> None:
        """Sets the GameObject which this camera will follow."""
        self.target = target

    
    def set_fov(self, x:int, y:int) -> None:
        """Changes the distance at which GameObjects are drawn."""
        self.fov_x = x
        self.fov_y = y


    def get_visible_layer(self, layer:pygame.sprite.Group) -> pygame.sprite.Group:
        """Returns a group of all sprites that are visible on the Screen. Compares the position of this object's target and the FOV to check for visibility."""

        visible = pygame.sprite.Group()
        
        #iterating through the given layer
        for s in layer:
            #comparing the position to the fov of the Camera
            if s.rect.center[0] > self.target.rect.center[0]-self.fov_x and s.rect.center[0] < self.target.rect.center[0]+self.fov_x:
                if s.rect.center[1] > self.target.rect.center[1] - self.fov_y and s.rect.center[1] < self.target.rect.center[1] + self.fov_y:
                    visible.add(s)
            
        return visible