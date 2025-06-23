import os
import requests
import threading
from PIL import Image
from gtts import gTTS
from googletrans import Translator

API_URL = "http://192.168.96.66:5000/detect"
image_path = "img.jpeg"
translator = Translator()

def capture_image():
    """Captures an image using the Raspberry Pi camera."""
    print("Capturing image...")
    os.system(f"libcamera-still -o {image_path} --timeout 100 --nopreview")
    print(f"Image captured and saved as {image_path}.")

def compress_image():
    """Compresses the captured image."""
    try:
        with Image.open(image_path) as img:
            img.save(image_path, "JPEG", quality=50)
            print(f"Image compressed and saved as {image_path}.")
    except Exception as e:
        print(f"Error compressing image: {e}")

def capture_and_compress():
    """Runs capture and compression in parallel."""
    capture_thread = threading.Thread(target=capture_image)
    capture_thread.start()
    capture_thread.join()
    compress_thread = threading.Thread(target=compress_image)
    compress_thread.start()
    compress_thread.join()

def speak_text(text):
    """Converts text to speech and plays it."""
    tts = gTTS(text, lang='en')
    tts.save('output.mp3')
    os.system("mpg123 output.mp3")

def send_image_to_api():
    """Sends image to API and handles response."""
    if not os.path.exists(image_path):
        print("Image capture failed or image does not exist.")
        return

    print("Sending image to API...")
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        try:
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                detections = response.json()
                spoken_text = ""

                if detections:
                    detections = sorted(detections, key=lambda x: x["distance"])
                    for detection in detections:
                        detection["distance"] = round(detection["distance"] * 3.28084, 1)
                        text = f"{detection['object']} with distance {detection['distance']} feet. "
                        print(text)
                        spoken_text += text

                    translation = translator.translate(spoken_text, dest='en')
                    print(translation.text)
                    speak_thread = threading.Thread(target=speak_text, args=(translation.text,))
                    speak_thread.start()
                else:
                    print("No objects detected.")
                    translation = translator.translate("No objects detected.", dest='en')
                    speak_thread = threading.Thread(target=speak_text, args=(translation.text,))
                    speak_thread.start()
            else:
                print(f"Failed to get response from API. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred while sending the image: {e}")

def main():
    capture_and_compress()
    send_image_to_api()

if __name__ == "__main__":
    main()
