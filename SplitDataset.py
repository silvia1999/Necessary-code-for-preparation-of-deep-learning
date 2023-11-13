import os
import random
import numpy as np
import shutil

def split_train_val_test(imgfilepath,lblfilepath,savepath,train_ratio,val_ratio):
    imgfiles = os.listdir(imgfilepath)
    num_img = len(imgfiles)
    lblfiles = os.listdir(lblfilepath)
    num_lbl = len(lblfiles)

    # 验证图片与标注是否数量相同
    if num_img != num_lbl:
        print('txt和image的数量不相等')
        exit(1)

    # 创建与图片数相等的索引list
    file = np.arange(0,num_img)
    filelist = file.tolist()

    # 生成train数据集
    # 随机数挑选出train的下标
    train_index = random.sample(filelist,round(num_img*train_ratio))

    # 创建train文件夹
    os.makedirs(savepath+'/train/images')
    os.makedirs(savepath + '/train/labels')
    for i in range(1,len(train_index)):
        shutil.copy(imgfilepath+imgfiles[train_index[i-1]],savepath+'/train/images')
        shutil.copy(lblfilepath+lblfiles[train_index[i-1]],savepath+'/train/labels')

    # 生成val数据集
    val_test_filelist = []
    for m in filelist:
        if m not in train_index:
            val_test_filelist.append(m)
    # 随机数挑选出val的下标
    val_index = random.sample(val_test_filelist,round(num_img*val_ratio))

    # 创建val文件夹
    os.makedirs(savepath+'/val/images')
    os.makedirs(savepath + '/val/labels')
    for i in range(1, len(val_index)):
        shutil.copy(imgfilepath+imgfiles[val_index[i - 1]], savepath + '/val/images')
        shutil.copy(lblfilepath+lblfiles[val_index[i - 1]], savepath + '/val/labels')

    # 生成test数据集
    test_filelist = []
    for m in val_test_filelist:
        if m not in val_index:
            test_filelist.append(m)

    # 创建test文件夹
    os.makedirs(savepath+'/test/images')
    os.makedirs(savepath + '/test/labels')
    for i in range(1, len(test_filelist)):
        shutil.copy(imgfilepath+imgfiles[test_filelist[i - 1]], savepath + '/test/images')
        shutil.copy(lblfilepath+lblfiles[test_filelist[i - 1]], savepath + '/test/labels')


# 给定参数
img = '.../image/'   # 带分割的图片放置的路径，注意后面一定要带上‘/’!!
lbl = '.../label/'   # 带分割的txt放置的路径，注意后面一定要带上‘/’!!
save = '.../dataSet'     # 分割完后的存储路径，注意后面不需要‘/’
train = 0.7     # 训练集占比
val = 0.2       # 验证集占比
split_train_val_test(img,lbl,save,train,val)