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


dir_out = "./text_dataset_DM"
if not os.path.exists(dir_out):
    os.makedirs(dir_out)
clear_img = os.path.join(folder, "*_orig.png")
blur_img = os.path.join(blur_folder, "*_blur.png")

A_clear_folder = os.path.join(dir_out, "clear_A")
A_blur_folder = os.path.join(dir_out, "blur_downsample_A")

B_clear_folder = os.path.join(dir_out, "clear_B")
B_blur_folder = os.path.join(dir_out, "blur_downsample_B")

test_clear_folder = os.path.join(dir_out, "clear_test")
test_blur_folder = os.path.join(dir_out, "blur_downsample_test")

if not os.path.exists(A_clear_folder):
    os.makedirs(A_clear_folder)
if not os.path.exists(A_blur_folder):
    os.makedirs(A_blur_folder)
if not os.path.exists(B_clear_folder): os.makedirs(B_clear_folder)
if not os.path.exists(B_blur_folder): os.makedirs(B_blur_folder)
if not os.path.exists(test_clear_folder): os.makedirs(test_clear_folder)
if not os.path.exists(test_blur_folder): os.makedirs(test_blur_folder)


# # retrieve file list
print("sorting file name..")
clear_filelist = sorted(glob.glob(clear_img))
blur_filelist = sorted(glob.glob(blur_img))
print("start organizing file..")
total_clear = len(clear_filelist)
total_blur = len(blur_filelist)
num_train_clear, num_train_blur = math.floor(total_clear*0.4), math.floor(total_blur*0.4)
for i, single_file in enumerate(tqdm.tqdm(clear_filelist)):
    if i < num_train_clear:
     # move file with full paths as shutil.move() parameters
        #dst_path = os.path.join(clear_folder, "")
        shutil.move(single_file, A_clear_folder)
    elif num_train_clear <= i < 2 * num_train_clear:
        shutil.move(single_file, B_clear_folder)
    else:
        shutil.move(single_file, test_clear_folder)

for i, single_file in enumerate(tqdm.tqdm(blur_filelist)):
    if i < num_train_blur:
     # move file with full paths as shutil.move() parameters
        shutil.copy(single_file, A_blur_folder)
    elif num_train_blur <= i < 2 * num_train_blur:
        shutil.copy(single_file, B_blur_folder)
    else:
        shutil.copy(single_file, test_blur_folder)

print("finished!")