import time
import shutil
import os

def process_video(input_video_path):
    """
    MOCK ML PROCESSOR
    This simulates the output of the real YOLO-based ML pipeline.
    """

    # Simulate processing time
    time.sleep(2)

    # Create mock output directories
    os.makedirs("static/outputs/faces", exist_ok=True)
    os.makedirs("static/outputs/plates", exist_ok=True)
    os.makedirs("static/outputs/processed_videos", exist_ok=True)

    # Fake processed video (just copy original)
    processed_video_path = "static/outputs/processed_videos/processed_demo.mp4"
    shutil.copy(input_video_path, processed_video_path)

    # Fake evidence images (placeholders)
    fake_faces = [
        "/static/outputs/faces/face_1.jpg",
        "/static/outputs/faces/face_2.jpg"
    ]

    fake_plates = [
        "/static/outputs/plates/plate_1.jpg"
    ]

    return {
        "processed_video": "/static/outputs/processed_videos/processed_demo.mp4",
        "stats": {
            "total_motorcycles": 12,
            "helmet_violations": 4
        },
        "faces": fake_faces,
        "plates": fake_plates,
        "processing_time": 2.0
    }
