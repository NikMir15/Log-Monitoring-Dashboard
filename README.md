# Log Monitoring Dashboard (ELK Stack)

## Overview
This project demonstrates a production-style log monitoring system built using the ELK stack (Elasticsearch, Logstash, Kibana) with Docker.  
It collects application logs, processes them centrally, and visualizes insights such as error trends and service-level logs in real time.

## Tech Stack
- Docker & Docker Compose
- Elasticsearch
- Logstash
- Kibana (Lens dashboards)
- Filebeat
- Python (sample apps)
- Windows + VS Code

## Architecture
- Application containers generate logs
- Filebeat ships logs
- Logstash processes and forwards logs
- Elasticsearch stores logs
- Kibana visualizes logs and dashboards

## Dashboards
- Error Logs Over Time
- Logs by Service
- Recent Error Logs Table

## How to Run (Local)

```bash
docker compose down
docker compose up -d --build
Access
Kibana: http://localhost:5601

Elasticsearch: http://localhost:9200

Key Learnings
Centralized logging with ELK

Dockerized observability stack

Kibana Lens dashboards

Log filtering and indexing

DevOps monitoring fundamentals

Future Improvements
Alerts on error spikes

Metrics with Metricbeat

Deployment to AWS (EC2 / ECS)

Authentication & security