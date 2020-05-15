# Final Report for CS 391D: Data Mining from a Mathematical Perspective

## Dataset

To train the model, unpaired sharp and blurred images folders should be named in the following format: `datasets/name/trainA` and `datasets/name/trainB`. Test images can be stored in the same folder and you may choose your own folder name.

## Usage

### Data Preperation

In our experiment, cross domain data is from [GoPro](https://drive.google.com/file/d/1H0PIXvJH4c40pk7ou6nAwoxuR4Qh_Sa2/view?usp=sharing) and text data is from [BMVC text dataset](http://www.fit.vutbr.cz/~ihradis/CNN-Deblur/).

### Train

To train the model, run the following command line in the source code directory. You may set other parameters based on your experiment setting.

```bash
python train.py --dataroot ../datasets/ --name job_name --batch_size 2 --lambdaB 0.1 --lr 0.0002
```

### Test

To test the model, run the following command line in the source code directory. You may set other parameters based on your experiment setting.

```bash
python test.py --dataroot ../datasets/testA/ --num 1 --resume ../results/00099.pth --name outputA --orig_dir ../datasets/group_truth/ --result_dir ../results/
```

## Acknowledgments

The code borrows heavily from [DRIT](https://github.com/HsinYingLee/DRIT). We use the image blurring method in [DeblurGAN](https://github.com/KupynOrest/DeblurGAN/tree/master/motion_blur).
