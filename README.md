Egyptian ID Card Recognition System
A Python-based application that detects and processes Egyptian ID cards using YOLO and EasyOCR. This system also identifies fraudulent IDs by verifying elements such as the picture, first name, and last name.

Features
ID Card Detection: Automatically detects and crops the ID card from an image.
Field Detection: Identifies key fields including name, address, and national ID number.
Text Extraction: Extracts text in both Arabic and English.
ID Decoding: Decodes the national ID to extract:
Birth Date
Governorate
Gender
Birth Place
Location
Nationality
Fraud Detection: Recognizes fake IDs by validating the authenticity of the picture and personal information.
Web Interface: User-friendly interface built with Flask.
Installation
Clone the repository:
Navigate to the project directory:
cd ocr_egyptian_ID
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Usage
Run the application:
python flask.py
Run the application:
streamlit run APP.py
Upload an Image: Use the web interface to upload an image of an Egyptian ID card.
View Results: The application will display the detected ID card, extracted fields, and decoded information.
Model Training
YOLO Model: Trained for ID card detection.
EasyOCR: Utilized for text extraction in Arabic and English.
Acknowledgments
YOLO for object detection.
EasyOCR for optical character recognition.
