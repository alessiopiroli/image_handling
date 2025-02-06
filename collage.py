from PIL import Image
import os

# List of image file paths
image_paths = ['/Volumes/SANDISK/work_UniSi/renamed_photos_collage/one_level/Image_8.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/one_level/Image_2.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/one_level/Image_10.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/one_level/Image_6.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/one_level/Image_5.JPG',
               '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/two_levels/Image_18.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/two_levels/Image_16.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/two_levels/Image_13.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/two_levels/Image_14.JPG', '/Volumes/SANDISK/work_UniSi/renamed_photos_collage/two_levels/Image_12.JPG']

# Open all the images
images = [Image.open(image).convert("RGBA") for image in image_paths]  # Convert images to RGBA mode for transparency

# Get the size of the images (assuming all images have the same size)
image_width, image_height = images[0].size

# Calculate the size of the collage
collage_width = image_width * 5  # 5 images per row
collage_height = image_height * 2  # 2 rows

# Create a blank canvas with a transparent background (RGBA mode)
collage = Image.new('RGBA', (collage_width, collage_height), (0, 0, 0, 0))  # (0,0,0,0) for transparency

# Paste images onto the collage
for i, image in enumerate(images):
    row = i // 5  # Determine the row (0 or 1)
    col = i % 5   # Determine the column (0 to 4)
    x_offset = col * image_width
    y_offset = row * image_height
    collage.paste(image, (x_offset, y_offset), image)  # Use the image itself as a mask to preserve transparency

# Define the folder and filename
save_folder = "/Volumes/SANDISK/work_UniSi/grasping_collage"  # Change to your desired folder
save_filename = "collage_2.png"  # Change the filename as needed
save_path = os.path.join(save_folder, save_filename)

# Ensure the folder exists
os.makedirs(save_folder, exist_ok=True)

# Save the collage as PNG (keeping transparency)
collage.save(save_path)
print(f"Collage saved at: {save_path}")
collage.show()
