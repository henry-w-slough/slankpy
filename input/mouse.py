import pygame


def get_pressed_buttons() -> tuple[bool, bool, bool]:
    """Gets all mouse buttons active this frame."""
    return pygame.mouse.get_pressed()


def is_mouse_pressed(button: int) -> bool:
    """Checks if the given mouse button is pressed this frame."""
    
 
    
    if pygame.mouse.get_pressed()[button]:
        return True
    return False


def is_mouse_just_pressed(button: int) -> bool:
    """Checks if the given mouse button is pressed this frame without consecutive active frames."""
    
    if pygame.mouse.get_just_pressed()[button]:
        return True 
    return False


def is_mouse_over_object(object:)