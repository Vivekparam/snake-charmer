import enum
import pygame


class ResourceType(enum.StrEnum):
    APPLE = "apple"
    BANANA = "banana"
    IRON = "iron"


def resource_sprite(
    resource_type: ResourceType, position: pygame.Vector2
) -> "ResourceSprite":
    if resource_type == ResourceType.APPLE:
        return AppleSprite(position)
    elif resource_type == ResourceType.BANANA:
        return BananaSprite(position)
    elif resource_type == ResourceType.IRON:
        return IronSprite(position)
    else:
        raise ValueError(f"Unknown resource type: {resource_type}")


class ResourceSprite:
    def __init__(
        self,
        resource_type: ResourceType,
        position: pygame.Vector2,
        color_str: str = "black",
    ):
        self.position = position
        self.size = 5
        self.resource_type = resource_type
        self.color = color_str

    def center(self) -> pygame.Vector2:
        return self.position + pygame.Vector2(self.size / 2, self.size / 2)


class AppleSprite(ResourceSprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__(ResourceType.APPLE, position, color_str="red")


class BananaSprite(ResourceSprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__(ResourceType.BANANA, position, color_str="yellow")


class IronSprite(ResourceSprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__(ResourceType.IRON, position, color_str="gray")
