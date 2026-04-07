import pygame
import random

class Screen():
    

    def __init__(self, width:int, height:int, fps:int=60) -> None:
        """Class that manages all window and update actions. Can add and remove layers for screen drawing and update the window with it's update() function."""

        self.screen = pygame.display.set_mode((width, height), vsync=True)
        
        self.width = width
        self.height = height

        self.clock = pygame.time.Clock()
        self.fps = fps

        #represents all the layers in the game
        self.layers = {

        }

        #works for Camera culling, used to only draw certain sprites but update all
        self.visible_layer = pygame.sprite.Group()
        self.should_cull = True

        self.fill_color = (0, 0, 0)


    def set_culling(self, cull:bool) -> None:
        ""Sets the method of drawing. In practice, culling should be used when a Camera object is used to filter visible and non-visible objects. Otherwise, culling should not be performed.""
        self.should_cull = cull


    def has_quit(self) -> bool:
        """Returns a bool of whether or not the user has quit the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False


    def update(self) -> None:
        """Refreshes the screen, updates and draws all layers added."""
        
        self.screen.fill(self.fill_color)

        #drawing layer, blitting it so any Camera in use can be properly used for offsetting each sprite
        if self.should_cull:
            self.visible_layer.update()
            for s in self.visible_layer:
                self.screen.blit(pygame.transform.scale(s.image, (s.viewport_width, s.viewport_height)), (s.viewport_x, s.viewport_y)) 
        else:
            for layer in self.layers:
                layer.update()
                layer.draw(self.screen)
            
        pygame.display.update()
        self.clock.tick_busy_loop(self.fps)


    def set_caption(self, caption:str) -> None:
        """Sets the caption of the screen window."""
        pygame.display.set_caption(caption)
    

    def add_layer(self, name:str) -> None:
        """Adds the given layer to the Screen layers."""
        if name in self.layers:
            print(f"WARNING: Screen: add_layer: Name {name} already exists within Screen layers, overwriting existing.")
        #layers is used only for sprite groups, so one can be automatically placed
        self.layers[name] = pygame.sprite.Group()
    

    def remove_layer(self, name:str) -> None:
        """Removes the given layer from the Screen."""
        #only checks self.layers because if it's in self.layers it'll be in self.visible_layers
        if name in self.layers:
            del self.layers[name]
            return
        print(f"ERROR: Screen: remove_layer: Layer of name {name} given for removal.")
        return
    

    def set_fill_color(self, color:tuple[int, int, int]) -> None:
        """Sets the color that clears the screen before layers are drawn."""
        self.fill_color = color