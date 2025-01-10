#for exctracting and saving landmark data
from db_manager import insert_landmark_data

def collect_data(label):
    # Logic to extract landmarks from MediaPipe
    landmarks = extract_landmarks()  # Your existing extraction logic
    insert_landmark_data(label, landmarks)
