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
        
        