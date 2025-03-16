import requests
from typing import Dict
from config.config import config
from util.air_quality_request_tracker import AirQualityRequestTracker

class AirQualityAPI:
    def __init__(self):
        self.api_key = config.AIR_QUALITY_API_KEY
        self.request_tracker = AirQualityRequestTracker()

    def fetch_air_quality(self, city: str) -> Dict:
        # Fetch air quality data for a given city
        self.request_tracker.increment_request()
        url = config.AIR_QUALITY_API_URL.format(city=city, token=self.api_key)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "ok":
                return {
                    "city": data["data"]["city"]["name"],
                    "aqi": data["data"]["aqi"],
                    "timestamp": data["data"]["time"]["s"],
                    "location": data["data"]["city"]["geo"],
                    "source": data["data"]["city"]["url"]
                }
        return {"error": "Could not fetch data"}