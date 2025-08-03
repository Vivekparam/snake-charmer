from multiprocessing.util import DEBUG
import pygame

from run_config import ACTION_HEIGHT, GAME_HEIGHT, GAME_WIDTH, RESOURCES_BAR_HEIGHT
from state.resources import ResourceType
from state.state import State


def loop():
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    state = State()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            state.player.position.y -= 300 * dt
        if keys[pygame.K_s]:
            state.player.position.y += 300 * dt
        if keys[pygame.K_a]:
            state.player.position.x -= 300 * dt
        if keys[pygame.K_d]:
            state.player.position.x += 300 * dt

        # Check if player is standing on food
        state.grab_resources()
        state.update()
        draw_state(screen, state)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000


def draw_state(screen: pygame.Surface, state: State):
    # Draw action field
    action_field = pygame.Surface((GAME_WIDTH, ACTION_HEIGHT))
    if DEBUG:
        action_field.fill("lightgray")
    screen.blit(action_field, (0, 0))

    # Draw all resources in the state
    for resource in state.actors.resources:
        pygame.draw.circle(
            screen,
            resource.color,
            (int(resource.position.x), int(resource.position.y)),
            resource.size,
        )
    if DEBUG:
        pygame.draw.rect(screen, "blue", state.resource_spawner.bounds, 1)

    # Draw player
    pygame.draw.rect(
        screen,
        state.player.color,
        pygame.Rect(
            state.player.position.x,
            state.player.position.y,
            state.player.size,
            state.player.size,
        ),
    )

    # Draw resources bar at bottom
    resources_bar = pygame.Surface((GAME_WIDTH / 3, RESOURCES_BAR_HEIGHT))
    resources_bar.fill("white")
    pygame.draw.rect(
        resources_bar,
        "black",
        pygame.Rect(0, 0, GAME_WIDTH / 3, RESOURCES_BAR_HEIGHT),
        width=3,
    )
    resources_font = pygame.font.Font(None, 25)
    apples_text = resources_font.render(
        f"Apples: {state.player.inventory.get_resource_amount(ResourceType.APPLE)}",
        True,
        "black",
    )
    bananas_text = resources_font.render(
        f"Bananas: {state.player.inventory.get_resource_amount(ResourceType.BANANA)}",
        True,
        "black",
    )
    iron_text = resources_font.render(
        f"Iron: {state.player.inventory.get_resource_amount(ResourceType.IRON)}",
        True,
        "black",
    )
    resources_bar.blit(apples_text, (10, 10))
    resources_bar.blit(bananas_text, (10, 30))
    resources_bar.blit(iron_text, (10, 50))
    screen.blit(resources_bar, (0, GAME_HEIGHT - RESOURCES_BAR_HEIGHT))


loop()
