"""Easily implemented debugging functionality that allows for quick developement testing with visual overlays.

Works by adding two "debug surfaces" which render respectively before and after Screen layer drawing. This
only happens if set_enabled is called and debugging is active.

To use, call toggle_enabled() once to turn debugging on and off, and call
any debugging functionality in the update loop of the game.
"""

from ..game_object.game_object import GameObject
import pygame


debug_enabled = False


_dirty_bottom = False
_dirty_top = False


#seperating into two layers so debug drawings can be on top and on bottom of drawn sprites
_debug_surface_bottom: pygame.Surface
_debug_surface_top: pygame.Surface


def init() -> None:
    global _debug_surface_bottom
    global _debug_surface_top
    _debug_surface_bottom = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)
    _debug_surface_top = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)


def toggle_enabled() -> None:
    """Toggles debugging rendering and functionality."""
    global debug_enabled
    debug_enabled = not debug_enabled


def draw_bottom(surface: pygame.Surface) -> None:
    """The rendering call for debug drawings that are to be drawn on the bottom of the layers of the game. 

    Works by taking the given surface and blitting the debug_surface_bottom onto it, which is the surface that
    is drawn to when debug drawing calls are made."""
    global _dirty_bottom
    global debug_enabled

    if not debug_enabled:
        return

    if _dirty_bottom:
        surface.blit(_debug_surface_bottom, (0, 0))

    _debug_surface_bottom.fill((0, 0, 0, 0))
    _dirty_bottom = False


def draw_top(surface: pygame.Surface) -> None:
    """The rendering call for debug drawings that are to be drawn on top of the layers of the game. 

    Works by taking the given surface and blitting the debug_surface_top onto it, which is the surface that
    is drawn to when debug drawing calls are made."""
    global _dirty_top
    global debug_enabled

    if not debug_enabled:
        return

    if _dirty_top:
        surface.blit(_debug_surface_top, (0, 0))

    _debug_surface_top.fill((0, 0, 0, 0))
    _dirty_top = False


def fill_hitbox(game_object: GameObject, color: tuple[int, int, int]) -> None:
    """Draws the rect (hitbox) of the given GameObject filled with the given color on the bottom buffer surface."""
    global _dirty_bottom
    _dirty_bottom = True
    pygame.draw.rect(_debug_surface_bottom, color, game_object.rect)


def fill_image(game_object: GameObject, color: tuple[int, int, int]) -> None:
    """ of the same size as the given game_object with the given color on the top buffer surface."""
    global _dirty_top

    mask = pygame.mask.from_surface(game_object.image)
    mask_surface = mask.to_surface(setcolor=color, unsetcolor=(0, 0, 0, 0))

    _debug_surface_top.blit(mask_surface, game_object.rect.topleft)
    _dirty_top = True
