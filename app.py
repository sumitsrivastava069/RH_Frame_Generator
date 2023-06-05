import os
import cv2
import time
from flask import Flask
import csv
import logging

def write_to_csv(file_name):
    csv_file = "./storage/Frame/processed_files.csv"
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([file_name])


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
    csv_file = "./storage/Frame/processed_files.csv"
    # Load existing file names from CSV
    existing_files = set()
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            existing_files.add(row[0])

    logging.basicConfig(filename='error.log', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    while True:
        # get all files in the folder
        files = os.listdir(folder_path)

        # check for new files
        for file_name in files:
            try:
                if file_name.endswith(".mp4") and file_name not in existing_files:
                    file_path = os.path.join(folder_path, file_name)
                    frame_capture(file_path)
                    write_to_csv(file_name)
                    existing_files.add(file_name)
                    print("New video file received: ", file_name)
            except Exception as e:
                logging.error(str(e))

        # sleep for a few seconds before checking again
        time.sleep(5)

app = Flask(__name__)
if __name__ == '__main__':
    monitor_folder()
    
    app.run()
