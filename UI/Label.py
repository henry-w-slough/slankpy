import pygame
from ..GameObject import GameObject

pygame.font.init()


class Label(GameObject.GameObject):
    def __init__(self, width: int, height: int, font_src: str, *groups: pygame.sprite.Group) -> None:
        """Represents any object that has text on its surface. Inherits from GameObject.
        All functions from GameObject can be used, including Sprite changes and rect transformations."""
        super().__init__(width, height, *groups)

        #uses pygame.SRCALPHA for transparency
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        self.text = ""
        self.previous_text = ""

        self.text_color = (255, 255, 255, 255)
        self.background_color = (0, 0, 0, 255)

        self.font_src = font_src

        #cache for storing font data
        self.font_cache = {}

        #whether or not the object's been changed this frame...
        self.is_dirty = True


    def set_font_src(self, font_src: str) -> None:
        """Sets the font source. Clears the font cache to store unuseable information."""
        self.font_src = font_src
        self.font_cache.clear()
        self.is_dirty = True


    def get_font_by_size(self, size: int) -> pygame.font.Font:
        """Returns a cached font of the given size, loading it if not already cached."""
        if size not in self.font_cache:
            if isinstance(self.font_src, str):
                try:
                    self.font_cache[size] = pygame.font.Font(self.font_src, size)
                except FileNotFoundError:
                    self.font_cache[size] = pygame.font.SysFont("Arial", size)
            else:
                self.font_cache[size] = pygame.font.SysFont("Arial", size)
        return self.font_cache[size]


    def set_text(self, text: str) -> None:
        """Sets the displayed text."""
        self.text = text


    def set_text_color(self, color: tuple) -> None:
        """Sets the text color. Accepts RGB or RGBA."""
        self.text_color = color
        self.is_dirty = True


    def set_background_color(self, color: tuple) -> None:
        """Sets the background color. Accepts RGB or RGBA."""
        self.background_color = color
        self.is_dirty = True


    def fit_font_size(self) -> int:
        """Binary search for the largest font size that fits within 90% of the element's dimensions."""
        low, high = 1, min(self.rect.width, self.rect.height) // 2
        best_size = low
        max_w = self.rect.width * 0.9
        max_h = self.rect.height * 0.9

        while low <= high:
            mid = (low + high) // 2
            font = self.get_font_by_size(mid)
            w, h = font.size(self.text)  # faster than rendering
            if w <= max_w and h <= max_h:
                best_size = mid
                low = mid + 1
            else:
                high = mid - 1

        return best_size


    def render_text(self, font: pygame.font.Font) -> pygame.Surface:
        """Renders the text with correct color and alpha onto an SRCALPHA surface."""
        rgb = self.text_color[:3]
        alpha = self.text_color[3] if len(self.text_color) == 4 else 255

        # Render onto SRCALPHA surface to preserve alpha compositing
        base = font.render(self.text, True, rgb)
        result = pygame.Surface(base.get_size(), pygame.SRCALPHA)
        result.blit(base, (0, 0))

        # Multiply alpha across every pixel
        if alpha < 255:
            alpha_mask = pygame.Surface(base.get_size(), pygame.SRCALPHA)
            alpha_mask.fill((255, 255, 255, alpha))
            result.blit(alpha_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        return result


    def redraw(self) -> None:
        """Redraws the element surface with the current text and colors."""
        self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)

        # Background — SRCALPHA surface respects RGBA fill
        bg = self.background_color if len(self.background_color) == 4 else (*self.background_color, 255)
        self.image.fill(bg)

        if self.text:
            size = self.fit_font_size()
            font = self.get_font_by_size(size)
            text_surface = self.render_text(font)
            x = (self.rect.width - text_surface.get_width()) // 2
            y = (self.rect.height - text_surface.get_height()) // 2
            self.image.blit(text_surface, (x, y))


    def update(self) -> None:
        if self.text != self.previous_text or self.is_dirty:
            self.redraw()
            self.previous_text = self.text
            self.is_dirty = False

