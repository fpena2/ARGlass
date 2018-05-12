import pytesseract
import cv2
from moviepy.editor import VideoFileClip
import string

# Function to process a video file frame-by-frame
def getScreenData(socket=None):
    videoFrame = VideoFileClip('f2.mp4') # loads file located in current dir 
    flag = "--psm 6"  # Tesseract flag to detect digits
    redValue_prev = "-1"
    blueValue_prev = "-1"

    for aFrame in videoFrame.iter_frames(fps = 4):
        aFrame = cv2.cvtColor(aFrame, cv2.COLOR_RGB2GRAY)

        """[yPixel: yPixel + height, xPixel: xPixel + width]
        Coordinates used for CBS Sports"""
        bluescore_img = aFrame[595:595 + 37, 431: 431 + 55]
        redscore_img = aFrame[593: 593 + 43, 624: 624 + 51]
        blue_img = aFrame[597: 597 + 32, 362: 362 + 70]
        red_img = aFrame[593: 593 + 33, 547: 547 + 73]

        # converting images to strings
        blueValue = pytesseract.image_to_string(bluescore_img, config=flag)
        blueName = pytesseract.image_to_string(blue_img, config=flag)

        redValue = pytesseract.image_to_string(redscore_img, config=flag)
        redName = pytesseract.image_to_string(red_img, config=flag)
        
        # Pytesseract can return false-positives
        # This statement filters values that are not digits nor possible team names 
        try:
            if(redName.isalpha() and redValue_prev != redValue and int(redValue_prev) <= int(redValue)):
                print("{0} = {1}".format(redName, int(redValue)))
                socket.send("{0} = {1}".format(redName, int(redValue)))
                redValue_prev = redValue

            if(blueName.isalpha() and blueValue_prev != blueValue and int(blueValue_prev) <= int(blueValue)):
                print("{0} = {1}".format(blueName, int(blueValue)))
                socket.send("{0} = {1}".format(blueName, int(blueValue)))
                blueValue_prev = blueValue

        except ValueError:
            #print("wrong value")
            continue
