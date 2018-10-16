# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:15:32 2018

@author: achoi
"""

SOURCE_PATH = './SourceImages/'
TARGET_PATH = './ResultImages/'

## import libraries
import os
from os import walk
import cv2
import numpy as np

## file list from input path
flist = []
for (dirpath, dirnames, filenames) in walk(SOURCE_PATH):
    flist.extend(filenames)
    break

# process file by file
cnt = 0
for filename in flist:
    channel = cnt % 4
    
    source = os.path.join(SOURCE_PATH, filename)
    srcImage = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
    
    if channel == 0:
        resultImage = np.zeros((srcImage.shape[0], srcImage.shape[1], 4), dtype='uint8')
    
    resultImage[:,:,channel] = srcImage
    
    if channel == 3:
        target = os.path.join(TARGET_PATH, filename.split('-')[0] + '.png')
        cv2.imwrite(target, resultImage)
    
    cnt += 1