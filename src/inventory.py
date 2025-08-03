from state.resources import ResourceType


class Inventory:
    def __init__(self):
        self.resources: dict[ResourceType, int] = {
            ResourceType.APPLE: 0,
            ResourceType.BANANA: 0,
            ResourceType.IRON: 0,
        }
        self.other = {}

    def add_resource(self, resource_type: ResourceType, amount: int) -> None:
        if resource_type in self.resources:
            self.resources[resource_type] += amount
        else:
            raise ValueError(f"Unknown resource type: {resource_type}")

    def get_resource_amount(self, resource_type: ResourceType) -> int:
        return self.resources.get(resource_type, 0)
