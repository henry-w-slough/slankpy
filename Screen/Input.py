import pygame

class Input():


    def __init__(self) -> None:
        """All keyboard and mouse input needed."""
        pass


    def key_pressed(self, *keys:int) -> bool:
        """Checks if the given keys are currently active and returns True if so."""
        for id in keys:
            if pygame.key.get_pressed()[id]:
                return True
        return False
        
        