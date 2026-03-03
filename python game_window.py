import pygame
import math
import sys
import random

# ── Init ──────────────────────────────────────────────────────────────────────
pygame.init()

SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("CHAT TPG's Game Window")
clock = pygame.time.Clock()

# ── Colours ───────────────────────────────────────────────────────────────────
BG_DARK     = (8,   5,   5)
GRID_COL    = (40,  10,  10)
ACCENT_RED  = (220, 30,  30)
ACCENT_ORG  = (255, 100, 20)
DIM_WHITE   = (180, 170, 170)

# ── Load sprite ───────────────────────────────────────────────────────────────
try:
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    raw = pygame.image.load(os.path.join(BASE_DIR, "Bike.png")).convert_alpha()
    SPRITE_W = 260
    ratio = SPRITE_W / raw.get_width()
    SPRITE_H = int(raw.get_height() * ratio)
    bike_img = pygame.transform.smoothscale(raw, (SPRITE_W, SPRITE_H))
except Exception as e:
    print(f"Could not load image: {e}")
    bike_img = None
    SPRITE_H = 160

# ── Fonts ─────────────────────────────────────────────────────────────────────
font_big   = pygame.font.SysFont("couriernew", 48, bold=True)
font_med   = pygame.font.SysFont("couriernew", 22)
font_small = pygame.font.SysFont("couriernew", 15)

# ── Particle sparks ───────────────────────────────────────────────────────────
class Spark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, -8)
        self.vy = random.uniform(-1.5, 1.5)
        self.life = random.uniform(0.3, 0.8)
        self.max_life = self.life
        self.size = random.randint(2, 5)

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.05
        self.life -= dt

    def draw(self, surface):
        alpha = max(0.0, min(1.0, self.life / self.max_life))
        r = max(0, min(255, int(255 * alpha)))
        g = max(0, min(255, int(80 * alpha)))
        size = max(1, int(self.size * alpha))
        pygame.draw.circle(surface, (r, g, 0), (int(self.x), int(self.y)), size)

sparks = []
dash_x_positions = [i * 120 for i in range(8)]

def draw_glitch_text(surface, text, font, x, y, primary, glitch_col, t):
    offset = int(math.sin(t * 4) * 4)
    s1 = font.render(text, True, glitch_col)
    s2 = font.render(text, True, primary)
    surface.blit(s1, (x + offset, y + 2))
    surface.blit(s2, (x, y))

random.seed(99)
speed_lines = [(random.randint(0, SCREEN_W // 2),
                random.randint(180, SCREEN_H - 100),
                random.randint(30, 90)) for _ in range(18)]

t = 0.0
running = True

while running:
    dt = clock.tick(60) / 1000.0
    t += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    road_surface_y = SCREEN_H - 80
    bike_x = SCREEN_W // 2 - 100
    bike_y = road_surface_y - SPRITE_H

    if random.random() < 0.6:
        sparks.append(Spark(bike_x + 10, bike_y + SPRITE_H - 30))
    sparks = [s for s in sparks if s.life > 0]
    for s in sparks:
        s.update(dt)

    dash_x_positions = [(x - 10) % (SCREEN_W + 120) - 120 for x in dash_x_positions]

    screen.fill(BG_DARK)

    horizon_y = SCREEN_H // 2 + 60
    for i in range(horizon_y):
        ratio_sky = i / horizon_y
        r = int(8 + 30 * ratio_sky)
        pygame.draw.line(screen, (r, 5, 5), (0, i), (SCREEN_W, i))

    for x in range(0, SCREEN_W + 80, 80):
        pygame.draw.line(screen, GRID_COL, (x, horizon_y), (x, SCREEN_H))
    for row in range(8):
        y = horizon_y + int((row / 8) ** 1.6 * (SCREEN_H - horizon_y))
        pygame.draw.line(screen, GRID_COL, (0, y), (SCREEN_W, y))

    for lx, ly, length in speed_lines:
        sx = lx - int(t * 180) % (SCREEN_W + 200)
        pygame.draw.line(screen, (60, 15, 15), (sx, ly), (sx + length, ly), 1)

    for dx in dash_x_positions:
        pygame.draw.rect(screen, (80, 20, 20), (int(dx), road_surface_y, 80, 8))

    for s in sparks:
        s.draw(screen)

    if bike_img:
        screen.blit(bike_img, (bike_x, bike_y))
    else:
        pygame.draw.rect(screen, ACCENT_RED, (bike_x, bike_y, 260, 160))

    glow_surf = pygame.Surface((280, 30), pygame.SRCALPHA)
    glow_alpha = int(100 + 60 * math.sin(t * 3))
    pygame.draw.ellipse(glow_surf, (200, 20, 20, glow_alpha), (0, 0, 280, 30))
    screen.blit(glow_surf, (bike_x - 10, bike_y + SPRITE_H - 10))

    title = "CHAT TPG's Game Window"
    tw = font_big.size(title)[0]
    draw_glitch_text(screen, title, font_big,
                     (SCREEN_W - tw) // 2, 22, ACCENT_RED, ACCENT_ORG, t)

    sub = font_med.render("[ PYGAME  v2  //  FIRST PROJECT ]", True, DIM_WHITE)
    screen.blit(sub, ((SCREEN_W - sub.get_width()) // 2, 86))

    fps_txt = font_small.render(f"FPS: {int(clock.get_fps())}", True, ACCENT_RED)
    screen.blit(fps_txt, (12, 12))

    hint = font_small.render("ESC or [X] to quit", True, DIM_WHITE)
    screen.blit(hint, (SCREEN_W - hint.get_width() - 12, 12))

    pulse = int(abs(math.sin(t * 2)) * 180 + 60)
    pygame.draw.rect(screen, (pulse, 0, 0), (0, 0, SCREEN_W, SCREEN_H), 3)

    pygame.display.flip()

pygame.quit()
sys.exit()