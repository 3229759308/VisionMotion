import cv2
import time

VIDEO_URL = "http://192.168.2.201:8080/video"

cap = cv2.VideoCapture(VIDEO_URL)

print(cap.isOpened())

fps_start_time = time.perf_counter()
frame_count = 0
fps = 0.0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1
    current_time = time.perf_counter()

    elapsed_time = current_time - fps_start_time

    if elapsed_time >= 1.0:
        fps = frame_count / elapsed_time
        print(f"FPS: {fps:.2f}")

        frame_count = 0
        fps_start_time = current_time

    display_frame = cv2.resize(frame, (960, 540))
    cv2.putText(
    display_frame,
    f"FPS: {fps:.2f}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,
    (0, 255, 0),
    2,
    cv2.LINE_AA,
    )
    cv2.imshow("Camera", display_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()