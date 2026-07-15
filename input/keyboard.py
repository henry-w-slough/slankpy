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


def get_input_axis(keys: tuple[int, int]) -> float:
    """The input axis for the given keys.

    An input axis is a representation of two inputs' states with a float value of -1, 1, or 0.

    -1 Represents the first value being active, 1 is the second value being active, and 0 is
    either both active at the same time or neither active.
    """
    axis = 0.0

    if is_key_pressed(keys[0]):
        axis -= 1.0
    if is_key_pressed(keys[1]):
        axis += 1.0

    return axis
            



        