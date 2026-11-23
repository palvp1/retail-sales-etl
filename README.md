
# Retail Sales ETL Pipeline

An end-to-end Data Engineering portfolio project that processes synthetic retail transactions using Python, Pandas, SQL, and SQLite.

## Project Overview

This pipeline generates 10,000 synthetic retail transactions, validates and transforms the records, loads cleaned data into SQLite, and produces sales analytics reports.

## Architecture

Synthetic Retail Data (CSV)
        |
        v
Python + Pandas ETL
        |
        v
Data Cleaning & Validation
        |
        +--> Clean Sales CSV
        |
        +--> Rejected Sales CSV
        |
        v
SQLite Database
        |
        v
SQL Sales Analytics
        |
        v
Data Reconciliation

## Technologies

- Python
- Pandas
- SQL
- SQLite
- Git and GitHub

## Features

- Synthetic data generation
- Duplicate order ID removal
- Data type validation
- Revenue calculation
- Category-level sales reporting
- SQLite database integration
- Source-to-target record reconciliation
- Order ID consistency checks

## Project Structure

    retail-sales-etl/
    ├── data/
    │   └── retail_sales.csv
    ├── output/
    │   ├── clean_sales.csv
    │   ├── rejected_sales.csv
    │   ├── category_sales_report.csv
    │   └── retail_sales.db
    ├── generate_data.py
    ├── etl_pipeline.py
    ├── database.py
    ├── reconciliation.py
    ├── requirements.txt
    └── README.md

## How to Run

Install dependencies:

    py -m pip install -r requirements.txt

Generate sample data:

    py generate_data.py

Run the ETL pipeline:

    py etl_pipeline.py

Load the SQLite database:

    py database.py

Validate reconciliation:

    py reconciliation.py

## Example Results

- Source transactions: 10,000
- Clean transactions: 10,000
- Rejected transactions: 0
- Database transactions: 10,000
- Reconciliation: PASS

### Revenue by Category

| Category | Revenue |
|---|---:|
| Electronics | $2,129,900 |
| Furniture | $975,490 |
| Accessories | $174,060 |
| Stationery | $18,632 |

Total completed sales revenue: **$3,298,082**

## Future Improvements

- PostgreSQL database integration
- Incremental loading and upsert logic
- Automated pipeline scheduling
- Unit tests and data quality alerts
- Docker deployment

## Data Disclaimer

All retail transactions are synthetically generated for educational and portfolio purposes.
