
class Transform():
    

    def __init__(self) -> None:
        """Holds all position (world and viewport) and size data for a GameObject."""

        self.world_x = 0
        self.world_y = 0

        self.viewport_x = 0
        self.viewport_y = 0

        self.width = 0
        self.height = 0

        