import time
from weather_data.air_quality_api import AirQualityAPI
from kafka_client.kafka_client import KafkaProducerClient
from config.config import config

def get_weather_data():
    # get data from all APIs
    # aggregate data from all APIs using data aggregator
    # yield data continuously
    yield None  # Placeholder for actual data aggregation logic

def main():
    producer = None
    try:
        api = AirQualityAPI()
        producer = KafkaProducerClient()
        producer.create_topic(config.TOPIC_NAME)
        start_time = time.time()
        
        CITIES = ["paris", "berlin", "madrid", "rome", "vienna"]
        
        # still need to invoke methods for data aggregation
        # iterate over data aggregrator which yields data continuously with yield
        # for each data point, send to kafka topic
        # for weather_data in get_weather_data():
        #    producer.send(weather_data)
        
        # For demonstration, we will fetch air quality data for a few cities
        while time.time() - start_time < 10:
            for city in CITIES:
                air_quality_data = api.fetch_air_quality(city)
                if "error" not in air_quality_data:
                    print("Publishing..")
                    if producer.send(air_quality_data):
                        print(f"Successfully sent data for {city}")
                    else:
                        print(f"Failed to send data for {city}")
                    time.sleep(1)  # Prevent hitting rate limits
                else:
                    print(f"Error fetching data for {city}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if producer:
            print("Flushing and closing producer.")
            producer.flush()
            producer.close()
            print("Producer closed.")

if __name__ == "__main__":
    main()