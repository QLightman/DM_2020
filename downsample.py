import os
import cv2
import glob
import tqdm
import shutil
import math

folder = "./data"
blur_folder = "./blur_downsample"
if not os.path.exists(blur_folder):
    os.makedirs(blur_folder)
all_blur = os.path.join(folder, "*_blur.png")
print("downsample single file")
for single_file in tqdm.tqdm(glob.glob(all_blur)):
    original = cv2.imread(single_file)
    w, h, _ = original.shape
    dim = (w//4, h//4)
    resized = cv2.resize(original, dim, interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(blur_folder, single_file.split('/')[-1]), resized)
