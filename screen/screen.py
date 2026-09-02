import pygame
from ..screen import debug
from ..game_object import GameObject


class Screen:

    pygame.init()

    def __init__(self, width: int, height: int, vsync : bool = True, target_fps: float = 60, *args, **kwargs) -> None:
        """Where all objects and layers are updated and drawn. Has full customization of the window along with directly screen-related settings.

        Note:
            The update function of the Screen must be called in order to have layers updated and drawn properly.
        """

        self._screen: pygame.Surface = pygame.display.set_mode((width, height), vsync=vsync, *args, **kwargs)

        #time-relations
        self._clock = pygame.time.Clock()
        self._delta_time: float = 0.0
        self._elapsed_ticks = 0

        if vsync == True:
            #getting the native fps to match vsync
            self.target_fps = pygame.display.get_desktop_refresh_rates()[0] if hasattr(pygame.display, 'get_desktop_refresh_rates') else 60
        else:
            self.target_fps = target_fps

        #screen layering
        self.background_color: tuple[int, int, int] = (0, 0, 0)
        self._layers: dict[str, pygame.sprite.Group[GameObject]] = {}

        #screen customs
        self._caption = "Slankpy Game"
        pygame.display.set_caption(self._caption)

        debug.init()


    @property 
    def screen(self) -> pygame.Surface:
        """The display surface that is drawn onto in each update frame."""
        return self._screen

    
    @property
    def caption(self) -> str:
        return self._caption
    

    @caption.setter
    def caption(self, caption: str) -> None:
        self._caption = caption
        pygame.display.set_caption(caption)


    @property
    def fps(self) -> float:
        """The current frames per second of the game. 
        
        This does not neccessarily match the target fps 
        of the Screen."""
        return self._clock.get_fps()


    @property
    def elapsed_ticks(self) -> int:
        """The total independent elapsed time of the game in ticks.
        
        One tick is added every frame of Screen.update()."""
        return self._elapsed_ticks  


    @property
    def delta_time(self) -> float:
        """The time elapsed since the last frame. 
        
        Used for consistent, frame-rate independent calculations."""
        return self._delta_time


    @property
    def height(self) -> int:
        return self._screen.get_height()
    

    @property
    def width(self) -> int:
        return self._screen.get_width()


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
        """Whether the window has been exited."""
        #using peek() instead as to not clear the event queue so we can
        #use it later down the line or in other places
        if pygame.event.peek(pygame.QUIT):
            return True
        return False


    def update(self) -> None:
        """Updates the screen by flipping the buffer and updating + drawing every layer in order.
        
        This is also where delta_time is updated.

        Should be called every frame of a loop in order for a game to be functional.
        """
        self._screen.fill(self.background_color)

        debug.draw_bottom(self._screen)

        for layer in self.layers.values():  
            layer.update()
            layer.draw(self._screen)

        debug.draw_top(self._screen)
        
        pygame.display.flip()

        #updating time
        self._elapsed_ticks += 1
        self._delta_time = self._clock.tick_busy_loop(self.target_fps) / 1000.0
    
    


        




