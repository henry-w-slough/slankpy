import pygame

class Screen():
    

    def __init__(self, width:int, height:int) -> None:

        self.screen = pygame.display.set_mode((width, height))
        
        self.width = width
        self.height = height

        self.clock = pygame.time.Clock()

        self.layers = {

        }

        self.fill_color = (0, 0, 0)


    def is_quit(self) -> bool:
        """Returns a bool of whether or not the user has quit the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False


    def update(self) -> None:
        """Refreshes the screen, updates and draws all layers added."""
        self.screen.fill(self.fill_color)

        for layer in self.layers.values():
            layer.update()
            layer.draw(self.screen)
            
        pygame.display.update()
        self.clock.tick(60)
    

    def add_layer(self, name:str) -> None:
        """Adds the given layer to the Screen layers with a new sprite group."""
        if name in self.layers:
            print("WARNING: Screen: add_layer: Given layer_key already exists within Screen layers, overwriting existing.")
        #layers is used only for sprite groups, so one can be automatically placed
        self.layers[name] = pygame.sprite.Group()
    

    def remove_layer(self, name:str) -> None:
        """Removes the given layer from the Screen's layer dict."""
        if name in self.layers:
            del self.layers[name]
            return
        print("ERROR: Screen: remove_layer: Invalid layer_key given for removal.")
        return
    

    def set_fill_color(self, color:tuple[int, int, int]) -> None:
        """Sets the color that clears the screen before layers are drawn on."""
        self.fill_color = color