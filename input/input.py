import pygame


def key_pressed(key: int) -> bool:
    """Checks whether the given key is being currently pressed."""
    return pygame.key.get_pressed()[key] 
        