from PIL import Image
import os

image_paths = []
images = [Image.open(image).convert("RGBA") for image in image_paths]  # Convert images to RGBA mode for transparency
image_width, image_height = images[0].size

collage_width = image_width * 5
collage_height = image_height * 2

collage = Image.new('RGBA', (collage_width, collage_height), (0, 0, 0, 0))

for i, image in enumerate(images):
    row = i // 5
    col = i % 5
    x_offset = col * image_width
    y_offset = row * image_height
    collage.paste(image, (x_offset, y_offset), image)

save_folder = "folder"
save_filename = "collage.extension"
save_path = os.path.join(save_folder, save_filename)

os.makedirs(save_folder, exist_ok=True)

collage.save(save_path)
print(f"Collage saved at: {save_path}")
collage.show()
