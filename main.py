import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions
import pygame
import keyboard

# ----------------------------
# Initialize Sound Engine
# ----------------------------

pygame.mixer.init()

sounds = {
    "a": pygame.mixer.Sound("sounds/sa.wav"),
    "s": pygame.mixer.Sound("sounds/re.wav"),
    "d": pygame.mixer.Sound("sounds/ga.wav"),
    "f": pygame.mixer.Sound("sounds/ma.wav"),
    "g": pygame.mixer.Sound("sounds/pa.wav"),
    "h": pygame.mixer.Sound("sounds/dha.wav"),
    "j": pygame.mixer.Sound("sounds/ni.wav")
}

playing = {}

# ----------------------------
# MediaPipe Setup
# ----------------------------

options = vision.HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    num_hands=1
)

landmarker = vision.HandLandmarker.create_from_options(options)

# ----------------------------
# Webcam Setup
# ----------------------------

cap = cv2.VideoCapture(0)

# reduce resolution for speed
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

previous_y = None
airflow = 0.0
new_airflow = 0.0

frame_count = 0
result = None

# ----------------------------
# Main Loop
# ----------------------------

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    # run hand detection only every 2 frames
    if frame_count % 2 == 0:
        result = landmarker.detect(mp_image)

    if result and result.hand_landmarks:

        for hand in result.hand_landmarks:

            finger = hand[8]  # index finger

            h, w, _ = frame.shape
            x = int(finger.x * w)
            y = int(finger.y * h)

            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            if previous_y is not None:

                delta = y - previous_y

                # downward pump
                if delta > 5:
                    new_airflow += delta * 0.002

            previous_y = y

    # decay air
    new_airflow -= 0.01
    new_airflow = max(0, min(1, new_airflow))

    # airflow smoothing filter
    airflow = airflow * 0.9 + new_airflow * 0.1

    # ----------------------------
    # Keyboard Notes
    # ----------------------------

    for key in sounds:

        if keyboard.is_pressed(key):

            if key not in playing:
                channel = sounds[key].play(loops=-1)
                playing[key] = channel

        else:

            if key in playing:
                playing[key].stop()
                del playing[key]

    # ----------------------------
    # Apply Volume from Airflow
    # ----------------------------

    for channel in playing.values():
        channel.set_volume(airflow)

    # ----------------------------
    # UI
    # ----------------------------

    bar_width = int(airflow * 200)

    cv2.rectangle(frame, (20, 80), (20 + bar_width, 120), (0, 255, 0), -1)
    cv2.rectangle(frame, (20, 80), (220, 120), (255, 255, 255), 2)

    cv2.putText(frame, f"Airflow: {airflow:.2f}",
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    cv2.putText(frame,
                "Keys: A S D F G H J",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2)

    cv2.imshow("Gesture Harmonium", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()