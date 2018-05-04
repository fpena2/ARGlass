import pytesseract
import cv2
from moviepy.editor import VideoFileClip

def videoProcessing():
    videoFrame = VideoFileClip('f2.mp4')
    for aFrame in videoFrame.iter_frames():
        aFrame = cv2.cvtColor(aFrame, cv2.COLOR_RGB2GRAY)
       
       """[yPixel: yPixel + height, xPixel: xPixel + width]"""
        teamOneScore = aFrame[595:595 + 37, 431: 431 + 55]
        teamTwoScore = aFrame[593: 593 + 43, 624: 624 + 51]
        teamOne = aFrame[597: 597 + 32, 362: 362 + 70]
        teamTwo = aFrame[593: 593 + 33, 547: 547 + 73]

        print(pytesseract.image_to_string(teamTwoScore, config='-psm 6' ))

    cv2.imshow("image", teamTwoScore)
    # cv2.imwrite('messigray.png',aFrame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
