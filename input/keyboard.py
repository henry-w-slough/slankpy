import pygame



def get_pressed_keys() -> pygame.key.ScancodeWrapper:
    """Gets all keys that are pressed this frame."""
    return pygame.key.get_pressed()


def is_key_pressed(key: int) -> bool:
    """Checks if the key is pressed this frame."""
    return pygame.key.get_pressed()[key] 


def is_key_just_pressed(key: int) -> bool:
    """Checks if the key is pressed this frame without consecutive active frames."""
    return pygame.key.get_just_pressed()[key]

        