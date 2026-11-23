
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "retail_sales.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# STEP 1: EXTRACT
df = pd.read_csv(INPUT_FILE)

print("=== EXTRACT ===")
print(f"Total source records: {len(df)}")

# STEP 2: TRANSFORM
df = df.drop_duplicates(subset=["order_id"]).copy()

df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

df["quantity"] = pd.to_numeric(
    df["quantity"], errors="coerce"
)

df["unit_price"] = pd.to_numeric(
    df["unit_price"], errors="coerce"
)

valid = (
    df["order_id"].notna()
    & df["customer_id"].notna()
    & df["order_date"].notna()
    & df["quantity"].gt(0)
    & df["unit_price"].ge(0)
    & df["status"].isin(
        ["Completed", "Cancelled", "Returned"]
    )
)

clean_df = df.loc[valid].copy()
rejected_df = df.loc[~valid].copy()

clean_df["total_amount"] = (
    clean_df["quantity"] * clean_df["unit_price"]
)

print("\n=== TRANSFORM ===")
print(f"Valid records: {len(clean_df)}")
print(f"Rejected records: {len(rejected_df)}")

# STEP 3: LOAD TO OUTPUT FILES
clean_df.to_csv(
    OUTPUT_DIR / "clean_sales.csv", index=False
)

rejected_df.to_csv(
    OUTPUT_DIR / "rejected_sales.csv", index=False
)

# Only completed orders count toward sales revenue
completed_df = clean_df[
    clean_df["status"] == "Completed"
].copy()

category_report = (
    completed_df.groupby("category", as_index=False)
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("total_amount", "sum")
    )
    .sort_values("total_revenue", ascending=False)
)

category_report.to_csv(
    OUTPUT_DIR / "category_sales_report.csv",
    index=False
)

print("\n=== LOAD ===")
print("Clean sales file saved.")
print("Rejected sales file saved.")
print("Category sales report saved.")

print("\n=== CATEGORY REVENUE ===")
print(category_report.to_string(index=False))

print("\nETL PIPELINE COMPLETED SUCCESSFULLY!")
