import cv2
import os

# upload the video
video_path = "path.MP4"
cap = cv2.VideoCapture(video_path)

# create a folder to save the frames
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0
while True:
    ret, frame = cap.read() # ret means reading successfull or not
    if not ret:
        break
    # save the frames from the video
    cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)
    frame_count += 50

cap.release()
print(f"Total {frame_count} frames saved.")
