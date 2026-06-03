import pygame


class Screen:


    def __init__(self, width: int, height: int, fps: float, *args, **kwargs) -> None:
        
        #creating the window instance
        self._screen: pygame.Surface = pygame.display.set_mode((width, height), *args, **kwargs)

        self._width = width
        self._height = height

        #time-relations
        self._clock = pygame.time.Clock()
        self._delta_time: float = 0
        self.fps = fps

        #screen layering
        self.background_color: tuple[int, int, int] = (0, 0, 0)


    @property 
    def screen(self) -> pygame.Surface:
        """The display surface that is drawn onto in each update frame."""
        return self._screen


    @property
    def delta_time(self) -> float:
        """The time elapsed since the last frame. 
        
        Used for consistent, frame-rate independent calculations."""
        return self._delta_time


    @property
    def height(self) -> int:
        return self._height


    @property
    def width(self) -> int:
        return self._width


    @property
    def center(self) -> tuple[float, float]:
        """The position of the center of the screen."""
        return (self._screen.get_width() / 2, self._screen.get_height() / 2)


    def update(self) -> None:
        """Updates the display by flipping the buffer and redrawing all layers to the screen.
        
        This is also where delta_time is updated.
        """

        self._screen.fill(self.background_color)

        pygame.display.flip()
        self._delta_time = self._clock.tick_busy_loop(self.fps) / 1000


    def has_quit(self) -> bool:
        """Whether the window has been closed or ended."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    


        




