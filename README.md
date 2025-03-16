<<<<<<< HEAD
# claudeTest
=======
# Weather Data Streaming System

This exercise implements a Kafka-based streaming system for collecting, processing, and consuming weather data from multiple sources.

## System Architecture

The system consists of:
1. A Kafka cluster (3 brokers) for resilient data streaming
2. A producer service that collects weather data and publishes to Kafka
3. A consumer service that processes the streaming weather data

## Kafka Configuration Analysis (Broker, Partition, Replica & In-Sync Replicas)

### Number of Brokers
- Brokers are individual Kafka servers that manage topics and store data.
- The more brokers, the better the fault tolerance and load distribution.

### Number of Partitions
- Partitions allow topics to be divided across brokers for parallel processing.
- Messages within a partition are ordered, but across partitions, there is no order guarantee.

### Number of Replicas
- Replicas are copies of partitions stored on multiple brokers.
- They improve fault tolerance: if one broker fails, another with a replica can take over.

### in.sync.replica (ISR) Configuration
- ISR is the set of replicas that are up-to-date with the leader partition.
- If ISR ≠ Replica list, some brokers are lagging or unavailable.
- Messages are considered "committed" only if they are written to `KAFKA_MIN_INSYNC_REPLICAS` number of brokers.

For This Project:
- We have 3 Kafka brokers.
- Default replication factor = 3 (each partition is copied to all brokers).
- `KAFKA_MIN_INSYNC_REPLICAS = 2` (at least 2 brokers must acknowledge a message before it is committed).

## Setup Instructions

### Prerequisites
- Docker and Docker Compose
- Python 3.8+

### Virtual Environment Setup
Setting up a dedicated virtual environment is recommended to isolate project dependencies:

#### Windows
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Your command prompt should now show (venv) at the beginning
```

#### macOS/Linux
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Your terminal should now show (venv) at the beginning
```

### Environment Configuration
1. Edit the `.env` file to set up Kafka related config and add your weather API keys

### Starting the Kafka Cluster
Run the following command to start the Kafka cluster:
```bash
docker compose up -d
```

This starts a 3-node Kafka cluster with the following endpoints:
- Broker 1: `localhost:9092`
- Broker 2: `localhost:9094`
- Broker 3: `localhost:9096`

### Running the Application
1. Install the required dependencies (make sure your virtual environment is activated):
   ```bash
   pip install -r requirements.txt
   ```

2. Run the producer to start sending weather data to Kafka:
   ```bash
   python producer.py
   ```

3. In a separate terminal, run the consumer to process the data:
   ```bash
   python consumer.py
   ```

### Deactivating the Virtual Environment
When you're done working with the project, deactivate the virtual environment:
```bash
deactivate
```

## Project Structure
- `docker-compose.yml`: Docker configuration for the Kafka cluster
- `.env`: Environment variables for configuration
- `requirements.txt`: Python dependencies
- `kafka/kafka_client.py`: Wrapper classes for Kafka producer and consumer
- `config/config.py`: Configuration management for the application
- `producer.py`: Main script for collecting and publishing weather data
- `consumer.py`: Main script for processing the weather data stream
- `weather_data/`: Directory containing weather data aggregation logic
  - `air_quality_api.py`: Client for interacting with Air Quality Index API
  - `meteo_stat_api.py`: Client for MeteoStat API
  - `weather_api.py`: Client for Weather API
  - `weather_data_aggregator.py`: Aggregates data from multiple sources
- `util/`: Utility functions
  - `air_quality_request_tracker.py`: Rate limiting for Air Quality API requests

## Completed Tasks
- Set up resilient Kafka cluster with Docker Compose (3 brokers)
  - Ensured resiliency by configuring Kafka with a minimum in-sync replicas setting (`KAFKA_MIN_INSYNC_REPLICAS: 2`). This ensures that at least two replicas must acknowledge a write for it to be considered successful, providing fault tolerance in case of broker failures.
  - Configured the Kafka cluster with a default replication factor of 3 (`KAFKA_DEFAULT_REPLICATION_FACTOR: 3`), ensuring that each partition is replicated across three brokers for high availability.
  - Set up a 3-node Kafka cluster using Docker Compose, with each broker running in a separate container and configured for both broker and controller roles.
- Implemented Kafka client wrappers for producing and consuming
- Created configuration management system with environment variables
- Built basic producer and consumer functionality
- Implemented proper error handling and resource cleanup
- Implemented Air Quality Index API with request rate limiting

## Tasks To Be Completed
- Implement additional weather data API clients
  - Complete MeteoStat API client implementation
  - Complete Weather API client implementation
- Create `weather_data_aggregator.py` to combine data from different sources
  - Implement functionality to merge data from multiple sources
  - Create standardized data format for different API responses

## Troubleshooting
- If you encounter connection issues, make sure all Kafka brokers are running:
  ```bash
  docker ps | grep kafka
  ```
- Check Kafka broker logs:
  ```bash
  docker logs kafka1 # or kafka2 and kafka3
  ```
- If you see dependency errors, ensure your virtual environment is activated (you should see `(venv)` in your terminal prompt)
>>>>>>> e3af2e3 (Initial commit to new repository)
