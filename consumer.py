import time
from kafka_client.kafka_client import KafkaConsumerClient

def main():
    consumer = None
    try:
        consumer = KafkaConsumerClient()
        while True:
            messages = consumer.poll(timeout_ms=10000)  # Poll for messages with a timeout of 10 seconds
            for msg in messages:
                print("Consumed:", msg)
            time.sleep(0.5)
            # if no messages within timeout, break the loop
            if not messages:
                print("No messages received within the timeout period.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if consumer:
            consumer.close()

if __name__ == "__main__":
    main()