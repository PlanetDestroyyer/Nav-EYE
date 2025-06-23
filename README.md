# Nav-Eye 🚶‍♂️🦯🔍

**Nav-Eye** is an AI-powered assistive system designed to help visually impaired individuals navigate their environment. It uses a Raspberry Pi-based edge device to capture real-time video and send it to a backend server for object detection and scene understanding. The results are then conveyed back to the user via audio feedback.

---

## 📁 Project Structure

├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── rpi_code/ # Code running on the Raspberry Pi
│ └── main.py # Captures video and sends it to the server
└── server/ # Backend server for object detection & response
└── app.py # Flask-based backend using YOLO and LLM


---

## 🛠️ Requirements

- Python 3.8+
- Raspberry Pi 3/4 with Camera Module
- Internet connection (for communication with server)
- `ultralytics` (for YOLO)
- `Flask`, `opencv-python`, `requests`, `langchain`, etc.

Install dependencies:

```bash
pip install -r requirements.txt

🚀 How to Run
1. Run the Backend Server

Navigate to the server/ directory:

cd server
python app.py

This will start the Flask server which listens for image frames and responds with detected objects and navigational insights.
2. Run the Raspberry Pi Code

On the Raspberry Pi:

cd rpi_code
python main.py

This will start capturing frames, sending them to the server, and playing back the responses (e.g., via text-to-speech or speaker).
🧠 Features

    Real-time object detection using YOLOv8

    Communication between Raspberry Pi and backend

    Audio feedback for the user

    Language model integration for better scene description (via LLM)

📌 Future Enhancements

    Add obstacle distance estimation

    Integrate GPS for outdoor navigation

    Improve LLM-based contextual reasoning

    Offline YOLO processing on RPi with Coral/TPU
