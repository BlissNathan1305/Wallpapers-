
from PIL import Image, ImageDraw, ImageFilter
import math
import random
import colorsys
import os

# Create output directory
os.makedirs("wallpapers", exist_ok=True)

# 4K vertical resolution
WIDTH, HEIGHT = 2160, 3840
CENTER = (WIDTH // 2, HEIGHT // 2)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def apply_radial_gradient(img, intensity=0.6):
    gradient = Image.new("L", (WIDTH, HEIGHT), 0)
    draw = ImageDraw.Draw(gradient)
    for i in range(max(WIDTH, HEIGHT)):
        opacity = int(255 * (1 - intensity * i / max(WIDTH, HEIGHT)))
        draw.ellipse([
            CENTER[0] - i, CENTER[1] - i,
            CENTER[0] + i, CENTER[1] + i
        ], fill=opacity)
    black_overlay = Image.new("RGB", (WIDTH, HEIGHT), "black")
    img.paste(black_overlay, (0, 0), gradient)

def design_radial_symmetry(draw):
    count = 60
    radius = 1400
    angle_step = 360 / count
    for i in range(count):
        angle = math.radians(i * angle_step)
        x = CENTER[0] + radius * math.cos(angle)
        y = CENTER[1] + radius * math.sin(angle)
        color = hsv2rgb(i / count, 0.9, 1)
        draw.ellipse([x - 30, y - 30, x + 30, y + 30], fill=color)

def design_concentric_triangles(draw):
    for i in range(1, 25):
        radius = i * 70
        points = []
        for j in range(3):
            theta = 2 * math.pi * j / 3
            x = CENTER[0] + radius * math.cos(theta)
            y = CENTER[1] + radius * math.sin(theta)
            points.append((x, y))
        color = hsv2rgb(i / 25, 0.7, 0.9)
        draw.polygon(points, outline=color)

def design_diagonal_stripes(draw):
    spacing = 150
    for i in range(-WIDTH, WIDTH * 2, spacing):
        color = hsv2rgb((i % 360) / 360, 0.6, 0.9)
        draw.line([(i, 0), (i - HEIGHT, HEIGHT)], fill=color, width=30)

def design_circular_grid(draw):
    for r in range(200, int(math.hypot(WIDTH, HEIGHT)), 200):
        for angle in range(0, 360, 15):
            theta = math.radians(angle)
            x = CENTER[0] + r * math.cos(theta)
            y = CENTER[1] + r * math.sin(theta)
            draw.ellipse([x - 15, y - 15, x + 15, y + 15], fill=hsv2rgb(angle / 360, 1, 1))

def design_flower_pattern(draw):
    petals = 80
    for i in range(petals):
        theta = 2 * math.pi * i / petals
        r = 600 * math.sin(4 * theta)
        x = CENTER[0] + r * math.cos(theta)
        y = CENTER[1] + r * math.sin(theta)
        color = hsv2rgb(i / petals, 0.8, 1)
        draw.ellipse([x - 20, y - 20, x + 20, y + 20], fill=color)

# List of designs to generate
designs = [
    ("radial_symmetry", design_radial_symmetry),
    ("concentric_triangles", design_concentric_triangles),
    ("diagonal_stripes", design_diagonal_stripes),
    ("circular_grid", design_circular_grid),
    ("flower_pattern", design_flower_pattern),
]

# Generate and save wallpapers
for name, design_func in designs:
    base = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(base)
    design_func(draw)
    apply_radial_gradient(base)
    base = base.filter(ImageFilter.GaussianBlur(radius=1))
    file_path = f"wallpapers/geometric_4k_{name}.jpg"
    base.save(file_path, "JPEG", quality=95)
    print(f"Wallpaper saved: {file_path}")
