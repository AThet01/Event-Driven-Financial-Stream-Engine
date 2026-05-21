# Event-Driven-Financial-Stream-Engine

## Define the README content with description included
readme_content = """# 📊 End-to-End Real-Time Transaction Streaming Pipeline

An enterprise-grade, event-driven streaming data pipeline designed to ingest, transform, and visualize live financial transaction streams with sub-second latency. This project implements a fully decoupled architecture utilizing **Apache Kafka** as a high-throughput distributed event broker, **Python** for stream simulation and transformation, and **Streamlit** for interactive, real-time analytics.

[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-7.5.0-black?style=flat-square&logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI%20Engine-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)

---

## 📝 Project Description

This repository showcases a production-ready, event-driven data engineering project designed to eliminate typical 24-hour batch window latencies. By leveraging containerized message brokers and Python-native streaming clients, the system ingests randomized mock financial transaction streams, processes payloads on the fly through schema-validation/filtering logic, and exposes real-time business intelligence metrics via a live-refreshing data dashboard.

---

## 🏗️ System Architecture

The pipeline is built on an **Event-Driven Architecture (EDA)** that enforces a strict separation of concerns among data ingestion, message brokerage, stream processing, and consumer visualization.

---

## Architectural Highlights
* **Decoupled Components:** The data source (`producer.py`) has zero dependency or knowledge of the downstream visualization layer (`app.py`). If the dashboard goes offline, Kafka handles backpressure and safely buffers events to prevent any data loss.
* **On-the-Fly Stream Cleaning:** Rather than dropping messy raw payloads straight into storage, the processing layer parses metadata schemas, handles data validation, filters out corrupted system failures, and normalizes numeric values in real time.
* **Infrastructure as Code (IaC):** The complete multi-container event brokerage network is fully containerized via Docker, allowing any developer to stand up the production-grade pipeline with a single command string.

---

## ⚡ Features

- **Sub-Second Event Processing:** Eradicates standard 24-hour batch window latencies, enabling immediate operational visibility.
- **Robust Exception and Protocol Handling:** Script definitions leverage explicit Kafka protocol configurations (`api_version`) to ensure smooth handshakes and strict schema validation between client drivers and server containers.
- **Memory-Optimized Aggregation:** Implements a sliding time-window model on the consumer end to prevent runtime memory leaks during heavy payload delivery.
- **Dynamic Chart Re-rendering:** Uses an interactive reactive layout that updates summary metrics, distribution metrics, and rolling audit logs automatically.

---

## 📂 Project Repository Structure

```text
streaming-pipeline-project/
│
├── docker-compose.yml     # Multi-container orchestration configurations for Kafka & Zookeeper
├── producer.py            # Event simulator emitting mock financial payloads to Kafka
├── consumer.py            # Stream parser running inline validations, filtering, and data cleansing
├── app.py                 # Streamlit UI engine managing analytical metric states and live charts
├── requirements.txt       # Environment dependencies and pinned core libraries
└── README.md              # Comprehensive project portfolio documentation
```
---
## 1. Clone & Navigate to the Project Root
```
git clone [https://github.com/AThet01/Event-Driven-Financial-Stream-Engine](https://github.com/AThet01/Event-Driven-Financial-Stream-Engine)
cd streaming-pipeline-project
```

