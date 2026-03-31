from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..GameObject import GameObject

import pygame



def get_mask_rect(self_rect:pygame.Rect, mask:pygame.Mask) -> pygame.Rect:
    """Gets the rect of the mask provided by connecting rect bounds."""
    # Get mask bounds in world space
    bounds: list[pygame.Rect] = mask.get_bounding_rects() #type: ignore

    #if the bounds are empty, meaning the rect is completely filled
    if not bounds:
        return self_rect

    #the first rect
    mask_rect = pygame.Rect(bounds[0])

    #building the mask rect
    for r in bounds[1:]: 
        mask_rect.union_ip(r)

    # Offset to world space
    mask_rect.move_ip(self_rect.topleft)

    return mask_rect


def get_mask_overlap(mask1_rect:pygame.Rect, mask2_rect:pygame.Rect) -> list[int]:
    """Returns x and y values in a list of the overlap of two masks"""
    overlap_x = min(mask1_rect.right, mask2_rect.right) - max(mask1_rect.left, mask2_rect.left)
    overlap_y = min(mask1_rect.bottom, mask2_rect.bottom) - max(mask1_rect.top, mask2_rect.top)

    return [overlap_x, overlap_y]


def get_mask_collision(collider:GameObject.GameObject, layer:pygame.sprite.Group, ignores:list[GameObject.GameObject]) -> dict:
    """Returns the directions of Mask collision between a layer and an object in dictionary form: ("top": None, "bottom": None, "left": None, "right": None)"""

    collisions = {
        "top": None,
        "bottom": None,
        "left": None,
        "right": None
    }

    for obj in pygame.sprite.spritecollide(collider, layer, False, pygame.sprite.collide_mask):  # type: ignore

        #specficied in arguements
        if obj in ignores:
            continue

        collider_mask_rect = get_mask_rect(collider.rect, collider.mask)
        obj_mask_rect = get_mask_rect(obj.rect, obj.mask)
        overlap_x, overlap_y = get_mask_overlap(collider_mask_rect, obj_mask_rect)

        if overlap_x < overlap_y:
            if collider_mask_rect.centerx < obj_mask_rect.centerx:
                collisions["right"] = obj
            else:
                collisions["left"] = obj
        else:
            if collider_mask_rect.centery < obj_mask_rect.centery:
                collisions["bottom"] = obj
            else:
                collisions["top"] = obj

    return collisions

