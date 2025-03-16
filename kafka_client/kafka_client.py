import json
from typing import List, Dict, Any
from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError, TopicAlreadyExistsError
from config.config import config

class KafkaProducerClient:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=config.BOOTSTRAP_SERVERS,
            acks="all",
            value_serializer=lambda m: json.dumps(m).encode("utf-8")
        )
        self.admin_client = KafkaAdminClient(bootstrap_servers=config.BOOTSTRAP_SERVERS)

        
    def create_topic(self, topic: str = config.TOPIC_NAME) -> None:
        try:
            topic_config = {
                "min.insync.replicas": str(config.MIN_IN_SYNC_REPLICAS)
            }
            new_topic = NewTopic(
                name=topic,
                num_partitions=config.NUM_PARTITIONS,
                replication_factor=config.REPLICATION_FACTOR,
                topic_configs=topic_config
            )
            self.admin_client.create_topics([new_topic])
            print(f"Created topic '{topic}' with {config.NUM_PARTITIONS} partitions and {config.REPLICATION_FACTOR} replicas.")
        except TopicAlreadyExistsError:
            print(f"Topic '{topic}' already exists.")
        except Exception as e:
            print(f"Error creating topic '{topic}': {e}")
    
    def send(self, message: Dict[str, Any], topic: str = config.TOPIC_NAME) -> bool:
        try:
            future = self.producer.send(topic, value=message)
            record_metadata = future.get(timeout=10)  # Wait for Kafka's acknowledgment
            print(f"Message written to {topic} | Partition: {record_metadata.partition} | Offset: {record_metadata.offset}")
            return True
        except KafkaError as e:
            print(f"Failed to send message: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    def flush(self) -> None:
        self.producer.flush()
        
    def close(self) -> None:
        self.producer.close()


class KafkaConsumerClient:
    def __init__(self):
        self.consumer = KafkaConsumer(
            config.TOPIC_NAME,
            bootstrap_servers=config.BOOTSTRAP_SERVERS,
            group_id=config.GROUP_ID,
            auto_offset_reset="earliest",
            value_deserializer=lambda m: json.loads(m.decode("utf-8"))
        )
    
    def poll(self, timeout_ms: int = 10000) -> List[Dict[str, Any]]:
        messages: List[Dict[str, Any]] = []
        msg_pack = self.consumer.poll(timeout_ms=timeout_ms)
        for tp, msgs in msg_pack.items():
            for msg in msgs:
                messages.append(msg.value)
        return messages

    def close(self):
        self.consumer.close()