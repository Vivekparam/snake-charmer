import pygame

from inventory import Inventory


class Player:
    def __init__(self, starting_x: int, starting_y: int, size: int = 30):
        self.position = pygame.Vector2(starting_x, starting_y)
        self.inventory = Inventory()
        self.color = "black"
        self.size = size

    def center(self) -> pygame.Vector2:
        return self.position + pygame.Vector2(self.size / 2, self.size / 2)
