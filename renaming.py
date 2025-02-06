import os
import shutil

# Define input and output folders
image_folder = "/Volumes/SANDISK/work_UniSi/cropped_photos_collage"
output_folder = "/Volumes/SANDISK/work_UniSi/renamed_photos"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all image files in the folder (filter by extensions, ignore hidden files)
image_files = sorted([
    f for f in os.listdir(image_folder) 
    if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.startswith(".")
])

# Rename and copy files to output folder
for index, filename in enumerate(image_files, start=1):
    old_path = os.path.join(image_folder, filename)
    file_ext = os.path.splitext(filename)[1]  # Keep original extension

    new_filename = f"Image_{index}{file_ext}"  # Format: Image_1.jpg
    new_path = os.path.join(output_folder, new_filename)

    shutil.copy2(old_path, new_path)  # Copy file instead of renaming in place
    print(f"Copied and renamed: {filename} → {new_filename}")

print("Batch renaming completed!")
