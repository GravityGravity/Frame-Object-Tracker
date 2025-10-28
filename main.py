# FILE: Main.py - Script for Frame-Object-Tracker
#
# Description:
"""
This script runs the object tracking process on a 30-frame video sequence.
It loads frames from the given input path, tracks the target object across
all frames, and produces the output with the object bounding box

Example:
    Input folder: C:\_repos\CompVision\Frame-Object-Tracker\tests\4
    Run command:  python main.py C:\_repos\CompVision\Frame-Object-Tracker\tests\4
"""
import sys
import cv2 as cv
import numpy as py


def main():

    # DEBUG: Check image path was passed
    try:
        print(f'Image path passed: {sys.argv[1]}')
        videoPath = sys.argv[1]

    except FileNotFoundError:
        sys.exit('ERROR: Invalid Argument for image path')

    # DEBUG: Check if initial object coordinates txt file was passed
    try:

        # Parse frame0 given object coordinates from txt file
        with open(videoPath + '\\rect.txt', "r", encoding='utf-8') as file:
            initRect = file.read()
            initRect = initRect.split()
            initRect = list(map(int, initRect))

            Xpos, Ypos, Width, Height = initRect

    except FileNotFoundError as e:
        sys.exit(
            'ERROR: No initial object highlight coordinates .txt file in video directory')

    # DEBUG:  Print videoPath and Initial Rectangle parsed data
    print(f'videoPath: {videoPath}')
    print(f'initial rectangle: {initRect}\n')

    # Coordinates to create template image using initial rectangle
    y_end = Ypos + Height
    x_end = Xpos + Width
    y_start = Ypos
    x_start = Xpos

    # LOOP: Using image processing process Current Frame + Next Frame -> Output Object Highlightf for 30 frames
    for i in range(29):

        # DEBUG: Iterators for current frame and next frame video path
        curPathItr = videoPath + f'\\frame{i}.png'
        nxtPathItr = videoPath + f'\\frame{i+1}.png'

        # DEBUG: Print i itr for loop
        print(f'({i})   curPath: {curPathItr}')

        # Read current frame & next frame (using grayscale)
        curImg = cv.imread(curPathItr, cv.IMREAD_GRAYSCALE)
        nxtImg = cv.imread(nxtPathItr, cv.IMREAD_GRAYSCALE)

        # Colored Frames
        curImgClr = cv.imread(curPathItr, cv.IMREAD_COLOR_BGR)
        nxtImgClr = cv.imread(nxtPathItr, cv.IMREAD_COLOR_BGR)

        if curImg is None or nxtImg is None:
            sys.exit('ERROR: Could not read image or video read ended')

        # Create a template based on current frame for the next frame
        templateImg = curImg[y_start:y_end, x_start:x_end]
        cv.imshow(f'Template image{i}', templateImg)

        # Analyze Next Frame with Current Frame Object Template
        matchloc = cv.matchTemplate(nxtImg, templateImg, cv.TM_CCOEFF_NORMED)
        print('Location Match for Template')

        # Find pixel location of image value has max matching value
        minval, maxval, minloc, maxloc = cv.minMaxLoc(matchloc)

        # Y and X deltas + start points to create Top-Left and Bottom Right rectangle points
        # Coordinates of Top left point
        topleft = maxloc
        y_start = topleft[1]
        y_end = topleft[1] + Height  # BR Y-axis

        x_start = topleft[0]
        x_end = topleft[0] + Width  # BR X-axis

        # Coordinates form of Bottom Right Point
        bottomright = (topleft[0] + Width, topleft[1] + Height)

        # Debugging min,max locations/values
        print(
            f'minval:{minval}, maxval:{maxval}, minloc:{minloc}, maxloc:{maxloc}')

        # Draw rectangle of predicted object location
        cv.rectangle(nxtImgClr, topleft,
                     bottomright, (255, 0, 0), 3)

        # Print Rectangle Object Highlight Coordinates
        print(f'{x_start} {y_start} {Width} {Height}')

        # DEBUG: Display Frame Data like [Corners, Object Box]
        cv.imshow(f'nxtframe{i+1}', nxtImgClr)

        # DEBUG: Press Q/q to close all windows and exit loop
        #        Press any other key to display next frame
        quitKey = cv.waitKey(0) & 0xFF
        if quitKey == ord('q') or quitKey == ord('Q'):
            print(
                '\n !!!!!   SYSTEM: user quit frame-by-frame using key press q/Q !!!!!\n')
            cv.destroyAllWindows()
            return 0

    # Terminal Formatting
    print()

    return 0


main()
