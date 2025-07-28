
#this file organizes all the images into Dataset folder %80 / %20

import os
import shutil
import random

# Source folders
source_dirs = ["weed_dataset", "not_weed_dataset"]

# Target base
output_base = "dataset"
splits = ["train", "val"]
split_ratio = 0.8  # 80% train, 20% val

# Prepare folders
for split in splits:
    os.makedirs(os.path.join(output_base, "images", split), exist_ok=True)
    os.makedirs(os.path.join(output_base, "labels", split), exist_ok=True)

# Gather all valid samples
all_pairs = []

for src in source_dirs:
    for file in os.listdir(src):
        if file.endswith(".jpg"):
            base = os.path.splitext(file)[0]
            img_path = os.path.join(src, base + ".jpg")
            txt_path = os.path.join(src, base + ".txt")
            if os.path.exists(txt_path):
                all_pairs.append((img_path, txt_path))
            else:
                print(f"Missing label for {img_path}")

# Shuffle and split
random.shuffle(all_pairs)
split_index = int(len(all_pairs) * split_ratio)
split_data = {
    "train": all_pairs[:split_index],
    "val": all_pairs[split_index:]
}

# Copy files
for split in splits:
    for img_path, txt_path in split_data[split]:
        base = os.path.basename(img_path)
        lable_base = os.path.basename(txt_path)

        shutil.copy(img_path, os.path.join(output_base, "images", split, base))
        shutil.copy(txt_path, os.path.join(output_base, "labels", split, lable_base))

    print(f"This process has been successful! The {split}: {len(split_data[split])} images has been successfully copied.")

print("\nDataset folder is now ready for YOLOv8 training.")
