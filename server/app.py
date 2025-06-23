from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
from ultralytics import YOLO
from langchain_community.llms import Ollama

app = Flask(_name_)


model = YOLO('yolov8n.pt')

llm = Ollama(model='gemma2:2b')

FOCAL_LENGTH = 973 
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_DISTANCE_CM = 500 

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def calculate_distance(focal_length, real_width, pixel_width):
    return (real_width * focal_length) / pixel_width


real_widths = {
    'person': 0.5,
    'car': 1.8,  
    'truck': 2.5,
    'bottle': 0.05,
    'computer': 0.43,
    'dining table': 1.3,
    'chair': 0.4,
    'tvmonitor': 0.3  
}


@app.route("/detect", methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        
        results = model(filepath)

        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                class_name = model.names[cls]

                pixel_width = x2 - x1

                if class_name in real_widths:
                    distance = calculate_distance(FOCAL_LENGTH, real_widths[class_name], pixel_width)

                    
                    if distance <= MAX_DISTANCE_CM:
                        detections.append({
                            'object': class_name,
                            'distance': round(distance, 2)
                        })

        
        os.remove(filepath)

        return jsonify(detections)

    return jsonify({"error": "Invalid file type"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
