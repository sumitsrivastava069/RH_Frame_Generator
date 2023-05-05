import cv2
from flask import Flask

app = Flask(__name__)

def FrameCapture(path):
    
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    
    success = 1

    while success:
        # vidObj object calls read function to extract frames
        success, image = vidObj.read()

        if success:
            # Check if the frame is a multiple of 10
            if count % 60 == 0:
                
                cv2.imwrite("./frame_new/frame%d.jpg" % count, image)

            count += 1
    while not success:
        print("No Frame Found")

    
    vidObj.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = "./frame/test_new.mp4"
    FrameCapture(path)

    
    app.run()
