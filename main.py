import sys
import cv2 as cv
import numpy as py

# PHASE 1 Test: 7 videos

# PHASE 2 Test: 40 Videos

# process all 30 frame videos in 10 seconds


def main():

    # Debug: Check image path was passed
    try:
        print(f'Image path passed: {sys.argv[1]}')
    except IndexError:
        sys.exit('ERROR: No Argument for image path')

    # Read image and Check image was read
    orgImg = cv.imread(sys.argv[1], cv.IMREAD_COLOR_BGR)

    if orgImg is None:
        sys.exit('ERROR: Could not read image')

    return 0