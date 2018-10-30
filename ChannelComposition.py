# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:51:38 2018
@ author: alex choi
@ purpose: composition of multi-channels from different lighting angles
@ note: input image filename convention:
       any image file format would be ok, but filename should be as following
       1-1.bmp, 1-2.bmp, 1-3.bmp, 1-4.bmp
       2-1.bmp, 2-2.bmp, 2-3.bmp, 2-4.bmp
       3-1.bmp, 3-2.bmp, 3-3.bmp, 3-4.bmp
       ...
       maximum 4 channels allowed
"""
 
#########################################################################################
#      USER DEFINITION
#########################################################################################
## define input & output path
# @input path : where your input channel images
# @output path : where to put your composition images
NUM_LIGHT_DIRECTION = 4  # number of lighting directions
INPUT_IMAGE_PATH = './SourceImages'
OUTPUT_IMAGE_PATH = './ResultImages'
OUTPUT_IMAGE_NAME = 'ChannelMixed'
OUTPUT_IMAGE_FORMAT = 'bmp'
LIGHT_SELECTION = [3,4,1]
#########################################################################################
 
## import libraries
import os, errno
import sys
from os import walk
import numpy as np
import cv2
 
###############################################################################
# @function : main
###############################################################################
def main():
    if(len(LIGHT_SELECTION) > 4):
        sys.exit()
    
    ## create output path if not exist
    try:
        os.makedirs(OUTPUT_IMAGE_PATH)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
    ## file list from input path
    flist = []
    for (dirpath, dirnames, filenames) in walk(INPUT_IMAGE_PATH):
        flist.extend(filenames)
        break
    
    ## initialize image mat
    tmp = cv2.imread(os.path.join(INPUT_IMAGE_PATH, flist[0]))
    img = np.zeros(shape=[tmp.shape[0], tmp.shape[1], len(LIGHT_SELECTION)], dtype=int)
    
    ## generate channel mixed images    
    for filename in flist:
        tmp = filename.split("-")
        fileIdx = tmp[0]
                
        chNo = tmp[1].split(".%s" % (OUTPUT_IMAGE_FORMAT))[0]
        
        fileIdx = int(fileIdx)
        chNo = int(chNo)
        
        if(chNo in LIGHT_SELECTION):
            idx = LIGHT_SELECTION.index(chNo)
            tmp = cv2.imread(os.path.join(INPUT_IMAGE_PATH, filename))
            tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
            img[:,:,idx] = tmp
            
            
        if(chNo == NUM_LIGHT_DIRECTION):
            fname = os.path.join(OUTPUT_IMAGE_PATH, "%s-%03d.png" % (OUTPUT_IMAGE_NAME, fileIdx))
            cv2.imwrite(fname, img)
            print("Saved : %s" % (fname))


if __name__ == "__main__":
    main()