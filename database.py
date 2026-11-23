
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "output" / "clean_sales.csv"
DB_FILE = BASE_DIR / "output" / "retail_sales.db"

# Read cleaned transactions
df = pd.read_csv(CSV_FILE)

# Connect to SQLite database
with sqlite3.connect(DB_FILE) as conn:

    # Create or replace the sales table
    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    # Check how many records were loaded
    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_records FROM sales",
        conn
    )

    print("=== DATABASE LOAD ===")
    print(f"Records loaded: {result.iloc[0]['total_records']}")

    # Run a real SQL aggregation
    query = """
    SELECT
        category,
        COUNT(*) AS total_orders,
        SUM(total_amount) AS total_revenue
    FROM sales
    WHERE status = 'Completed'
    GROUP BY category
    ORDER BY total_revenue DESC
    """

    report = pd.read_sql_query(query, conn)

    print("\n=== SQL SALES REPORT ===")
    print(report.to_string(index=False))

print("\nDATABASE LOAD COMPLETED SUCCESSFULLY!")
