# Library
import cv2

# Select Camera
camera = cv2.VideoCapture(0)

# Read Camera
ret, frame = camera.read()

# Take Picture
if ret:
    cv2.imwrite('Youpic.png', frame)
camera.release()
cv2.destroyAllWindows()


# Finish
# Create By Moein Heshmati
