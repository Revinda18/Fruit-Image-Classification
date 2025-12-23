import os
import shutil
import random

SOURCE_DIR = "dataset"
BASE_DIR = "dataset_split"

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

classes = os.listdir(SOURCE_DIR)

for cls in classes:
    cls_path = os.path.join(SOURCE_DIR, cls)
    images = os.listdir(cls_path)
    random.shuffle(images)

    train_end = int(len(images) * TRAIN_RATIO)
    val_end = train_end + int(len(images) * VAL_RATIO)

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split, imgs in splits.items():
        split_dir = os.path.join(BASE_DIR, split, cls)
        os.makedirs(split_dir, exist_ok=True)

        for img in imgs:
            src = os.path.join(cls_path, img)
            dst = os.path.join(split_dir, img)
            shutil.copyfile(src, dst)

print("Dataset berhasil di-split!")