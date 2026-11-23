
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

source = pd.read_csv(
    BASE_DIR / "data" / "retail_sales.csv"
)

clean = pd.read_csv(
    BASE_DIR / "output" / "clean_sales.csv"
)

rejected = pd.read_csv(
    BASE_DIR / "output" / "rejected_sales.csv"
)

with sqlite3.connect(
    BASE_DIR / "output" / "retail_sales.db"
) as conn:
    db_count = conn.execute(
        "SELECT COUNT(*) FROM sales"
    ).fetchone()[0]

source_count = len(source)
clean_count = len(clean)
rejected_count = len(rejected)

print("\n=== DATA RECONCILIATION REPORT ===")
print(f"Source records:   {source_count}")
print(f"Clean records:    {clean_count}")
print(f"Rejected records: {rejected_count}")
print(f"Database records: {db_count}")

source_balanced = (
    source_count == clean_count + rejected_count
)

database_balanced = (
    clean_count == db_count
)

# Confirm all cleaned order IDs exist in the database
with sqlite3.connect(
    BASE_DIR / "output" / "retail_sales.db"
) as conn:
    db_ids = pd.read_sql_query(
        "SELECT order_id FROM sales", conn
    )

ids_match = (
    len(clean) == len(db_ids)
    and clean["order_id"].is_unique
    and db_ids["order_id"].is_unique
    and set(clean["order_id"]) == set(db_ids["order_id"])
)

print("\n=== VALIDATION ===")
print(f"Source balance:  {'PASS' if source_balanced else 'FAIL'}")
print(f"Database balance:{' PASS' if database_balanced else ' FAIL'}")
print(f"Order ID match:  {'PASS' if ids_match else 'FAIL'}")

if source_balanced and database_balanced and ids_match:
    print("\nRECONCILIATION STATUS: PASS")
else:
    print("\nRECONCILIATION STATUS: FAIL")
    raise SystemExit(1)
