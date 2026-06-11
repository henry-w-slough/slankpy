import pygame


class Sprite():


    def __init__(self, width:float, height:float) -> None:
        """Handles all animation and sprite-related operations to a GameObject.
        
        Holds a Sprite image, which is the image drawn on the GameObject image on the screen."""
        
        self.width = width
        self.height = height

        self.image = pygame.Surface((width, height))
        self._image_unmodified = pygame.Surface((width, height))

        self.animations: dict[str, dict[int, pygame.Surface]] = {}
    
    
    @property
    def image_unmodified(self) -> pygame.Surface:
        """The untransformed image of the sprite, unaffected by operations like rotation."""
        return self._image_unmodified


    def fill_color(self, color:tuple[int, int, int]) -> None:
        """Fills the image with the given color."""
        self.image.fill(color)
        self.image_unmodified.fill(color)
    

    def set_sprite(self, animation_name: str, sprite_index: int) -> None:
        self._image_unmodified = self.animations[animation_name][sprite_index]
        self.image = pygame.transform.scale(self.animations[animation_name][sprite_index], (self.width, self.height))


    def add_animation(self, name: str, src: str, sprite_rows: int, sprite_columns: int) -> None:
        """Adds an animation from the given image source 
        
        The given image is cut into seperate sprites based on the amount of sprite rows and columns provided.
        
        Sprites are added by their placement from left to right in the spritesheet, starting at 0."""

        spritesheet = pygame.image.load(src).convert_alpha()

        #empty animation dict
        self.animations[name] = {}

        #calculating size of sprite from the given num of sprites and the full size
        sprite_width = spritesheet.get_width() / sprite_rows
        sprite_height = spritesheet.get_height() / sprite_columns

        sprite_num = 0

        column = 0
        row = 0
        
        #the surface rect of each sprite
        sprite_rect = pygame.Rect(0, 0, sprite_width, sprite_height)

        while column != sprite_columns:
            
            #prevents making a new rect every frame
            sprite_rect.x = row*sprite_width
            sprite_rect.y = column*sprite_height

            #section of image for new sprite
            new_sprite = spritesheet.subsurface(sprite_rect)

            self.animations[name][sprite_num] = new_sprite

            sprite_num += 1

            #iterating over from left to right of the image
            row += 1
            if row == sprite_rows:
                column += 1
                row = 0
    