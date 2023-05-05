import cv2

# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        if success:
            # Check if the frame is a multiple of 10
            if count % 60 == 0:
                # Save the frame with frame-count
                cv2.imwrite("./frame/frame%d.jpg" % count, image)

            count += 1
    while not success:
        print("No Frame Found")

    # Release the video file object and close all windows
    vidObj.release()
    cv2.destroyAllWindows()

# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("./frame/test_new.mp4")
