import pygame


class Sprite():


    def __init__(self, width: float, height: float) -> None:
        """Handles all animation and sprite-related operations to a GameObject."""
        
        self._width: float = width
        self._height: float = height

        self._image = pygame.Surface((width, height))
        self._image_unmodified = pygame.Surface((width, height))

        self.animations: dict[str, dict[int, pygame.Surface]] = {}

        #this should never be called for reference of rotation, only Transform should
        self._rotation: float = 0.0


    @property
    def image(self) -> pygame.Surface:
        return self._image
    

    def _update_image(self) -> None:
        """Refreshes the image by setting it to the current unmodified sprite with the current transformations."""
        #this if logic is only here for performance so a rotozoom call doesn't always fire
        if self._rotation != 0:
            #use 1.0 scale because scale is applied after for custom width and height
            self._image = pygame.transform.scale(self._image_unmodified, (self._width, self._height))  
            self._image = pygame.transform.rotozoom(self._image, self._rotation, 1.0)
        else:
            self._image = pygame.transform.scale(self._image_unmodified, (self._width, self._height))


    @property
    def width(self) -> float:
        return self._width
    

    @width.setter
    def width(self, width: float) -> None:
        self._width = width
        self._update_image()
        
    
    @property
    def height(self) -> float:
        return self._height
    

    @height.setter
    def height(self, height: float) -> None:
        self._height = height
        self._update_image()    


    @property
    def rotation(self) -> float:
        return self._rotation
    

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        self._rotation = rotation
        self._update_image()
    

    def set_sprite(self, animation_name: str, sprite_index: int) -> None:
        """Sets the image of the Sprite to the given animation and sprite index."""
        self._image_unmodified = self.animations[animation_name][sprite_index]
        self._update_image()


    def add_animation(self, animation_name: str, src: str, sprite_rows: int, sprite_columns: int) -> None:
        """Adds an animation from the given image source 
        
        The given image is cut into seperate sprites based on the amount of sprite rows and columns provided.
        
        Sprites are added by their placement from left to right in the spritesheet, starting at 0."""

        spritesheet = pygame.image.load(src).convert_alpha()

        #empty animation dict
        self.animations[animation_name] = {}

        sprite_width = spritesheet.get_width() / sprite_columns
        sprite_height = spritesheet.get_height() / sprite_rows

        sprite_num = 0

        #used to track the current iteration through the sheet
        column = 0
        row = 0

        #the 'cut out' for each sprite
        sprite_rect = pygame.Rect(0, 0, sprite_width, sprite_height)

        while row != sprite_rows:

            sprite_rect.x = round(column*sprite_width)
            sprite_rect.y = round(row*sprite_height)

            #cutting out new sprite
            new_sprite = spritesheet.subsurface(sprite_rect)

            #adding new sprite
            self.animations[animation_name][sprite_num] = new_sprite
            
            #iterating to next sprite
            sprite_num += 1
            column += 1
            if column == sprite_columns:
                row += 1
                column = 0
    