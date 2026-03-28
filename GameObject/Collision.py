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
