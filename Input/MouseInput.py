import pygame


def get_mouse_position() -> tuple[int, int]:
    """Returns the position of the mouse cursor."""
    return pygame.mouse.get_pos()


def is_mouse_clicked(*buttons:int) -> bool:
    """Returns whether or not the given mouse buttons have been clicked. Note that only buttons (0=LEFT, 1=RIGHT) are detected and returned. All other mouse buttons result in error."""
    for b in buttons:

        try:
            if pygame.mouse.get_pressed()[b]:
                return True
        except IndexError as e:
            print("ERROR: MouseInput: is_mouse_clicked: Given integer for mouse button detection is invalid. Use 0 for left click, and 1 for right click.")
            break
        
    return False        
        