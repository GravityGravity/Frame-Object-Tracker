# Project 2: Video-Object-Tracker

import sys
import cv2 as cv
import numpy as py

# PHASE 1 Test: 7 videos

# PHASE 2 Test: 40 Videos

# process all 30 frame videos in 10 seconds

#Example Input: $ python project2.py /path/to/video/

def main():

    # Debug: Check image path was passed
    try:
        print(f'Image path passed: {sys.argv[1]}')
        videoPath = sys.argv[1]
    except IndexError:
        sys.exit('ERROR: No Argument for image path')

    # Read image and Check image was read
    for i in range(29):
        curImg = cv.imread(videoPath, cv.IMREAD_GRAYSCALE) #Current image that was processed
        nxtImg = cv.imread(videoPath, cv.IMREAD_GRAYSCALE) #Next image being processed and compared to first

    if curImg or nxtImg is None:
        sys.exit('ERROR: Could not read image or video read ended')

    return 0