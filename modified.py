import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lovers walking")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRASS_GREEN = (34, 139, 34)
SKY_BLUE = (135, 206, 235)
SKIN_COLOR = (255, 224, 189)

# Function to draw the sun
def draw_sun(screen, x, y, radius):
    pygame.draw.circle(screen, YELLOW, (x, y), radius)

# Function to draw the man
def draw_man(screen, x, y):
    pygame.draw.circle(screen, SKIN_COLOR, (x, y), 20)  # Head
    pygame.draw.rect(screen, BLUE, (x-10, y+20, 20, 40))  # Body
    pygame.draw.line(screen, SKIN_COLOR, (x, y+60), (x-20, y+80), 4)  # Left Leg
    pygame.draw.line(screen, SKIN_COLOR, (x, y+60), (x+20, y+80), 4)  # Right Leg
    pygame.draw.line(screen, SKIN_COLOR, (x-10, y+30), (x-30, y+50), 4)  # Left Arm
    pygame.draw.line(screen, SKIN_COLOR, (x+10, y+30), (x+30, y+50), 4)  # Right Arm

# Function to draw the woman
def draw_woman(screen, x, y):
    pygame.draw.circle(screen, SKIN_COLOR, (x, y), 20)  # Head
    pygame.draw.rect(screen, RED, (x-10, y+20, 20, 40))  # Body
    pygame.draw.line(screen, SKIN_COLOR, (x, y+60), (x-20, y+80), 4)  # Left Leg
    pygame.draw.line(screen, SKIN_COLOR, (x, y+60), (x+20, y+80), 4)  # Right Leg
    pygame.draw.line(screen, SKIN_COLOR, (x-10, y+30), (x-30, y+50), 4)  # Left Arm
    pygame.draw.line(screen, SKIN_COLOR, (x+10, y+30), (x+30, y+50), 4)  # Right Arm

# Function to draw a heart shape
def draw_heart(screen, x, y, size):
    pygame.draw.polygon(screen, RED, [
        (x, y - size // 2),
        (x - size // 2, y),
        (x, y + size // 2),
        (x + size // 2, y),
    ])
    pygame.draw.circle(screen, RED, (x - size // 4, y - size // 4), size // 4)
    pygame.draw.circle(screen, RED, (x + size // 4, y - size // 4), size // 4)

# Function to draw a single stripe
def draw_stripe(screen, width, height):
    stripe_width = width
    stripe_height = 10
    y = height // 2.7 + height // 4 - stripe_height // 2
    pygame.draw.rect(screen, WHITE, (0, y, stripe_width, stripe_height))

# Initial positions
man_x, man_y = 100, height // 4  # Start in the blue part
woman_x, woman_y = 160, height // 4 * 3  # Start in the green part
speed = 2

# Heart size and position
heart_size = 20
heart_max_size = 30
heart_min_size = 15

# Delay for heart pump animation
pump_delay = 100  # in milliseconds
last_pump_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions
    man_x += speed
    woman_x += speed

    # Reset positions if they move off-screen
    if man_x > width + 20:
        man_x = -40
    if woman_x > width + 20:
        woman_x = -40

    # Calculate heart position
    heart_x = (man_x + woman_x) // 2
    heart_y = (man_y + woman_y) // 2

    # Check if the cursor is over the heart
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if heart_x - heart_size < mouse_x < heart_x + heart_size and heart_y - heart_size < mouse_y < heart_y + heart_size:
        current_time = pygame.time.get_ticks()
        if current_time - last_pump_time > pump_delay:
            last_pump_time = current_time
            if heart_size == heart_min_size:
                heart_size = heart_max_size
            else:
                heart_size = heart_min_size
    else:
        heart_size = 20

    # Draw custom background: half blue and half green
    screen.fill(WHITE)  # Clear the screen first
    pygame.draw.rect(screen, SKY_BLUE, (0, 0, width, height // 2))  # Top half blue
    
    # Draw the lower part split into black and green
    pygame.draw.rect(screen, BLACK, (0, height // 2, width, height // 4))  # Upper part of the lower half black
    pygame.draw.rect(screen, GRASS_GREEN, (0, height // 2 + height // 4, width, height // 4))  # Lower part of the lower half green

    # Draw a single stripe
    draw_stripe(screen, width, height)

    # Draw the sun
    draw_sun(screen, 100, 100, 50)  # Sun positioned in the left part of the screen

    # Draw characters
    draw_man(screen, man_x, height // 2.5)  # Man in the blue part
    draw_woman(screen, woman_x, height //2.5)  # Woman 

    # Draw the heart only if dubai jana screen bhitra xa vane!!!
    if 0 <= man_x <= width and 0 <= woman_x <= width:
        draw_heart(screen, heart_x, heart_y, heart_size)
    
    # Update the display
    pygame.display.flip()

    # Delay to control frame rate
    pygame.time.delay(30)

pygame.quit()
sys.exit()