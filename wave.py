
from PIL import Image, ImageDraw
import math
import colorsys
import os

# Create output directory
os.makedirs("wallpapers", exist_ok=True)

# 4K mobile wallpaper dimensions
WIDTH, HEIGHT = 2160, 3840

def hsv2rgb(h, s, v):
    """Convert HSV to RGB (0-255)"""
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def draw_wave_pattern(draw, amplitude, frequency, color_shift):
    """Draw sinusoidal wave pattern line-by-line"""
    for y in range(0, HEIGHT, 10):
        points = []
        for x in range(0, WIDTH, 5):
            offset = amplitude * math.sin((x / WIDTH) * frequency * 2 * math.pi + y / 100)
            points.append((x, y + offset))
        hue = ((y / HEIGHT) + color_shift) % 1.0
        color = hsv2rgb(hue, 0.8, 1)
        draw.line(points, fill=color, width=3)

def generate_wave_wallpaper(name_suffix, amplitude=50, frequency=4, color_shift=0.0):
    """Generate and save a 4K wave wallpaper"""
    image = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(image)
    draw_wave_pattern(draw, amplitude, frequency, color_shift)
    file_path = f"wallpapers/geometric_4k_wave_{name_suffix}.jpg"
    image.save(file_path, "JPEG", quality=95)
    print(f"Saved: {file_path}")

# Generate multiple wave designs with different properties
generate_wave_wallpaper("classic")  # balanced
generate_wave_wallpaper("amplitude_high", amplitude=100)
generate_wave_wallpaper("frequency_high", frequency=10)
generate_wave_wallpaper("color_shifted", color_shift=0.5)
generate_wave_wallpaper("dense", amplitude=30, frequency=15, color_shift=0.25)
