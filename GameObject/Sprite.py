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
        if self.texture.get_width() != width or self.texture.get_height() != height:
            self.texture = pygame.transform.scale(self.texture, (width, height))
        self.width = width
        self.height = height


    def get_sprite(self, animation_name:str, sprite_index:int) -> pygame.Surface:

        #checking if the animation exists
        if animation_name not in self.animations:
            print("ERROR: Sprite: get_sprite: Given animation name does not exist.")

        #excepting an invalid index, returns a placeholder surface thats black
        try:
            return self.animations[animation_name][sprite_index]
        except KeyError:
            print(f"ERROR: Sprite: get_sprite: Given sprite index does not exist.")
            return pygame.Surface((32, 32))


    def load_sprites(self, src:str, name:str, sprite_rows:int, sprite_columns:int) -> None:
        """Adds the sprites from the given image to an animation of the given name."""
        
        #attempting image loading
        try:
            spritesheet = pygame.image.load(src)
        except Exception as e:
            print(f"ERROR: Sprite: load_sprites: {e}")
            return

        #creating new animation dict for the new sprites
        self.animations[name] = {}

        #calculating size of sprite from the given num of sprites and the full size
        sprite_width = spritesheet.get_width() / sprite_rows
        sprite_height = spritesheet.get_height() / sprite_columns

        #used to track the total number of sprites iterated over
        sprite_num = 0

        #going through each sprite
        for sr in range(sprite_rows):
            for sc in range(sprite_columns):
                sprite_num += 1
                #calculating the rect of the new sprite within the context of the spritesheet
                sprite_rect = pygame.Rect(sr*sprite_width, sc*sprite_height, sprite_width, sprite_height)
                #cutting the new sprite out
                new_sprite = spritesheet.subsurface(sprite_rect)
                #adding the new sprite at the index of sprite_num
                self.animations[name][sprite_num] = new_sprite


        


    