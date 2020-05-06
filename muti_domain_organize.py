import os
import cv2
import glob
import tqdm
import shutil
import math

sharp_folder="./LR"
blur_folder="./LR_Blur"
trainA_folder="./trainA"
trainB_folder="./trainB"
test_folder="./testA"
group_truth_folder="./group_truth"

if not os.path.exists(test_folder):
    os.makedirs(test_folder)
if not os.path.exists(trainA_folder):
    os.makedirs(trainA_folder)
if not os.path.exists(trainB_folder):
    os.makedirs(trainB_folder)
if not os.path.exists(group_truth_folder):
    os.makedirs(group_truth_folder)



clear_img = os.path.join(sharp_folder, "*.png")
blur_img = os.path.join(blur_folder, "*.png")

clear_filelist = sorted(glob.glob(clear_img))
blur_filelist = sorted(glob.glob(blur_img))

num_train_clear=90

for i, single_file in enumerate(tqdm.tqdm(clear_filelist)):
    if i < num_train_clear:
     # move file with full paths as shutil.move() parameters
        #dst_path = os.path.join(clear_folder, "")
        shutil.move(single_file, group_truth_folder)
    else:
        shutil.move(single_file, trainA_folder)


for i, single_file in enumerate(tqdm.tqdm(blur_filelist)):
    if i < num_train_clear:
     # move file with full paths as shutil.move() parameters
        #dst_path = os.path.join(clear_folder, "")
        shutil.move(single_file, test_folder)
    else:
        shutil.move(single_file, trainB_folder)

os.rmdir(sharp_folder)
os.rmdir(blur_folder)

print("finished!")