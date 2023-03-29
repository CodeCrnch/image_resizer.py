from PIL import Image
import os

def resize_images(input_dir, output_dir, size):
    for filename in os.listdir(input_dir):
        try:
            img = Image.open(os.path.join(input_dir, filename))
            img = img.resize(size)
            img.save(os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.png"))

            print(f"{filename} resized and saved as PNG to {output_dir}")

        except Exception as e:
            print(f"Error processing {filename} : {e}")

input_dir = "input_images"
output_dir = "output_images"
size = (224, 224)

resize_images(input_dir, output_dir, size)
