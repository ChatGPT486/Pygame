import pygame
import sys
import os

# ── Init ──────────────────────────────────────────────────────────────────────
pygame.init()

# Window - at least 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CHAT TPG's Game Window")

clock = pygame.time.Clock()

# ── Bonus: Load sprite ────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    sprite = pygame.image.load(os.path.join(BASE_DIR, "Bike.png")).convert_alpha()
except:
    sprite = None

# ── Bonus: Font for name ──────────────────────────────────────────────────────
font = pygame.font.SysFont("couriernew", 36, bold=True)
name_text = font.render("CHAT TPG", True, (220, 30, 30))

# ── Main loop ─────────────────────────────────────────────────────────────────
running = True
while running:

    # Handle events - proper close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    screen.fill((0, 0, 0))

    # Bonus: draw sprite center screen
    if sprite:
        x = (800 - sprite.get_width()) // 2
        y = (600 - sprite.get_height()) // 2
        screen.blit(sprite, (x, y))

    # Bonus: draw name as text
    screen.blit(name_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

# Proper quit - no force quit needed
pygame.quit()
sys.exit()