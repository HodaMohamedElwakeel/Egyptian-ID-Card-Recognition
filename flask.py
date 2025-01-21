from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import easyocr

# Initialize Flask app
gui = Flask(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['ar'], gpu=False)

# Functions from your script (add them here, e.g., detect_and_process_id_card, etc.)

@gui.route('/')
def home():
    return render_template('index.html')  # HTML template for the upload form

@gui.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Convert uploaded file to a NumPy array
    img = Image.open(file.stream)
    img_np = np.array(img)

    # Process the image using your function
    try:
        results = detect_and_process_id_card(img_np)
        response = {
            "First Name": results[0],
            "Second Name": results[1],
            "Full Name": results[2],
            "National ID": results[3],
            "Address": results[4],
            "Birth Date": results[5],
            "Governorate": results[6],
            "Gender": results[7]
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    gui.run(debug=True)
