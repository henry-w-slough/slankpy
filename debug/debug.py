from ..game_object.game_object import GameObject
import pygame


_dirty = False
_debug_surface: pygame.Surface


def _init() -> None:
    global _debug_surface
    _debug_surface = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)


def _draw(surface: pygame.Surface) -> None:
    """The rendering process for all debug drawing calls made through this frame.
    
    Works by taking the given surface and blitting the debug_surface onto it, which is the surface that
    is drawn to when debug drawing calls are made."""
    global _dirty

    if _dirty:
        surface.blit(_debug_surface, (0, 0))

    _debug_surface.fill((0, 0, 0, 0))
    _dirty = False


def draw_object_hitbox(game_object: GameObject, color: tuple[int, int, int]) -> None:
    """Draws the rect (hitbox) of the given GameObject filled with the given color on the buffer surface."""
    global _dirty
    _dirty = True
    pygame.draw.rect(_debug_surface, color, game_object.rect)


