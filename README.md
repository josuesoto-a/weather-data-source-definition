# Weather Data Pipeline

## Overview

End-to-end weather data engineering pipeline using the Open-Meteo API.

This project extracts real-time weather data, stores raw JSON files, cleans and transforms the information, generates structured outputs, logs execution events, and runs automatically using Windows Task Scheduler.

---

# Project Architecture

```text
Open-Meteo API
        ↓
Fetch Script
        ↓
Raw JSON Storage
        ↓
Cleaning Script
        ↓
Processed JSON
        ↓
Pipeline Orchestration
        ↓
Logging System
        ↓
Automated Scheduler
```

---

# Data Source Description

This data source provides high-resolution global weather forecasts and real-time weather conditions.

It includes variables such as:

- Temperature
- Wind speed
- Wind direction
- Elevation
- Weather condition codes
- Timestamp data

---

# Data Provider

Open-Meteo

---

# Access Method

REST API

HTTP GET

---

# API Endpoint Example

```bash
https://api.open-meteo.com/v1/forecast?latitude=9.93&longitude=-84.08&current_weather=true
```

---

# Technologies Used

- Python 3.11
- Requests
- JSON
- Logging
- Windows Task Scheduler
- Git & GitHub

---

# Project Structure

```text
weather-data-source-definition/
│
├── data/
│   ├── processed/
│   └── weather_data_*.json
│
├── logs/
│   └── pipeline.log
│
├── scripts/
│   ├── fetch_weather_data.py
│   └── clean_weather_data.py
│
├── pipeline.py
│
├── README.md
│
└── .gitignore
```

---

# Pipeline Components

## 1. Data Ingestion

Script:

```text
scripts/fetch_weather_data.py
```

Responsibilities:

- Connects to Open-Meteo API
- Downloads current weather data
- Stores timestamped raw JSON files

Example output:

```text
weather_data_2026-04-29_08-38-20.json
```

---

## 2. Data Cleaning

Script:

```text
scripts/clean_weather_data.py
```

Responsibilities:

- Detects latest raw JSON file automatically
- Validates JSON structure
- Extracts relevant fields
- Generates clean structured JSON

Cleaned fields:

- latitude
- longitude
- elevation
- temperature
- windspeed
- wind_direction
- weather_code
- timestamp

---

## 3. Logging System

Log file:

```text
logs/pipeline.log
```

The logging system records:

- Pipeline start/end
- API requests
- Successful executions
- Errors and exceptions
- File generation events

---

## 4. Pipeline Orchestration

Script:

```text
pipeline.py
```

Responsibilities:

- Executes fetch script
- Executes cleaning script
- Controls execution flow
- Handles pipeline lifecycle

---

## 5. Automation

The pipeline runs automatically using:

Windows Task Scheduler

Execution frequency:

```text
Daily
```

---

# Example Clean Output

```json
{
    "latitude": 10.0,
    "longitude": -84.125,
    "elevation": 1161.0,
    "temperature": 20.0,
    "windspeed": 11.6,
    "wind_direction": 60,
    "weather_code": 2,
    "timestamp": "2026-04-16T12:00"
}
```

---

# Data Format

JSON

---

# Update Frequency

Weather data is updated hourly based on global meteorological forecast models.

---

# Potential Use Cases

## Smart Agriculture

Automated irrigation systems based on weather conditions and temperature.

## Logistics and Transportation

Route optimization to avoid storms or dangerous weather conditions.

## Renewable Energy

Weather-based forecasting for solar and wind energy production.

## Consumer Applications

Real-time weather dashboards and weather alert systems.

---

# Current Development Status

Completed:

- Data Source Definition
- Data Ingestion
- Raw Data Storage
- Data Cleaning
- Logging System
- Pipeline Orchestration
- Automation Scheduling

Next Stage:

```text
Database Persistence Layer (SQLite)
```

---

# Author

Josué Soto

Data Engineering Learning Project