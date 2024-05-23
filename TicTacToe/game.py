import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player properties
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 50  # Adjusted the y position to make the character visible
player_vel_y = 0
jump_force = -10
gravity = 0.5

# Define obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_vel = 5
obstacle_frequency = 25  # Lower values increase frequency

obstacles = []

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y == screen_height - player_height:
        player_vel_y = jump_force

    player_vel_y += gravity
    player_y += player_vel_y

    # Generate obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = screen_width
        obstacle_y = screen_height - obstacle_height
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_vel
        pygame.draw.rect(screen, BLACK, obstacle)

        # Collision detection
        if obstacle.colliderect((player_x, player_y, player_width, player_height)):
            running = False  # Game over if collision occurs

    # Draw player character
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))  # Body
    pygame.draw.rect(screen, BLACK, (player_x + 15, player_y + 10, 10, 10))  # Left eye
    pygame.draw.rect(screen, BLACK, (player_x + 30, player_y + 10, 10, 10))  # Right eye

    # Update display
    pygame.display.flip()

    # Clear screen
    screen.fill(WHITE)

    # Control frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
