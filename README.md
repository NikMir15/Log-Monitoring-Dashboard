# Log Monitoring Dashboard (ELK Stack)

## Overview
This project implements a centralized log monitoring system using the ELK Stack.
It collects structured logs from multiple services, processes them in real time,
and visualizes insights through Kibana dashboards.

The project demonstrates production-grade DevOps logging and observability practices.

---

## Architecture
Application Services → Filebeat → Logstash → Elasticsearch → Kibana

yaml
Copy code

---

## Tech Stack
- Docker & Docker Compose
- Elasticsearch
- Logstash
- Kibana
- Filebeat
- Python (log-generating services)

---

## Features
- Centralized log collection from multiple services
- Structured JSON logging
- Real-time log ingestion and indexing
- Search and filtering by service, log level, and time
- Interactive dashboards for error analysis and observability

---

## Project Structure
log-monitoring-dashboard/
├── docker-compose.yml
├── services/
│ ├── Dockerfile
│ ├── app1/app.py
│ └── app2/app.py
├── logstash/logstash.conf
├── filebeat/filebeat.yml
└── README.md

yaml
Copy code

---

## How to Run Locally

### Prerequisites
- Docker Desktop (WSL2 enabled on Windows)
- Docker Compose

### Steps
```bash
git clone https://github.com/<your-username>/log-monitoring-dashboard.git
cd log-monitoring-dashboard
docker compose up -d
Open Kibana:

arduino
Copy code
http://localhost:5601
Create Data View:

Index pattern: app-logs-*

Time field: @timestamp

Dashboards
The Kibana dashboard includes:

Error logs over time

Logs grouped by service

Top recurring error messages

Learning Outcomes
Implemented centralized logging using the ELK stack

Debugged real-world Docker, WSL, and Kibana startup issues

Gained hands-on experience with observability and log pipelines