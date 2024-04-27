import pickle
import cv2
import mediapipe as mp
import numpy as np
import time
import pyttsx3

engine = pyttsx3.init()

try:
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']
except Exception as e:
    print("Error loading model:", e)
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Updated labels_dict for A to Z
labels_dict = {i: chr(ord('A') + i) for i in range(26)}

# Set the duration of the video in seconds (10 minutes = 600 seconds)
video_duration = 600
start_time = time.time()

# Adjusted rendering frequency
render_frequency = 5
frame_count = 0

# Flag to indicate if detection should start
start_detection = False

# Flag to indicate if audio should be played
play_audio = True

while True:
    try:
        data_aux_list = []
        x_list = []
        y_list = []

        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read frame")
            continue

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if start_detection:
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

                    x = []
                    y = []
                    data_aux = []
                    for landmark in hand_landmarks.landmark:
                        x.append(landmark.x)
                        y.append(landmark.y)
                    min_x, min_y = min(x), min(y)
                    for i in range(len(x)):
                        data_aux.append(x[i] - min_x)
                        data_aux.append(y[i] - min_y)
                    data_aux_list.append(data_aux)
                    x_list.append(x)
                    y_list.append(y)

            for i in range(len(data_aux_list)):
                prediction = model.predict([np.asarray(data_aux_list[i])])
                predicted_character = labels_dict[int(prediction[0])]

                min_x = int(min(x_list[i]) * W) - 10
                min_y = int(min(y_list[i]) * H) - 10
                max_x = int(max(x_list[i]) * W) - 10
                max_y = int(max(y_list[i]) * H) - 10

                cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character, (min_x, min_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)
                
                if play_audio:
                    engine.say(predicted_character)
                    engine.runAndWait()
                    play_audio = False

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == ord('b'):  # Press 'b' to start detection
            start_detection = True
            play_audio = True

        # Check if 10 minutes have passed or if "s" key is pressed, break the loop if true
        if time.time() - start_time > video_duration or key == ord('s'):
            break

        frame_count += 1
        if frame_count % render_frequency == 0:
            frame_count = 0

    except Exception as e:
        print("Error:", e)

cap.release()
cv2.destroyAllWindows()
