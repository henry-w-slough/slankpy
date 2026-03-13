import pygame

from .import GameObject

class PhysicsObject(GameObject.GameObject):


    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        """GameObject inherited object that moves with velocities and friction instead of direct position changes. move_and_slide() must be called for movement to function."""
        super().__init__(width, height, *groups)

        self.vel_x = 0
        self.vel_y = 0

        self.friction = 0.9


    def move_and_slide(self) -> None:
        """Updates all physics-based calculations, required for object physics simulation."""

        #updating position based on velocity
        self.add_position(self.vel_x, self.vel_y)

        if abs(self.vel_x) < self.friction:
            #velocity will never equal 0, so it has to be given a nudge
            self.vel_x = 0
        else:
            #updating velocity based on friction and time
            self.vel_x *= self.friction

        #applying same math to y as x velocity
        if abs(self.vel_y) < self.friction:
            self.vel_y = 0
        else:
            self.vel_y *= self.friction


    def apply_force(self, x:int, y:int) -> None:
        """Adds the given values to the velocity of the object."""
        self.vel_x += x
        self.vel_y += y


    def set_velocity(self, x:int, y:int) -> None:
        """Sets the velocity to the given values."""
        self.vel_x = x
        self.vel_y = y

    
    def add_force(self, x:int, y:int) -> None:
        """Adds the given forces to the corresponding velocities of the object."""
        self.vel_x += x
        self.vel_y += y