import pygame

class Sprite():


    def __init__(self, width:int, height:int) -> None:
        """Holds all that's needed for animation and sprites for a GameObject."""
        
        self.texture = pygame.Surface((width, height))

        self.width = width
        self.height = height

        #idea is that a dict holding animation dict, 
        #holding sprites with an index
        self.animations = {
            
        }


    def set_size(self, width:int, height:int) -> None:

        self.texture = pygame.transform.scale(self.texture, (width, height))

        self.width = width
        self.height = height


    def set_sprite(self, animation_name:str, sprite_index:int) -> None:
        """Sets the given texture of this sprite to the one given. Returns a surface for setting another objects image."""
        
        new_sprite = pygame.Surface((self.width, self.height))
        #checking if the animation exists
        if animation_name not in self.animations:
            print(f"ERROR: Sprite: get_sprite: Given animation name {animation_name} does not exist.")
        else:
            try:
                #returns the sprite transformed to the current size
                new_sprite = pygame.transform.scale(self.animations[animation_name][sprite_index], (self.width, self.height))
            except KeyError:
                print(f"ERROR: Sprite: get_sprite: Given sprite index {sprite_index} does not exist.")

        #returning and setting new_sprite
        self.texture = new_sprite


    def add_sprites(self, src:str, name:str, sprite_rows:int, sprite_columns:int) -> None:
        """Adds the sprites from the given image to an animation of the given name."""
        
        #attempting image loading
        try:
            spritesheet = pygame.image.load(src)
            spritesheet.convert_alpha()
        except Exception as e:
            print(f"ERROR: Sprite: load_sprites: {e}")
            return

        #creating new animation dict for the new sprites
        self.animations[name] = {}

        #calculating size of sprite from the given num of sprites and the full size
        sprite_width = spritesheet.get_width() / sprite_rows
        sprite_height = spritesheet.get_height() / sprite_columns


        #tracks total number of sprites iterated over
        sprite_num = 0

        #tracks the current column and row of iteration
        column = 0
        row = 0

        while column != sprite_columns:

            #calculating the rect of the new sprite within the context of the spritesheet
            sprite_rect = pygame.Rect(row*sprite_width, column*sprite_height, sprite_width, sprite_height)
            #cutting the new sprite out
            #note it's unscaled, when accessing a sprite properly, the sprite will be transformed when accessed then
            new_sprite = spritesheet.subsurface(sprite_rect)

            self.animations[name][sprite_num] = new_sprite

            sprite_num += 1

            #adding 1 to row, and when the row end is met,
            #we go to the beginning of the next row
            row += 1
            if row == sprite_rows:
                column += 1
                row = 0


        


    