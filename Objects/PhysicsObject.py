import pygame

from .KinematicObject import KinematicObject

class PhysicsObject(KinematicObject):


    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        """Any object that moves with velocities and friction instead of direct position changes. move_and_slide() must be called for movement to function.
            Inherits from KinematicObject, meaning positions, size, and sprites can still be adjusted directly."""
        super().__init__(width, height, *groups)

        self.vel_x = 0
        self.vel_y = 0

        self.friction = 0.9


    def move_and_slide(self) -> None:
        """Updates and applies all physics-based transformations of a PhysicsObject. Required call for physics simulation."""
        
        self.rect.x += round(self.vel_x)
        self.rect.y += round(self.vel_y)

        if abs(self.vel_x) > 0.1:
            self.vel_x -= self.vel_x * self.friction
        else:
            self.vel_x = 0
        if abs(self.vel_y) > 0.1:
            self.vel_y -= self.vel_y * self.friction
        else:
            self.vel_y = 0


    def set_friction(self, friction:float) -> None:
        """Changes the friction of this PhysicsObject. 
            Friction is used as a multiplier of velocity, so values between 0 and 1 should be used for proper simulation, 
            0 being the least drag and 1 being the most.
        """
        self.friction = friction


    def apply_force(self, x:int, y:int) -> None:
        """Adds the given values to the velocity of the object."""
        self.vel_x += x
        self.vel_y += y


    def set_velocity(self, x:int, y:int) -> None:
        """Sets the velocity to the given values."""
        self.vel_x = x
        self.vel_y = y