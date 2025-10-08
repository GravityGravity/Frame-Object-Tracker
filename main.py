# Project 2: Video-Object-Tracker

import sys
import cv2 as cv
import numpy as py

# PHASE 1 Test: 7 videos

# PHASE 2 Test: 40 Videos

# process all 30 frame videos in 10 seconds

# Example Input: $ python project2.py /path/to/video/


def main():

    # Debug: Check image path was passed
    try:
        print(f'Image path passed: {sys.argv[1]}')
        videoPath = sys.argv[1]

        # Parse frame0 given object coordinates from txt file
        with open(videoPath + '\\rect.txt', "r", encoding='utf-8') as file:
            initRect = file.read()
            initRect = initRect.split()
            initRect = list(map(int, initRect))

            Xpos, Ypos, Width, Height = initRect

    except IndexError:
        sys.exit('ERROR: Invalid Argument for image path')

    # DEBUG:  Print videoPath and Initial Rectangle parsed data
    print(f'videoPath: {videoPath}')
    print(f'initial rectangle: {initRect}')

    # Read image and Check image was read
    for i in range(29):
        # DEBUG: Print current frame and next frame video path
        curPathItr = videoPath + f'\\frame{i}.png'
        nxtPathItr = videoPath + f'\\frame{i+1}.png'

        # DEBUG: Print i itr for loop
        print(f'({i})   curPath: {curPathItr}')

        # Current image that was processed
        curImg = cv.imread(curPathItr, cv.IMREAD_GRAYSCALE)
        # Next image being processed and compared to first
        nxtImg = cv.imread(nxtPathItr, cv.IMREAD_GRAYSCALE)

        curImgClr = cv.imread(curPathItr, cv.IMREAD_COLOR_BGR)
        nxtImgClr = cv.imread(nxtPathItr, cv.IMREAD_COLOR_BGR)

        if curImg is None or nxtImg is None:
            sys.exit('ERROR: Could not read image or video read ended')

        # Create list of edges used in optical flow for object tracking
        features = cv.goodFeaturesToTrack(curImg, 50, 0.01, 20)

        # Convert FP to int for int operations
        features = features.astype(int)

        print(features)

        # DEBUG: Print what corners are detected from cv.goodfeaturestotrack()
        for corner in features:
            print(corner[0, :])
            cv.circle(curImgClr, (corner[0, :]), 10, (0, 255, 0), 1, cv.FILLED)
        # cv.calcOpticalFlowPyrLK(curImg, nxtImg, )

        cv.rectangle(curImgClr, (Xpos, Ypos),
                     ((Xpos + Width), (Ypos + Height)), (255, 0, 0), 3)

        # Print Rectangle Object Highlight Coordinates
        print(f'{Xpos} {Ypos} {Width} {Height}')

        # DEBUG: Display Frame Data like [Corners, Object Box]
        cv.imshow(f'frame{i}', curImgClr)

        # DEBUG: Press Q/q to close all windows and exit loop
        #        Press any other key to display next frame
        quitKey = cv.waitKey(0) & 0xFF
        if quitKey == ord('q') or quitKey == ord('Q'):
            cv.destroyAllWindows()
            break

    # DEBUG: Formatting
    print()

    return 0


main()
