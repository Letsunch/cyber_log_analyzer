# README.md

# Cybersecurity Log Analyzer

This is a lightweight Python-based tool to analyze web server access logs, detect anomalies (like brute-force attacks), generate visualizations, and create PDF reports.

## Features
- Apache log parsing using pandas
- Detect brute-force login attempts
- Visualize traffic trends and top IPs
- Generate PDF reports with graphs

## Setup
```bash
pip install pandas matplotlib seaborn
python main.py
```

## Folder Structure
- `main.py` — entry point
- `log_parser.py` — log to DataFrame
- `analyzer.py` — detect anomalies
- `visualizer.py` — generate plots
- `report_generator.py` — create PDF report
- `config.py` — configuration
- `outputs/` — result PDFs and images
- `sample_logs/` — raw logs

## Requirements
- Python 3.8+
- matplotlib
- pandas
- seaborn


