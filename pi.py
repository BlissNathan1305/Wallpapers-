
from PIL import Image, ImageDraw

# Define the size of the pixel art and the wallpaper
pixel_size = 10  # Each pixel in the pattern will be 10x10 pixels
pattern_size = (10, 10)  # 10x10 pixel pattern
wallpaper_size = (1080, 1920)  # Typical mobile wallpaper size

# Create a new image for the pattern
pattern = Image.new('RGB', (pattern_size[0] * pixel_size, pattern_size[1] * pixel_size), color='white')
draw = ImageDraw.Draw(pattern)

# Define colors for the pixel art
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

# Create a simple pattern
for y in range(pattern_size[1]):
    for x in range(pattern_size[0]):
        color = colors[(x + y) % len(colors)]  # Simple color cycling
        draw.rectangle([x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size], fill=color)

# Create a new image for the wallpaper
wallpaper = Image.new('RGB', wallpaper_size, color='black')

# Calculate how many times the pattern needs to be repeated
repeat_x = wallpaper_size[0] // pattern.size[0]
repeat_y = wallpaper_size[1] // pattern.size[1]

# Tile the pattern to fill the wallpaper
for y in range(repeat_y):
    for x in range(repeat_x):
        wallpaper.paste(pattern, (x * pattern.size[0], y * pattern.size[1]))

# Save the wallpaper
wallpaper.save('pixel_art_wallpaper.png')
