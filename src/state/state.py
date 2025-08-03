import pygame

from state.resources import ResourceSprite
from run_config import (
    ACTION_HEIGHT,
    GAME_WIDTH,
    RESOURCE_COLLECTION_AREA_HEIGHT,
    RESOURCE_COLLECTION_AREA_WIDTH,
)
from state.actors import Actors
from state.player import Player
from state.resource_spawner import ResourceSpawner

from loguru import logger as log


class State:
    def __init__(self):
        self.actors = Actors()
        self.player = Player(
            GAME_WIDTH // 2,
            ACTION_HEIGHT + RESOURCE_COLLECTION_AREA_HEIGHT // 2,
            size=30,
        )

        self.resource_spawner = ResourceSpawner(
            pygame.Rect(
                (GAME_WIDTH / 2) - 150,
                ACTION_HEIGHT,
                RESOURCE_COLLECTION_AREA_WIDTH,
                RESOURCE_COLLECTION_AREA_HEIGHT,
            )
        )

    def update(self):
        resource: ResourceSprite | None = self.resource_spawner.try_spawn_resource()
        if resource:
            self.actors.resources.append(resource)

    def grab_resources(self):
        for resource in self.actors.resources:
            # overlap = consume
            if self.player.center().distance_to(resource.center()) < (
                self.player.size * 1.5 / 2
            ) + (resource.size * 1.5 / 2):
                # TODO: add an animation when the resource disappears
                self.actors.resources.remove(resource)
                self.player.inventory.add_resource(resource.resource_type, 1)
                log.debug(f"Player consumed {resource.resource_type}!")
