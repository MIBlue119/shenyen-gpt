"""fix the image path.

Rename
 00001_0000_0000.jpg to 0001_0000_0000.jpg
 00012_0007_0007.jpg to 0012_0007_0007.jpg
"""
import os
img_dir = "/Users/weirenlan/Desktop/self_practice/shenyen-gpt/public"

for img in os.listdir(img_dir):
    if img.startswith("0"):
        new_img = img[1:]
        os.rename(os.path.join(img_dir, img), os.path.join(img_dir, new_img))
