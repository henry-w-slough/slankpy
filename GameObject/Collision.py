import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..GameObject import GameObject # Only imported during type checking


class Collision:


    def __init__(self, game_object: "GameObject.GameObject") -> None:
        """Handles collision detection and positional resolution for a GameObject."""
        self.game_object = game_object


    def _get_mask(self) -> pygame.mask.Mask:
        return pygame.mask.from_surface(self.game_object.image)


    def check_rect(self, group: pygame.sprite.Group) -> list["GameObject.GameObject"]:
        """Returns all sprites in the group whose rect overlaps this object's rect."""
        return pygame.sprite.spritecollide(
            self.game_object, group, False #type: ignore
        )

    def check_mask(self, group: pygame.sprite.Group) -> list["GameObject.GameObject"]:
        """Returns all sprites in the group whose mask overlaps this object's mask.
        Requires each sprite to have an 'image' surface for mask generation."""
        return pygame.sprite.spritecollide(
            self.game_object, group, False, #type: ignore
            collided=pygame.sprite.collide_mask
        )

    def check_rect_single(self, other: "GameObject.GameObject") -> bool:
        """Returns True if this object's rect overlaps another object's rect."""
        return self.game_object.rect.colliderect(other.rect)

    def check_mask_single(self, other: "GameObject.GameObject") -> bool:
        """Returns True if this object's mask overlaps another object's mask."""
        offset = (
            other.rect.x - self.game_object.rect.x,
            other.rect.y - self.game_object.rect.y
        )
        self_mask = self._get_mask()
        other_mask = pygame.mask.from_surface(other.image)
        return self_mask.overlap(other_mask, offset) is not None
    

    def resolve_rect(self, group: pygame.sprite.Group) -> None:
        """Pushes this object out of any rect overlaps in the group.
        Resolves along the axis of smallest overlap."""
        hits = self.check_rect(group)
        for other in hits:
            self._resolve_overlap(self.game_object.rect, other.rect)


    def resolve_mask(self, group: pygame.sprite.Group) -> None:
        """Pushes this object out of any mask overlaps in the group.
        Uses rect bounds to determine displacement direction."""
        hits = self.check_mask(group)
        for other in hits:
            self._resolve_overlap(self.game_object.rect, other.rect)


    def _resolve_overlap(
        self, rect: pygame.Rect, other_rect: pygame.Rect
    ) -> None:
        """Displaces rect out of other_rect along the axis of smallest penetration depth."""
        dx = self._overlap_x(rect, other_rect)
        dy = self._overlap_y(rect, other_rect)

        # Push along whichever axis has less penetration — minimises jitter
        if abs(dx) <= abs(dy):
            self.game_object.rect.x += dx
        else:
            self.game_object.rect.y += dy


    @staticmethod
    def _overlap_x(rect: pygame.Rect, other: pygame.Rect) -> int:
        """Returns signed horizontal displacement to separate rect from other."""
        if rect.centerx < other.centerx:
            return other.left - rect.right   # push left
        return other.right - rect.left       # push right


    @staticmethod
    def _overlap_y(rect: pygame.Rect, other: pygame.Rect) -> int:
        """Returns signed vertical displacement to separate rect from other."""
        if rect.centery < other.centery:
            return other.top - rect.bottom   # push up
        return other.bottom - rect.top       # push down
    

    def resolve_rect_x(self, group):
        for other in pygame.sprite.spritecollide(self.game_object, group, False): #type: ignore
            self.game_object.rect.x += self._overlap_x(self.game_object.rect, other.rect)

    def resolve_rect_y(self, group):
        for other in pygame.sprite.spritecollide(self.game_object, group, False): #type: ignore
            self.game_object.rect.y += self._overlap_y(self.game_object.rect, other.rect)
