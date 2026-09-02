"""Keyboard input detection module.

Contains functionality for input detection along with special cases such as
current-frame input or axis-translated floats."""

import pygame



def get_pressed_keys() -> pygame.key.ScancodeWrapper:
    """Gets all keys that are pressed this frame."""
    return pygame.key.get_pressed()


def keys_pressed(*keys: int) -> bool:
    """Checks if the given keys are pressed this frame."""
    for key in keys:
        if pygame.key.get_pressed()[key]:
            return True
    return False


def keys_just_pressed(*keys: int) -> bool:
    """Checks if any of the given keys are pressed this frame without consecutive active frames."""
    for key in keys:
        if pygame.key.get_just_pressed()[key]:
            return True
    return False


def get_input_vector(input_x: tuple[int, int], input_y: tuple[int, int]) -> pygame.math.Vector2:
    """
    """
    axis = pygame.math.Vector2()

    for key in input_x:
        if keys_pressed()

    return axis
            



        