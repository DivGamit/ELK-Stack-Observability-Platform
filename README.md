# ELK-Stack-Observability-Platform

A complete, production-like centralized logging system built with the ELK Stack (Elasticsearch + Kibana) and a custom Python ingester.

![Dashboard Preview](screenshots/dashboard.png)

## Project Overview
This project demonstrates end-to-end log collection, parsing, storage, and visualization — exactly how real companies monitor their applications.

## Key Features
- 20 realistic log entries from multiple services
- Custom Python script for structured log ingestion
- Professional Kibana dashboards with dark theme

## Data Note (Fully Transparent)
All logs are synthetic but realistic, intelligently generated using AI to replicate actual production scenarios. This ensures a complete, reproducible, and impressive demo without requiring a running application.

## Tech Stack
- Python (log parsing & ingestion)
- Elasticsearch (storage & full-text search)
- Kibana (beautiful real-time dashboards)

## Quick Setup
```bash
# Start ELK

# Ingest logs
python ingest_logs.py

#Open ElasticSearch
http://localhost:9200

# Open Kibana
http://localhost:5601 → Create index pattern `fake*` → Enjoy the dashboard!
