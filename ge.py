
from PIL import Image, ImageDraw
import math
import random
import colorsys

# Wallpaper dimensions
WIDTH, HEIGHT = 3840, 2160  # 4K resolution
BACKGROUND = (15, 15, 25)    # Dark blue-black

# Create new image
img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
draw = ImageDraw.Draw(img)

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def draw_geometric_pattern():
    # Parameters
    cell_size = 120
    rows = HEIGHT // cell_size + 2
    cols = WIDTH // cell_size + 2
    max_radius = cell_size * 0.8
    
    for row in range(rows):
        for col in range(cols):
            # Calculate center position with offset for even rows
            offset = cell_size / 2 if row % 2 == 0 else 0
            x = col * cell_size + offset
            y = row * cell_size * 0.866  # Hexagonal spacing
            
            # Generate color based on position
            hue = (x / WIDTH + y / HEIGHT * 0.5) % 1.0
            saturation = 0.7 + 0.3 * math.sin(x * 0.01)
            value = 0.8 + 0.2 * math.cos(y * 0.005)
            color = hsv_to_rgb(hue, saturation, value)
            
            # Draw hexagon
            sides = 6
            radius = max_radius * 0.9
            points = []
            for i in range(sides):
                angle = math.pi * 2 * i / sides + math.pi / 6
                px = x + radius * math.cos(angle)
                py = y + radius * math.sin(angle)
                points.append((px, py))
            
            draw.polygon(points, fill=color, outline=(30, 30, 40))
            
            # Draw inner circles
            for i in range(3, 0, -1):
                inner_radius = radius * i * 0.25
                inner_color = hsv_to_rgb(
                    (hue + 0.1 * i) % 1.0,
                    max(0.3, saturation - 0.1 * i),
                    min(1.0, value + 0.1 * i)
                )
                draw.ellipse(
                    (x - inner_radius, y - inner_radius, 
                     x + inner_radius, y + inner_radius),
                    fill=inner_color
                )

def add_glow_effects():
    # Create a glow effect by drawing semi-transparent circles
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(100, 500)
        hue = random.random()
        color = hsv_to_rgb(hue, 0.5, 0.9)
        
        # Create a temporary image for the glow
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        
        for i in range(10, 0, -1):
            alpha = 5 * i
            r = radius * i / 10
            glow_draw.ellipse(
                (x - r, y - r, x + r, y + r),
                fill=(color[0], color[1], color[2], alpha)
            )
        
        # Composite the glow onto the main image
        img.paste(Image.alpha_composite(img.convert('RGBA'), glow), (0, 0))

# Generate the wallpaper
draw_geometric_pattern()
add_glow_effects()

# Save the image
img.save('geometric_wallpaper.png')
print("Wallpaper generated successfully!")
