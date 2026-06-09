import pygame


class Transform:


    def __init__(self, width:float, height:float) -> None:
        """Holds the position, rotation, and scale for a GameObject."""

        self.x: float = 0.0
        self.y: float = 0.0 

        self.width: float = width
        self.height: float = height

        self.rotation: float = 0.0


    def get_rotated_surface(self, image:pygame.Surface) -> tuple[pygame.Surface, pygame.Rect]:
        """Gets the given Surface rotated to the Transform's rotation. Also returns the updated Rect which is created
        based on the updated Surface.

        Example:
            _transform.rotation += 5 (setting the rotation)
            self.image, self.rect = _transform.get_rotated_surface(self.image) (updating for rotation)
        """
        #proper rotation, changing Surface and updating new Rect
        rotated_image = pygame.transform.rotate(image, self.rotation)
        rotated_image = pygame.transform.scale(rotated_image, (self.width, self.height))

        rotated_rect = rotated_image.get_rect(center=(self.x+(self.width/2), self.y+(self.height/2)))
        rotated_rect.width = self.width
        rotated_rect.height = self.height

        return rotated_image, rotated_rect