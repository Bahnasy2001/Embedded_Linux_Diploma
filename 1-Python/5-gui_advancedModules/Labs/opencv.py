# pip install opencv-python
import cv2

def main():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)
    # Check if the Camera was opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the camera. ")
        return
    # Set the window name for the live video stream
    window_name = "Camera Preview"
    cv2.namedWindow(window_name)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Check if the frame was captured successfully
        if not ret:
            print("Error: Unable to capture frame. ")
            break
        # Display the frame in a window
        cv2.imshow(window_name,frame)
        # Break the loop when the 'q'key is pressed
        key = cv2.waitKey(1)
        if key == ord('c'): # press 'c' to take a picture
            # save the captured frame as an image 
            cv2.imwrite("captured_image.jpg",frame)
            print("Image captured successfully")
        # Break the loop when the 'q' key is pressed
        if key == ord('q'):
            break
    # Release the camera and close window
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()

