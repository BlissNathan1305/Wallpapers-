
from PIL import Image, ImageDraw
import random
import math

# Common settings for mobile wallpapers
WIDTH, HEIGHT = 1080, 1920  # Standard mobile wallpaper size
PIXEL_SIZE = 20  # Size of each "pixel" in the art
OUTPUT_PREFIX = "pixel_wallpaper_"

def create_pixel_art_wallpapers():
    for wallpaper_num in range(1, 11):
        # Create new image
        img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Each wallpaper has a different design
        if wallpaper_num == 1:
            # 1. Classic 8-bit mountains
            draw_pixel_mountains(draw)
        elif wallpaper_num == 2:
            # 2. Space invaders theme
            draw_space_invaders(draw)
        elif wallpaper_num == 3:
            # 3. Pixel heart grid
            draw_pixel_hearts(draw)
        elif wallpaper_num == 4:
            # 4. Retro game landscape
            draw_retro_landscape(draw)
        elif wallpaper_num == 5:
            # 5. Digital rain (Matrix style)
            draw_digital_rain(draw)
        elif wallpaper_num == 6:
            # 6. Pixel sunset
            draw_pixel_sunset(draw)
        elif wallpaper_num == 7:
            # 7. Minecraft-inspired blocks
            draw_minecraft_blocks(draw)
        elif wallpaper_num == 8:
            # 8. Pixel city skyline
            draw_pixel_city(draw)
        elif wallpaper_num == 9:
            # 9. Pixel ocean waves
            draw_pixel_ocean(draw)
        else:
            # 10. Abstract pixel art
            draw_abstract_pixels(draw)
        
        # Save the image
        img.save(f"{OUTPUT_PREFIX}{wallpaper_num}.png")
    
    print("Generated 10 pixel art wallpapers!")

def draw_pixel_mountains(draw):
    colors = [(30, 60, 110), (50, 90, 150), (80, 130, 200), (150, 200, 240)]
    for y in range(0, HEIGHT, PIXEL_SIZE):
        for x in range(0, WIDTH, PIXEL_SIZE):
            height_factor = 1 - (y / HEIGHT)
            noise = math.sin(x * 0.01) * 0.2 + math.cos(y * 0.005) * 0.1
            mountain_level = int(height_factor * 4 + noise * 4) % len(colors)
            draw.rectangle([x, y, x+PIXEL_SIZE, y+PIXEL_SIZE], fill=colors[mountain_level])

def draw_space_invaders(draw):
    bg_color = (0, 0, 50)
    invader_colors = [(150, 255, 150), (255, 150, 150), (150, 150, 255)]
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=bg_color)
    
    for i in range(5):
        for j in range(3):
            x = 200 + i * 150
            y = 300 + j * 250
            color = invader_colors[(i+j) % len(invader_colors)]
            draw_space_invader(draw, x, y, color)

def draw_space_invader(draw, x, y, color):
    pattern = [
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,0,0],
        [0,1,1,0,1,1,1,0,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [0,0,0,1,1,0,1,1,0,0,0]
    ]
    
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            if pattern[row][col]:
                draw.rectangle([
                    x + col*PIXEL_SIZE, 
                    y + row*PIXEL_SIZE, 
                    x + (col+1)*PIXEL_SIZE, 
                    y + (row+1)*PIXEL_SIZE
                ], fill=color)

def draw_pixel_hearts(draw):
    bg_color = (250, 240, 230)
    heart_colors = [(255, 100, 100), (255, 150, 150), (255, 200, 200)]
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=bg_color)
    
    for y in range(0, HEIGHT, PIXEL_SIZE * 5):
        for x in range(0, WIDTH, PIXEL_SIZE * 5):
            color = random.choice(heart_colors)
            draw_pixel_heart(draw, x, y, color)

def draw_pixel_heart(draw, x, y, color):
    pattern = [
        [0,1,1,0,1,1,0],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [0,1,1,1,1,1,0],
        [0,0,1,1,1,0,0],
        [0,0,0,1,0,0,0]
    ]
    
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            if pattern[row][col]:
                draw.rectangle([
                    x + col*PIXEL_SIZE, 
                    y + row*PIXEL_SIZE, 
                    x + (col+1)*PIXEL_SIZE, 
                    y + (row+1)*PIXEL_SIZE
                ], fill=color)

def draw_retro_landscape(draw):
    # Sky gradient
    for y in range(0, HEIGHT//2, PIXEL_SIZE):
        blue = int(50 + 150 * (y / (HEIGHT//2)))
        draw.rectangle([0, y, WIDTH, y+PIXEL_SIZE], fill=(0, 50, blue))
    
    # Ground
    draw.rectangle([0, HEIGHT//2, WIDTH, HEIGHT], fill=(50, 120, 60))
    
    # Sun
    draw.ellipse([WIDTH//2-100, HEIGHT//4-100, WIDTH//2+100, HEIGHT//4+100], fill=(255, 220, 100))
    
    # Trees
    for x in range(100, WIDTH, 200):
        draw.rectangle([x-10, HEIGHT//2-100, x+10, HEIGHT//2], fill=(100, 70, 40))
        draw.polygon([x-50, HEIGHT//2-100, x, HEIGHT//2-250, x+50, HEIGHT//2-100], fill=(0, 100, 0))

def draw_digital_rain(draw):
    chars = ["0", "1"]
    font_size = PIXEL_SIZE
    bg_color = (0, 0, 0)
    text_color = (0, 255, 0)
    
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=bg_color)
    
    for x in range(0, WIDTH, font_size):
        length = random.randint(5, 20)
        speed = random.randint(1, 3)
        for i in range(length):
            y_pos = (HEIGHT + i * font_size - int(time.time() * speed * 10)) % HEIGHT
            char = random.choice(chars)
            brightness = max(50, 255 - (i * 255 // length))
            color = (0, brightness, 0)
            draw.text((x, y_pos), char, fill=color)

def draw_pixel_sunset(draw):
    colors = [
        (255, 100, 100), (255, 150, 100), (255, 200, 100),
        (255, 220, 100), (100, 100, 255), (50, 50, 150)
    ]
    
    for y in range(0, HEIGHT, PIXEL_SIZE):
        color_index = min(len(colors)-1, y // (HEIGHT // len(colors)))
        draw.rectangle([0, y, WIDTH, y+PIXEL_SIZE], fill=colors[color_index])
    
    # Sun
    draw.ellipse([WIDTH//2-150, HEIGHT//3-150, WIDTH//2+150, HEIGHT//3+150], fill=(255, 240, 150))

def draw_minecraft_blocks(draw):
    block_types = [
        {"color": (100, 150, 70), "size": 1},  # Grass
        {"color": (130, 100, 60), "size": 1},  # Dirt
        {"color": (80, 80, 80), "size": 1},   # Stone
        {"color": (100, 100, 255), "size": 2}  # Diamond (larger)
    ]
    
    for y in range(0, HEIGHT, PIXEL_SIZE):
        for x in range(0, WIDTH, PIXEL_SIZE):
            block = random.choice(block_types)
            size = block["size"]
            draw.rectangle([
                x, y,
                x + PIXEL_SIZE*size,
                y + PIXEL_SIZE*size
            ], fill=block["color"])

def draw_pixel_city(draw):
    # Night sky
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(10, 10, 30))
    
    # Stars
    for _ in range(200):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT//2)
        size = random.randint(1, 3)
        draw.ellipse([x, y, x+size, y+size], fill=(255, 255, 255))
    
    # Buildings
    building_colors = [(20, 20, 60), (30, 30, 80), (40, 40, 100)]
    for x in range(0, WIDTH, 100):
        width = random.randint(50, 150)
        height = random.randint(200, 600)
        color = random.choice(building_colors)
        draw.rectangle([x, HEIGHT-height, x+width, HEIGHT], fill=color)
        
        # Windows
        for wy in range(HEIGHT-height+20, HEIGHT-20, 30):
            for wx in range(x+10, x+width-10, 30):
                if random.random() > 0.3:  # 70% chance of a light being on
                    draw.rectangle([wx, wy, wx+15, wy+15], fill=(255, 255, 150))

def draw_pixel_ocean(draw):
    # Water gradient
    for y in range(0, HEIGHT, PIXEL_SIZE):
        blue_green = min(255, 50 + int(200 * (y / HEIGHT)))
        draw.rectangle([0, y, WIDTH, y+PIXEL_SIZE], fill=(0, blue_green//2, blue_green))
    
    # Waves
    for x in range(0, WIDTH, 40):
        wave_height = random.randint(5, 15)
        draw.arc([
            x, HEIGHT//2-wave_height,
            x+80, HEIGHT//2+wave_height
        ], 180, 360, fill=(0, 100, 200), width=3)
    
    # Fish
    for _ in range(10):
        x = random.randint(0, WIDTH)
        y = random.randint(HEIGHT//2, HEIGHT-100)
        size = random.randint(20, 40)
        color = (random.randint(150, 255), random.randint(50, 150), 50)
        draw.ellipse([x, y, x+size, y+size//2], fill=color)
        draw.polygon([x+size, y+size//4, x+size+size//2, y, x+size+size//2, y+size//2], fill=color)

def draw_abstract_pixels(draw):
    for y in range(0, HEIGHT, PIXEL_SIZE):
        for x in range(0, WIDTH, PIXEL_SIZE):
            if random.random() > 0.7:  # 30% chance of a colored pixel
                hue = random.random()
                saturation = 0.7 + random.random() * 0.3
                value = 0.8 + random.random() * 0.2
                r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, value)]
                draw.rectangle([x, y, x+PIXEL_SIZE, y+PIXEL_SIZE], fill=(r, g, b))

if __name__ == "__main__":
    import time
    create_pixel_art_wallpapers()
