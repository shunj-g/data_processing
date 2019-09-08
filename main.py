#!/usr/bin/env python
# encoding: utf-8
'''
@author: shunj-g
@license: (C) Copyright 2018-2035, Digital Imaging and Intelligent Computing Laboratory(DIIC LAB).SHMTU
@contact: shunjieg@gmail.com
@software: main
@file: main.py
@time: 2019/9/8 19:27
@desc:  

'''
import SimpleITK as sitk
import nibabel as nib
import numpy as np
from utils import resize
from sitk_utils import resample_to_spacing


def images_align():
    image = nib.load('20121114_075953s982300a000.nii.gz')
    affine = image.affine
    data = np.array(image.dataobj[:,:,:,2])
    image_nib = nib.Nifti1Image(data, affine=affine)
    new_image_nib = resize(image_nib, (96, 96, 106), interpolation="nearest")
    nib.save(new_image_nib,'test.nii')
    print(new_image_nib)

if __name__ == '__main__':
    images_align()