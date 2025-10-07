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

        with open(videoPath + '\\rect.txt', "r", encoding='utf-8') as file:
            initRect = file.read()
            initRect = initRect.split()
            initRect = list(map(int, initRect))

            Xpos, Ypos, Width, Height = initRect

    except IndexError:
        sys.exit('ERROR: No Argument for image path')

    # DEBUG:  Print videoPath and Initial Rectangle
    print(f'videoPath: {videoPath}')
    print(f'initial rectangle: {initRect}')

    quitKey = cv.waitKey(1) & 0xFF

    # Read image and Check image was read
    for i in range(29):
        curPathItr = videoPath + f'\\frame{i}.png'
        nxtPathItr = videoPath + f'\\frame{i+1}.png'

        # DEBUG: Print i itr for loop
        print(f'({i})   curPath: {curPathItr}')

        if quitKey == ord('q'):
            break

        # Current image that was processed
        curImg = cv.imread(curPathItr, cv.IMREAD_COLOR_BGR)
        # Next image being processed and compared to first
        nxtImg = cv.imread(nxtPathItr, cv.IMREAD_COLOR_BGR)

        if curImg is None or nxtImg is None:
            sys.exit('ERROR: Could not read image or video read ended')

        cv.rectangle(curImg, (Xpos, Ypos),
                     ((Xpos + Width), (Ypos + Height)), (255, 0, 0), 3)

        print(f'{Xpos} {Ypos} {Width} {Height}')

        cv.imshow(f'frame{i}', curImg)

        quitKey = cv.waitKey(0) & 0xFF
        if quitKey == ord('q') or quitKey == ord('Q'):
            break

    print()

    return 0


main()
