import pygame

class Input():


    def __init__(self) -> None:
        """Class to access and handle all keyboard and mouse input events."""
        pass


    def get_key(self, *keys:int) -> bool:
        """Checks if any of the given keys are currently active."""
        for id in keys:
            if pygame.key.get_pressed()[id]:
                return True
        return False
        
        