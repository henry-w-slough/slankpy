import pygame


class Transform:


    def __init__(self, width: float, height: float) -> None:
        """Holds the position, rotation, and scale for a GameObject."""

        self.x: float = 0.0
        self.y: float = 0.0

        self.width: float = width
        self.height:float = height

        self.rotation: float = 0.0