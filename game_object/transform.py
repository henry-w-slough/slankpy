import pygame


class Transform:


    def __init__(self, width:float, height:float) -> None:
        """Holds the position, rotation, and scale for a GameObject."""

        self._x: float = 0.0
        self._y: float = 0.0 

        self.draw_x: int = 0
        self.draw_y: int = 0

        self._width: float = width
        self._height: float = height

        self.rotation: float = 0.0

        self.draw_width: int = round(width)
        self.draw_height: int = round(height)


    @property
    def x(self) -> float:
        return self._x
    

    @x.setter
    def x(self, x:float) -> None:
        self._x = x
        self.draw_x = round(x)
    

    @property
    def y(self) -> float:
        return self._y
    

    @y.setter
    def y(self, y:float) -> None:
        self._y = y
        self.draw_y = round(y)


    @property
    def width(self) -> float:
        return self._width
    

    @width.setter
    def width(self, width:float) -> None:
        self._width = width
        self.draw_width = round(width)
    

    @property
    def height(self) -> float:
        return self._height
    

    @height.setter
    def height(self, height:float) -> None:
        self._width = height
        self.draw_height = round(height)


    def get_rotated_surface(self, image:pygame.Surface, rect:pygame.Rect) -> tuple[pygame.Surface, pygame.Rect]:
        """Gets the given Surface rotated to the Transform's rotation. Also returns the updated Rect which is created
        based on the updated Surface.
        """
        #proper rotation, changing Surface and updating new Rect
        rotated_image = pygame.transform.rotate(image, self.rotation)

        ratio_width = rotated_image.width / image.width
        ratio_height = rotated_image.height / image.height

        rotated_image = pygame.transform.scale(rotated_image, (self.width*ratio_width, self.height*ratio_height))
        
        rotated_rect = rotated_image.get_rect(center=rect.center)

        return rotated_image, rotated_rect