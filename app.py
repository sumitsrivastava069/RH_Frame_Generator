import os
import cv2
import time
from flask import Flask


app = Flask(__name__)

def frame_capture(path):
    
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    
    success = True

    while success:
        # vidObj object calls read function to extract frames
        success, image = vidObj.read()

        if success:
            # Check if the frame is a multiple of 10
            if count % 60 == 0:
                cv2.imwrite("./storage/Frame/frame%d.jpg" % count, image)

            count += 1

    vidObj.release()
    cv2.destroyAllWindows()


def monitor_folder():
    
    folder_path = "./storage/CCTV_Capture"
    
    processed_files = set()

    while True:
        
        # get all files in the folder
        files = os.listdir(folder_path)

        # check for new files
        for file_name in files:
            if file_name.endswith(".mp4") and file_name not in processed_files:
                
                file_path = os.path.join(folder_path, file_name)
                frame_capture(file_path)
                processed_files.add(file_name)
                
                print("New video file received: ", file_name)

        # sleep for a few seconds before checking again
        time.sleep(5)


if __name__ == '__main__':
    monitor_folder()
    
    app.run()
