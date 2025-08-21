# VirtualNumKeyboard (Two-Hand Gesture Version)

This project implements a **virtual numeric keyboard using hand gestures**, designed for **IoT security applications**. Unlike traditional biometric systems or physical keypads that leave physical traces, this solution uses **two-hand gesture recognition** to enter numeric input, minimizing security risks.

---

## 🔍 About the Project

The **VirtualNumKeyboard** uses computer vision and hand gesture recognition to simulate a numeric keypad. The program detects two hands using **OpenCV** and **cvzone** (HandTrackingModule) and maps different finger combinations to numeric inputs (`0-9`). It can also terminate when a specific gesture is shown.

### ✅ Why Two-Hand Gesture Input?
- **Security:** Avoids physical touch, reducing the risk of fingerprints or hardware keyloggers.
- **Touchless Interaction:** Ideal for IoT devices and secure environments.
- **Customizable:** You can map gestures to any action beyond numbers.

---

## ✨ Features
- Detects **two hands** using the webcam.
- Supports **gesture-based numeric input (0–9)**.
- Special gesture combination for **exit/quit**.
- Uses **cvzone HandDetector** for finger tracking.
- Lightweight and optimized for Raspberry Pi and similar IoT hardware.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rishabh480604/VirtualNumkeyboard.git
cd VirtualNumkeyboard
```

### 2. Install Dependency
```bash
pip install opencv-python
pip install cvzone
pip install pyautogui
```
Gesture Mapping

Here’s how the gestures map to numbers:
```bash
Gesture Pattern (Left + Right)	Output
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]	1
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0]	2
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0]	3
[0, 1, 1, 1, 1, 0, 0, 0, 0, 0]	4
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]	5
[1, 1, 1, 1, 1, 0, 1, 0, 0, 0]	6
[1, 1, 1, 1, 1, 0, 1, 1, 0, 0]	7
[1, 1, 1, 1, 1, 0, 1, 1, 1, 0]	8
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1]	9
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]	0
```
Exit Gesture: [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

### Security Considerations

- Eliminates physical keypad entry, reducing risk of fingerprint detection or hardware keyloggers.
- Dynamic gesture mapping ensures harder-to-guess input patterns.
- Can be integrated with face recognition or biometric validation for multi-factor authentication.
- Works best in controlled environments with consistent lighting for reliable gesture detection.

## Future Enhancements

- Configurable gesture mapping (customize which gesture corresponds to which key).
- Add biometric verification (e.g., face recognition) before enabling gesture input.
- Improve exit gestures for more intuitive shutdown.
- Multi-language support for symbols and alphanumeric entry.
- Error feedback system (e.g., visual indicator for invalid gesture).