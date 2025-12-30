
<<<<<<< HEAD
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
git clone https://github.com/dinamain/web-data-aggregation.git
cd web-data-aggregation
2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the data pipeline
python main.py
5. Run visualizations
python run_visuals.py

Sample Outputs

Price distribution histogram

Top expensive products bar chart

Price trend visualization (if historical data exists)

Learning Outcomes

Designed a real-world data pipeline instead of a one-off script

Understood snapshot vs historical data modeling

Handled false positives in change detection

Applied composite keys for correct entity identity

Practiced debugging data consistency and execution order issues

Followed clean architectural principles

Future Enhancements

Add more websites via configuration

Introduce dashboards (Streamlit)

Schedule periodic scraping

Add alerts for significant price changes
Author

Dina Usman
B.Tech CSE | Python & Data Engineering
=======
>>>>>>> 3c6457eda9b1a7d4cfa1e52662e45b5e56eb5ba3
