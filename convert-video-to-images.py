import cv2
import os

# upload the video
video_path = "path.MP4"
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")
fps = int(fps) / 3

print(f"Frames per second: {fps}")

# create a folder to save the frames
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0
image_count = 0
while True:

    ret, frame = cap.read() # ret means reading successfull or not
    if not ret:
        break

    # save the frames from the video
    if frame_count % fps == 0:
        cv2.imwrite(f"{output_folder}/frame_{image_count}.jpg", frame)
        image_count += 1

    frame_count += 1

cap.release()
print(f"Total {image_count} frames saved.")
