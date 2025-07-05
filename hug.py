
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO
import datetime
import os

# Use a high-quality model
client = InferenceClient(model="stabilityai/sdxl-turbo")  # You can try other models too

def generate_wallpaper(prompt, output_dir="wallpapers", width=1024, height=1024):
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating: {prompt}")
    
    # Generate image using Hugging Face hosted model
    response = client.text_to_image(
        prompt,
        width=width,
        height=height,
        guidance_scale=7.5,  # Optional: controls image creativity/detail
        num_inference_steps=25  # More steps = better quality, slower
    )

    # Save as JPEG
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{output_dir}/wallpaper_{timestamp}.jpeg"

    # Convert to RGB (in case image is in RGBA)
    image = response.convert("RGB")
    image.save(file_path, "JPEG", quality=95)

    print(f"Saved as {file_path}")

# Example prompt
generate_wallpaper("A fantasy forest with glowing mushrooms and waterfalls, ultra detailed, 4k")
