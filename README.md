# Web Data Aggregation & Price Intelligence System

## Overview
This project is an end-to-end **web data aggregation and analysis pipeline** built using Python.  
It goes beyond basic web scraping by focusing on **clean architecture, data correctness, historical tracking, and analysis**.

The system is **config-driven**, allowing new websites to be added without changing scraping code.

---

## Key Features
- Config-driven generic web scraper (YAML-based)
- Pagination handling
- Data cleaning and normalization
- SQLite storage with snapshot vs history separation
- Price change detection with tolerance-based comparison
- Composite product identity to avoid false history
- Data analysis using Pandas
- Price distribution and trend visualization using Matplotlib

---

## Tech Stack
- Python
- Requests, BeautifulSoup
- Pandas
- SQLite
- Matplotlib
- YAML
- Git

---

## Architecture Overview

Config (YAML)
↓
Generic Scraper
↓
Data Cleaning & Normalization
↓
SQLite Database
├── Latest Snapshot
└── Price History
↓
Analysis & Visualization


---

## Project Structure

web-data-aggregation/
│
├── scraper/
│ └── generic_scraper.py
├── cleaning/
│ └── data_cleaner.py
├── database/
│ └── data_store.py
├── analysis/
│ ├── price_analysis.py
│ └── price_comparator.py
├── visualization/
│ └── price_visualization.py
├── config/
│ └── sites.yaml
├── utils/
│ └── logger.py
│
├── main.py
├── run_visuals.py
├── check_history.py
├── reset_db.py
├── requirements.txt
└── README.md



---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/web-data-aggregation.git
cd web-data-aggregation
