import paygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Ball properties
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_radius = 15
ball_dx, ball_dy = 5, 5

# Table properties (white rectangle)
table_top = HEIGHT * 0.7
table_rect = pygame.Rect(50, table_top, WIDTH - 100, HEIGHT - table_top - 50)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1
    if ball_y - ball_radius <= 0:
        ball_dy *= -1
    
    # Bounce off table
    if (table_rect.collidepoint(ball_x, ball_y) and ball_dy > 0):
        ball_dy *= -1
    
    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, table_rect)
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()