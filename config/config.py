import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

class Config:
    def __init__(self) -> None:
        # List of Kafka bootstrap servers (split on commas)
        self.BOOTSTRAP_SERVERS: List[str] = [
            server.strip() for server in os.getenv("BOOTSTRAP_SERVERS", "").split(",") if server.strip()
        ]
        self.CONTROLLER_SERVERS: List[str] = [
            server.strip() for server in os.getenv("CONTROLLER_SERVERS", "").split(",") if server.strip()
        ]
        
        # Name of the Kafka topic to use
        self.TOPIC_NAME: str = os.getenv("TOPIC_NAME", "weather_data")
        
        # Default consumer group id (optional)
        self.GROUP_ID: str = os.getenv("GROUP_ID", "weather_data_consumer_group")
        
        # (Optional) Topic creation settings
        self.NUM_PARTITIONS: int = int(os.getenv("NUM_PARTITIONS", "1"))
        self.REPLICATION_FACTOR: int = int(os.getenv("REPLICATION_FACTOR", "3"))
        self.MIN_IN_SYNC_REPLICAS: int = int(os.getenv("MIN_IN_SYNC_REPLICAS", "2"))
        
        # Weather API keys
        self.METEO_STAT_API_KEY: str = os.getenv("METEO_STAT_API_KEY", None)
        self.METEO_STAT_API_HOST: str = os.getenv("METEO_STAT_API_HOST", "meteostat.p.rapidapi.com")
        self.WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY", None)
        
        # Air Quality API
        self.AIR_QUALITY_API_KEY: str = os.getenv("AIR_QUALITY_API_KEY", None)
        self.AIR_QUALITY_API_URL: str = "https://api.waqi.info/feed/{city}/?token={token}"
        self.AIR_QUALITY_REQUEST_TRACKER_FILE: str = os.path.join("requests", "air_quality_request_tracker.txt")
        self.AIR_QUALITY_REQUEST_LIMIT: int = 1000  # Per second (quota limit from API)
config = Config()