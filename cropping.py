from PIL import Image
import os

# Define input and output directories
input_folder = "/Volumes/SANDISK/work_UniSi/Grasping_photos_for_collage"
output_folder = "/Volumes/SANDISK/work_UniSi/cropped_photos_collage"
os.makedirs(output_folder, exist_ok=True)

# Define how much to remove from each side (left, top, right, bottom)
CROP_MARGIN = (2200, 200, 2300, 450)  # Adjust these values as needed

# Process each image
for filename in os.listdir(input_folder):
    if filename.startswith("."):  # Ignore hidden files
        continue

    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        
        try:
            img = Image.open(img_path)
        except Exception as e:
            print(f"Skipping {filename}: {e}")
            continue

        img_width, img_height = img.size
        left_crop, top_crop, right_crop, bottom_crop = CROP_MARGIN

        # Compute the new crop box dynamically
        left = left_crop
        top = top_crop
        right = img_width - right_crop
        bottom = img_height - bottom_crop

        # Ensure the crop box is valid
        if left >= right or top >= bottom:
            print(f"Skipping {filename}: Invalid crop dimensions ({left}, {top}, {right}, {bottom})")
            continue

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img = cropped_img.convert("RGB")  # Ensure compatibility with JPEG

        output_path = os.path.join(output_folder, filename)
        cropped_img.save(output_path)
        print(f"Cropped and saved: {filename} (New size: {cropped_img.size})")

print("Batch cropping completed!")