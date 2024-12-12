import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot

# MediaPipe Hands 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Pycaw를 이용한 오디오 볼륨 제어 초기화
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# 볼륨 범위 가져오기
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# OpenCV로 웹캠 스트림 열기
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # BGR 이미지를 RGB로 변환
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # MediaPipe Hands로 손 인식
    results = hands.process(image)

    # 다시 BGR로 변환(OpenCV에서 사용하기 위해)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 엄지와 검지의 랜드마크 가져오기
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # 화면 좌표로 변환
            h, w, _ = image.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            # 두 점 사이 거리 계산
            distance = hypot(index_x - thumb_x, index_y - thumb_y)

            # 볼륨 계산 (거리와 볼륨을 매핑)
            vol = np.interp(distance, [30, 200], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)


    cv2.imshow('Hand Volume Control', image)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키로 종료
        break

cap.release()
cv2.destroyAllWindows()
