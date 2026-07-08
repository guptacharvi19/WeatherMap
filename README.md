# WeatherMap

# A Real-Time Cloud Data Automation & Meteorological Telemetry Pipeline

An enterprise-grade, 100% serverless data pipeline that automates the ingestion, parsing, and analysis of live global meteorological payloads. Built completely with a zero-cost cloud architecture footprint, the pipeline schedules isolated Linux containers to flag environmental anomalies and stream telemetry evaluations entirely in the cloud.

## 🛠️ System Architecture

The pipeline leverages a modern event-driven architecture, decoupling scheduling, ingestion, compute, and secrets management without incurring any infrastructure overhead:

```text
[GitHub Schedule Clocks] ──(Every 15 Mins)──► [Ubuntu-Latest Runner Container]
                                                          │
                                                (Secured Access Token)
                                                          │
                                                          ▼
                                              [OpenWeatherMap API Node]
                                                          │
                                              (JSON Payload Extractor)
                                                          │
                                                          ▼
[Console Diagnostic Logs] ◄─────────────────── [Python Heuristic Engine]
