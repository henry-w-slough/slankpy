

class Transform:


    def __init__(self, width:int, height:int) -> None:
        """Holds the position, rotation, and scale for a GameObject."""

        #Only position right now...
        #Scale and Rotation will be added later down the line with Sprite additions.
        self.x: float = 0.0
        self.y: float = 0.0 

        self.width: float = 0
        self.height: float = 0