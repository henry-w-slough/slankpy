import pygame


def is_key_pressed(*keys: int) -> bool:
    """Checks if the given keys are active in the current frame."""
    current_input = pygame.key.get_pressed()
    for key in keys:
        if current_input[key]:
            return True
    return False
