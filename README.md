# Log Monitoring Dashboard (ELK + Grafana)

## Overview
This project implements a centralized log monitoring and visualization system using the **ELK stack (Elasticsearch)** integrated with **Grafana**.  
It enables real-time log ingestion, indexing, and querying, providing operational visibility into application logs across containers.

The setup demonstrates how large-scale logs can be stored, queried, and monitored efficiently using cloud-native tooling.

---

## Architecture
- Application logs are collected and shipped into Elasticsearch
- Logs are indexed using a daily index pattern (`app-logs-*`)
- Grafana connects directly to Elasticsearch for querying and visualization
- Dashboards provide insights such as total logs ingested and log distribution

---

## Tech Stack
- **Docker & Docker Compose**
- **Elasticsearch**
- **Grafana**
- **Linux / Shell**
- **REST APIs (Elasticsearch Query DSL)**

---

## Key Features
- Centralized log storage using Elasticsearch
- Scalable index pattern (`app-logs-*`)
- Real-time log counting and querying
- Grafana dashboards for log analytics
- Containerized setup for easy local deployment

---

## Verification (Working Proof)
Logs are successfully ingested and indexed in Elasticsearch.

Example verification command:
```bash
curl http://localhost:9200/app-logs-*/_count
Sample output:

json
Copy code
{
  "count": 2611238,
  "successful": 1,
  "failed": 0
}
This confirms:

Elasticsearch is running

Indexes exist

Logs are being ingested correctly

How to Run (Local)
Prerequisites
Docker

Docker Compose

Steps
bash
Copy code
git clone <repository-url>
cd log-monitoring-dashboard
docker compose up -d
Access:

Elasticsearch: http://localhost:9200

Grafana: http://localhost:3000

Learning Outcomes
Hands-on experience with log aggregation and observability

Understanding Elasticsearch indexing and queries

Grafana dashboard creation using Elasticsearch as a data source

Container-based monitoring architecture

Future Improvements
Add Logstash/Filebeat pipelines explicitly

Create alerting rules in Grafana

Add severity-based dashboards (ERROR, WARN, INFO)

Deploy to cloud (AWS / Azure) with managed Elasticsearch