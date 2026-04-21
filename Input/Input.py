import pygame


def is_key_pressed(*keys:int) -> bool:
    """Checks if any of the given keys are currently active."""

    #if no specific keys are given, returns whether or not there is any keys pressed
    if len(keys) == 0:
        if any(pygame.key.get_pressed()):
            return True
    
    #iterates through every key given
    for id in keys:
        #if any are True, returns so
        if pygame.key.get_pressed()[id]:
            return True
        
    return False


def get_input_vector(key1:int, key2:int) -> int:
    """Gets the given input as a 2D vector, meaning it can be used for opposing input handling. Note that vector x and y values are returned in values of 1 or -1, meaning they are by default normalized."""
    vector = 0
    if pygame.key.get_pressed()[key1]:
        vector -= 1
    if pygame.key.get_pressed()[key2]:
        vector += 1

    return vector


def get_mouse_position() -> tuple[int, int]:
    """Returns the position of the mouse cursor."""
    return pygame.mouse.get_pos()
        
        