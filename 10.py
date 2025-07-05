
from PIL import Image, ImageDraw
import random

# Define the size of the pixel art and the wallpaper
pixel_size = 10  # Each pixel in the pattern will be 10x10 pixels
pattern_size = (10, 10)  # 10x10 pixel pattern
wallpaper_size = (1080, 1920)  # Typical mobile wallpaper size

# Define a list of colors
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255),  # White
    (0, 0, 0)  # Black
]

def create_pattern(colors, pattern_size, pixel_size):
    pattern = Image.new('RGB', (pattern_size[0] * pixel_size, pattern_size[1] * pixel_size), color='white')
    draw = ImageDraw.Draw(pattern)
    
    for y in range(pattern_size[1]):
        for x in range(pattern_size[0]):
            color = random.choice(colors)  # Randomly select a color
            draw.rectangle([x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size], fill=color)
    
    return pattern

def create_wallpaper(pattern, wallpaper_size):
    wallpaper = Image.new('RGB', wallpaper_size, color='black')
    
    repeat_x = wallpaper_size[0] // pattern.size[0]
    repeat_y = wallpaper_size[1] // pattern.size[1]
    
    for y in range(repeat_y):
        for x in range(repeat_x):
            wallpaper.paste(pattern, (x * pattern.size[0], y * pattern.size[1]))
    
    return wallpaper

# Create 10 unique wallpapers
for i in range(10):
    pattern = create_pattern(colors, pattern_size, pixel_size)
    wallpaper = create_wallpaper(pattern, wallpaper_size)
    wallpaper.save(f'pixel_art_wallpaper_{i+1}.png')
    print(f'Wallpaper {i+1} created.')
