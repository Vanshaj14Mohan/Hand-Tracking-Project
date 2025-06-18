# ✋ Real-Time Hand Tracking with MediaPipe and OpenCV

This project demonstrates real-time hand tracking using **MediaPipe** and **OpenCV**. It captures live video from your webcam, detects hand landmarks, and overlays them along with frames per second (FPS) in a display window. Ideal for anyone exploring gesture recognition, computer vision, or interactive applications using hand inputs.

---

## 🚀 Features

* Real-time hand detection and landmark tracking
* Coordinates of each landmark printed to console
* Highlights the wrist (landmark ID 0) with a colored circle
* Displays the frame rate (FPS) on screen
* Uses MediaPipe's pre-trained hand tracking model

---

## 🛠️ Technologies Used

* Python 🐍
* [MediaPipe](https://google.github.io/mediapipe/) by Google
* OpenCV (cv2)

---

## 📂 Project Structure

```plaintext
hand-tracking-project/
│
├── main.py              # Main file to run the hand tracking
├── README.md            # Project overview and details
```

---

## 🖥️ How It Works

1. Accesses webcam feed using `cv2.VideoCapture(0)`
2. Converts each frame to RGB for MediaPipe processing
3. Detects hand landmarks using `mp.solutions.hands`
4. Draws landmarks and connections on the hand
5. Highlights landmark ID 0 (wrist point)
6. Calculates and displays FPS in real time

---

## ✅ Landmark Details

* Each hand has 21 landmarks (e.g., fingertips, joints, wrist).
* Example: ID `0` is the wrist, `4` is the tip of the thumb.

---

## ▶️ Getting Started

### Prerequisites

* Python 3.x
* OpenCV
* MediaPipe

### Installation

```bash
pip install opencv-python mediapipe
```

### Run the Code

```bash
python main.py
```

Make sure your webcam is connected and accessible.

---

## 🙌 Applications

* Gesture-based controls
* Sign language recognition
* Augmented Reality (AR)
* Human-computer interaction

---

## 📌 Notes

* Landmark IDs can be used to build more complex gesture detection logic.
* The frame rate display helps in evaluating real-time performance.
* You can modify the code to detect multiple hands or track specific finger tips.

---

## 💡 Future Enhancements

* Add gesture recognition (like thumbs up, victory sign)
* Save gesture data for training models
* Integrate with a GUI or web app

---

👤 Author

Made with ❤️ by Vanshaj P Mohan a Data Science Enthusiast.

---
