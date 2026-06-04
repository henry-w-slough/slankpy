import pygame


class Screen:


    def __init__(self, width: int, height: int, fps: float, *args, **kwargs) -> None:
        """Where all objects and layers are updated and drawn. Has full customization of the window along with directly screen-related settings.

        Note:
            The update function of the Screen must be called in order to have layers updated and drawn properly.
        """

        #creating the window instance
        self._screen: pygame.Surface = pygame.display.set_mode((width, height), *args, **kwargs)

        #time-relations
        self._clock = pygame.time.Clock()
        self._delta_time: float = 0.0
        self.fps: float = fps

        #screen layering
        self.background_color: tuple[int, int, int] = (0, 0, 0)
        self._layers: dict[str, pygame.sprite.Group] = {}


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
        return self._screen.get_width()
    

    @property
    def width(self) -> int:
        return self._screen.get_height()


    @property
    def center(self) -> tuple[float, float]:
        """The position of the center of the screen."""
        return (self._screen.get_width() / 2, self._screen.get_height() / 2)
    

    @property
    def layers(self) -> dict[str, pygame.sprite.Group]:
        return self._layers
    

    def add_layer(self, name: str) -> None:
        """Adds a layer to be updated and drawn every frame.

        Note:
            Layers are drawn in the order they fall in the dictionary. To take advantage of this,
            add layers in the order of their perspective relative to the camera.
        """
        self.layers[name] = pygame.sprite.Group()


    def remove_layer(self, name: str) -> None:
        """Adds a layer to be updated and drawn every frame.

        Note:
            Layers are drawn in the order they fall in the dictionary. To take advantage of this,
            add layers in the order of their perspective relative to the camera.
        """
        self.layers.pop(name)
    

    def has_quit(self) -> bool:
        """Whether the window has been exited.
        
        Note: 
            Clears pygame.event.get() queue! If you need to access events
            elsewhere, use pygame.event.peek() to avoid issues.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False


    def update(self) -> None:
        """Updates the screen by flipping the buffer. Updates and draws every layer in order.
        
        This is also where delta_time is updated.
        """

        self._screen.fill(self.background_color)

        for layer in self._layers.values():
            layer.update()
            layer.draw(self._screen)

        pygame.display.flip()
        #using 1000.0 to specify for float type
        self._delta_time = self._clock.tick_busy_loop(self.fps) / 1000.0
    
    


        




