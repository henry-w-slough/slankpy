import pygame


class Transform:


    def __init__(self) -> None:
        """Holds the position, rotation, and scale for a GameObject."""

        self.x: float = 0.0
        self.y: float = 0.0 

        self.width: float = 0
        self.height: float = 0

        self.rotation: float = 0


    def get_rotated_surface(self, image:pygame.Surface, rect:pygame.Rect) -> tuple[pygame.Surface, pygame.Rect]:
        """Gets the given Surface rotated to the Transform's rotation. Also returns the updated Rect which is created
        based on the updated Surface.

        Example:
            _transform.rotation += 5 (setting the rotation)
            self.image, self.rect = _transform.get_rotated_surface(self.image) (updating for rotation)
        """
        #proper rotation, changing Surface and updating new Rect
        rotated_image = pygame.transform.rotate(image, self.rotation)
        rotated_rect = rotated_image.get_rect(center=(self.x, self.y))


        return rotated_image, rotated_rect