from deepface import DeepFace
from time import time


class Person:
    def __init__(self):
        self.detections_count = 0
        self.time_in_frame = 0
        self.max_time_in_frame = 0
        self.min_time_in_frame = 0
        self.average_time = 0
        self.vectors = None
        self.photo_path = ""


start = time()
DeepFace.stream('database', frame_threshold=5, source=0)
end = time() - start
print(end)