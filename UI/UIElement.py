import pygame
from ..GameObject import GameObject

pygame.font.init()

class UIElement(GameObject.GameObject):
    

    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.text = ""
        self.previous_text = ""

        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0, 255)

        self.font_cache = {}


    def get_font(self, size: int) -> pygame.font.Font:
        """Get a cached font object of the given size."""
        if size not in self.font_cache:
            self.font_cache[size] = pygame.font.Font("font.ttf", size)
        return self.font_cache[size]
    

    def set_text(self, text:str, text_color:tuple=(255, 255, 255, 0), background_color:tuple=(0, 0, 0)) -> None:
        """Sets the text displayed to the given string."""

        self.image.fill(self.background_color)

        self.text = text

        #uses default font unless other is specified through function
        self.font = pygame.font.get_default_font()

        self.text_color = text_color
        self.background_color = background_color
        

    def update(self) -> None:

        #more efficient when the text hasn't changed
        if self.text != self.previous_text:
        
            temp = self.image

            #lowest and highest font sizes
            low = 1
            high = min(self.rect.width, self.rect.height) // 2

            best_size = low
            
            #until high and low are ==, or there is no more sizes to iterate through
            while low <= high:
                #middle size of the font sizes
                mid = (low + high) // 2

                #rendering the text with the new size of mid
                font = self.get_font(mid)
                text_image = font.render(self.text, False, self.text_color)
                
                #if the size is too small
                if text_image.get_width() <= self.rect.width * 0.9 and text_image.get_height() <= self.rect.height * 0.9:
                    best_size = mid
                    low = mid + 1
                #if the size is too big
                else:
                    high = mid - 1
            

            #rendering final font
            font = self.get_font(best_size)
            text_image = font.render(self.text, False, self.text_color)

            #calculating position based on object and text size
            x = (self.rect.width - text_image.get_width()) // 2
            y = (self.rect.height - text_image.get_height()) // 2


            temp.blit(text_image, (x, y))
            self.image = temp

        self.previous_text = self.text



