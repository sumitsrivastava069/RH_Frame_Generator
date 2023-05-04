import cv2

# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0
    # Time delay in milliseconds between frame captures
    time_delay = 10000
    # Current time
    current_time = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        if success:
            # Check if 10 seconds have passed since the last frame capture
            if count == 0 or (cv2.waitKey(1) & 0xFF == ord('q')) or (cv2.waitKey(1) & 0xFF == ord('n')) or (cv2.waitKey(1) & 0xFF == ord('p')) or (cv2.waitKey(1) & 0xFF == ord('s')):
                if count != 0:
                    # Update the current time
                    current_time += time_delay

                # Save the frame with frame-count
                cv2.imwrite("./frame/frame%d.jpg" % count, image)
                count += 1

                # Update the current time
                current_time = current_time + time_delay

                # Set the video position to the current time
                vidObj.set(cv2.CAP_PROP_POS_MSEC, current_time)

    # Release the video file object and close all windows
    vidObj.release()
    cv2.destroyAllWindows()

# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("./frame/test1.mp4")
