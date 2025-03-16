import time
import json
import os
from config.config import config

class AirQualityRequestTracker:
    def __init__(self):
        self.filepath = config.AIR_QUALITY_REQUEST_TRACKER_FILE
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        self.request_count = 0
        self.load_requests()

    def load_requests(self):
        # Load previous request count from file
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
                self.request_count = data.get("count", 0)
                self.timestamp = data.get("timestamp", time.time())
        except FileNotFoundError:
            self.request_count = 0
            self.timestamp = time.time()

    def save_requests(self):
        with open(self.filepath, "w") as file:
            json.dump({"count": self.request_count, "timestamp": time.time()}, file)

    def check_limit(self):
        if self.request_count >= config.AIR_QUALITY_REQUEST_LIMIT:
            elapsed_time = time.time() - self.timestamp
            if elapsed_time < 1:  # 1 second window
                print("API request limit reached! Waiting...")
                time.sleep(1 - elapsed_time)
            self.request_count = 0  # Reset count after time window

    def increment_request(self):
        self.check_limit()
        self.request_count += 1
        self.save_requests()