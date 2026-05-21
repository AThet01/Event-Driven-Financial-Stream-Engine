# Real-Time Financial Transaction Streaming Engine via Apache Kafka

An end-to-end event-driven streaming data pipeline designed to ingest, process, and analyze continuous financial logging data. Built with Docker, Apache Kafka, Python-Native Streaming Clients, and Streamlit.

## Tech Stack
* **Infrastructure Orchestration:** Docker, Docker Compose
* **Event Brokerage:** Apache Kafka, Apache Zookeeper
* **Streaming Logic & Aggregation:** Python 3 (Kafka-Python clients)
* **Real-time Interface:** Streamlit Engine, Pandas DataFrames

## System Setup & Reproducibility Guide

### 1. Fire up the Kafka Cluster Infrastructure
Ensure you have Docker Desktop running, then run:
```bash
docker-compose up -d