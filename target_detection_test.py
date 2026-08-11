import cv2
import time

VIDEO_URL = "http://127.0.0.1:4747/video/1920x1080"

cap = cv2.VideoCapture(VIDEO_URL)

print(cap.isOpened())

fps_start_time = time.perf_counter()
frame_count = 0
fps = 0.0

while True:
    ret, frame = cap.read()

    if not ret:
        break
    height, width = frame.shape[:2]

    center_x = width // 2
    center_y = height // 2

    center_bgr = frame[center_y, center_x]
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    center_hsv = hsv_frame[center_y, center_x]

    lower_orange = (8, 150, 120)
    upper_orange = (20, 255, 255)
    MIN_TARGET_AREA = 5000

    mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    clean_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(
    clean_mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE,
    )
    target_contour = None
    target_area = 0.0

    if contours:
        candidate = max(contours, key=cv2.contourArea)
        candidate_area = cv2.contourArea(candidate)

        if candidate_area >= MIN_TARGET_AREA:
            target_contour = candidate
            target_area = candidate_area
            moments = cv2.moments(target_contour)
    if target_contour is not None:
        x, y, w, h = cv2.boundingRect(target_contour)
        box_center_x = x + w // 2
        box_center_y = y + h // 2

        if moments["m00"] != 0:
            target_x = int(moments["m10"] / moments["m00"])
            target_y = int(moments["m01"] / moments["m00"])
        else:
            target_x = box_center_x
            target_y = box_center_y

        cv2.putText(
        frame,
        f"Target: ({target_x}, {target_y})",
        (x, max(y - 15, 30)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
        )
        cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3,
        )
        cv2.circle(
        frame,
        (target_x, target_y),
        8,
        (255, 0, 0),
        -1,
        )


    frame_count += 1
    current_time = time.perf_counter()

    elapsed_time = current_time - fps_start_time

    if elapsed_time >= 1.0:
        fps = frame_count / elapsed_time
        print(f"FPS: {fps:.2f}")
        print(f"Target Detected: {target_contour is not None}")
        print(f"Center BGR: {center_bgr}")
        print(f"Center HSV: {center_hsv}")

        areas = [cv2.contourArea(contour) for contour in contours]
        if target_contour is not None:
            print(f"Target Center: ({target_x}, {target_y})")
            print(f"Target Area: {target_area:.1f}")
            print(
            f"Box Center: ({box_center_x}, {box_center_y}), "
            f"Delta: ({target_x - box_center_x}, {target_y - box_center_y})"
                )

        print(f"Contours: {len(contours)}")
        print(f"Areas: {sorted(areas, reverse=True)[:5]}")

        frame_count = 0
        fps_start_time = current_time

    display_frame = cv2.resize(frame, (960, 540))
    display_height, display_width = display_frame.shape[:2]

    cv2.drawMarker(
        display_frame,
        (display_width // 2, display_height // 2),
        (0, 0, 255),
        cv2.MARKER_CROSS,
        30,
        2,
    )
    height, width = frame.shape[:2]
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
    cv2.putText(
    display_frame,
    f"Resolution: {width}x{height}",
    (20, 80),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,
    (0, 255, 0),
    2,
    cv2.LINE_AA,
    )
    cv2.imshow("Camera", display_frame)
    cv2.imshow("Mask", cv2.resize(clean_mask, (960, 540)))

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()