import pygame
import numpy as np

from state.resources import ResourceSprite, ResourceType, resource_sprite


class ResourceSpawner:
    def __init__(self, bounds: pygame.Rect):
        self.bounds = bounds
        self.probabilities = {
            "items": [None, ResourceType.APPLE, ResourceType.BANANA, ResourceType.IRON],
            "frequencies": [0.990, 0.006, 0.002, 0.002],
        }

    def try_spawn_resource(self) -> ResourceSprite | None:
        result: ResourceType | None = np.random.choice(
            self.probabilities["items"], p=self.probabilities["frequencies"]
        )
        if result is None:
            return None
        sprite: ResourceSprite = resource_sprite(
            result, position=self._get_random_position()
        )
        return sprite

    def _get_random_position(self) -> pygame.Vector2:
        x = np.random.uniform(self.bounds.left, self.bounds.right)
        y = np.random.uniform(self.bounds.top, self.bounds.bottom)
        return pygame.Vector2(x, y)
