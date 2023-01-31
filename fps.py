import cv2
# Open video

video = cv2.VideoCapture(0)

# Get the frames per second (fps)
fps = video.get(cv2.CAP_PROP_FPS)

print("Frames per second:", fps)

# Release the video file
video.release()
