```markdown
# Nav-Eye 🚶‍♂️🦯🔍

**Nav-Eye** is an AI-powered assistive system designed to help visually impaired individuals navigate their surroundings. It uses a Raspberry Pi-based edge device to capture real-time video, which is sent to a backend server for object detection and scene understanding. The results are conveyed to the user via audio feedback.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![YOLO](https://img.shields.io/badge/YOLO-v8-orange.svg)](https://github.com/ultralytics/ultralytics)

---

## 📁 Project Structure

```plaintext
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── rpi_code/              # Code running on the Raspberry Pi
│   └── main.py            # Captures video and sends it to the server
└── server/                # Backend server for object detection & response
    └── app.py             # Flask-based backend using YOLO and LLM
```

---

## 🛠️ Requirements

- **Hardware**:
  - Raspberry Pi 3 or 4 with Camera Module
  - Speaker or audio output device
  - Stable internet connection (for communication with the server)

- **Software**:
  - Python 3.8 or higher
  - Dependencies: `ultralytics`, `Flask`, `opencv-python`, `requests`, `langchain`, etc.

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 1. Run the Backend Server

Navigate to the `server/` directory and start the Flask server:

```bash
cd server
python app.py
```

The server will listen for image frames from the Raspberry Pi and respond with detected objects and navigational insights.

### 2. Run the Raspberry Pi Code

On the Raspberry Pi, navigate to the `rpi_code/` directory and run:

```bash
cd rpi_code
python main.py
```

This script captures video frames, sends them to the server, and plays the server's responses via audio (e.g., text-to-speech or speaker).

---

## 🧠 Features

- **Real-time Object Detection**: Powered by YOLOv8 for accurate and fast object identification.
- **Edge-to-Cloud Communication**: Seamless interaction between the Raspberry Pi and backend server.
- **Audio Feedback**: Descriptive audio output to guide the user.
- **Scene Understanding**: Language model integration for contextual scene descriptions.

---

## 📌 Future Enhancements

- Obstacle distance estimation using depth sensing.
- GPS integration for outdoor navigation.
- Improved contextual reasoning with advanced LLM models.
- Offline YOLO processing on Raspberry Pi using Coral/TPU.



