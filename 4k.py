
from PIL import Image, ImageDraw, ImageFilter
import math
import random
import colorsys
import os

# Create output directory
os.makedirs("wallpapers", exist_ok=True)

# Dimensions for 4K vertical mobile wallpaper
WIDTH, HEIGHT = 2160, 3840
CENTER = (WIDTH // 2, HEIGHT // 2)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def draw_symmetric_shapes(draw, count=72, radius=1400):
    angle_step = 360 / count
    for i in range(count):
        angle = math.radians(i * angle_step)
        x = CENTER[0] + radius * math.cos(angle)
        y = CENTER[1] + radius * math.sin(angle)
        color = hsv2rgb(i / count, 0.8, 1)
        draw.ellipse([x - 40, y - 40, x + 40, y + 40], fill=color, outline=None)

def draw_concentric_polygons(draw, levels=20):
    for i in range(1, levels + 1):
        sides = random.choice([3, 4, 6, 8])
        radius = i * 70
        angle_offset = random.uniform(0, math.pi * 2)
        points = []
        for j in range(sides):
            theta = angle_offset + 2 * math.pi * j / sides
            x = CENTER[0] + radius * math.cos(theta)
            y = CENTER[1] + radius * math.sin(theta)
            points.append((x, y))
        color = hsv2rgb(i / levels, 0.7, 0.9)
        draw.polygon(points, outline=color, fill=None)

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

def generate_geometric_wallpaper():
    base = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(base)

    draw_symmetric_shapes(draw)
    draw_concentric_polygons(draw)

    apply_radial_gradient(base)

    base = base.filter(ImageFilter.GaussianBlur(radius=1))
    file_path = f"wallpapers/geometric_4k_wallpaper_{random.randint(1000,9999)}.jpg"
    base.save(file_path, "JPEG", quality=95)
    print(f"Wallpaper saved at: {file_path}")

# Run the generator
generate_geometric_wallpaper()
