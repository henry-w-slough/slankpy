import pygame

class Screen():
    

    def __init__(self, width:int, height:int) -> None:
        """Class that manages all window and update actions. Can add and remove layers for screen drawing and update the window with it's update() function."""

        self.screen = pygame.display.set_mode((width, height))
        
        self.width = width
        self.height = height

        self.clock = pygame.time.Clock()


        #represents all the layers in the game
        self.layers = {

        }

        #fundamentally represents all layers drawn on the Screen. This is seperate from self.layers
        #because this dict can remove or add layers/sprites, and self.layers can hold and update them even
        #when they aren't visible
        self.visible_layers = {
            
        }

        self.fill_color = (0, 0, 0)


    def has_quit(self) -> bool:
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

        for layer in self.visible_layers.values():
            layer.draw(self.screen)
            
        pygame.display.update()
        self.clock.tick(60)


    def get_layer(self, name:str) -> pygame.sprite.Group:
        try:
            return self.layers[name]
        except Exception as e:
            print(f"ERROR: Screen: get_layer: {e}")
            return pygame.sprite.Group()
    

    def add_layer(self, name:str, is_visible:bool=False) -> None:
        """Adds the given layer to the Screen layers. If the visible is always visible, use the is_visible argument to specify."""
        if name in self.layers:
            print("WARNING: Screen: add_layer: Given layer_key already exists within Screen layers, overwriting existing.")
        #layers is used only for sprite groups, so one can be automatically placed
        self.layers[name] = pygame.sprite.Group()
        self.visible_layers[name] = pygame.sprite.Group()
    

    def remove_layer(self, name:str) -> None:
        """Removes the given layer from the Screen."""
        #only checks self.layers because if it's in self.layers it'll be in self.visible_layers
        if name in self.layers:
            del self.layers[name]
            del self.visible_layers[name]
            return
        print("ERROR: Screen: remove_layer: Invalid layer_key given for removal.")
        return
    

    def update_visible_layer(self, name:str, new_value:pygame.sprite.Group) -> None:
        try:
            self.visible_layers[name] = new_value
        except Exception as e:
            print(f"ERROR: Screen: update_visible_layer: {e}")
            return
    

    def set_fill_color(self, color:tuple[int, int, int]) -> None:
        """Sets the color that clears the screen before layers are drawn."""
        self.fill_color = color