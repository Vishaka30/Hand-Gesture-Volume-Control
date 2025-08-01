import os
import time
import cv2
import mediapipe as mp
import numpy as np
import platform
import sys

# Check OS
current_os = platform.system()

if current_os == "Windows":
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

    def increase_volume():
        current_vol = volume_interface.GetMasterVolumeLevelScalar()
        volume_interface.SetMasterVolumeLevelScalar(min(1.0, current_vol + 0.05), None)

    def decrease_volume():
        current_vol = volume_interface.GetMasterVolumeLevelScalar()
        volume_interface.SetMasterVolumeLevelScalar(max(0.0, current_vol - 0.05), None)

elif current_os == "Darwin":  # macOS
    def increase_volume():
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 5)'")

    def decrease_volume():
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 5)'")

else:
    print("Unsupported OS for this script. Only macOS and Windows are supported.")
    sys.exit(1)

# Set webcam resolution
wCam, hCam = 1280, 720
webcam = cv2.VideoCapture(0)
webcam.set(3, wCam)
webcam.set(4, hCam)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

pTime = 0

while True:
    success, image = webcam.read()
    if not success:
        break

    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):
                x, y = int(lm.x * frame_width), int(lm.y * frame_height)
                lm_list.append((id, x, y))

            if len(lm_list) >= 9:
                x4, y4 = lm_list[4][1], lm_list[4][2]
                x8, y8 = lm_list[8][1], lm_list[8][2]

                cv2.circle(image, (x4, y4), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(image, (x8, y8), 10, (0, 0, 255), cv2.FILLED)
                cv2.line(image, (x4, y4), (x8, y8), (0, 255, 0), 3)

                # Calculate distance
                dist = ((x8 - x4) ** 2 + (y8 - y4) ** 2) ** 0.5

                # Adjust volume
                if dist > 50:
                    increase_volume()
                else:
                    decrease_volume()

    # Display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime + 0.0001)
    pTime = cTime
    cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Show image
    cv2.imshow("Gesture Volume Control", image)
    key = cv2.waitKey(10)
    if key == 27:  # ESC
        break

webcam.release()
cv2.destroyAllWindows()
