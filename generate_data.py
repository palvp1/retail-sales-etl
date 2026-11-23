
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

products = [
    ("Laptop", "Electronics", 850),
    ("Headphones", "Electronics", 75),
    ("Keyboard", "Electronics", 45),
    ("Office Chair", "Furniture", 180),
    ("Desk", "Furniture", 250),
    ("Notebook", "Stationery", 8),
    ("Backpack", "Accessories", 55),
    ("Water Bottle", "Accessories", 20)
]

statuses = ["Completed", "Completed", "Completed", "Cancelled", "Returned"]

output_file = DATA_DIR / "retail_sales.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "order_id",
        "customer_id",
        "product",
        "category",
        "quantity",
        "unit_price",
        "order_date",
        "status"
    ])

    for order_id in range(1, 10001):
        product, category, price = random.choice(products)
        quantity = random.randint(1, 5)
        customer_id = random.randint(1001, 3000)

        order_date = datetime(2025, 1, 1) + timedelta(
            days=random.randint(0, 364)
        )

        status = random.choice(statuses)

        writer.writerow([
            order_id,
            customer_id,
            product,
            category,
            quantity,
            price,
            order_date.strftime("%Y-%m-%d"),
            status
        ])

print("Retail sales dataset generated successfully!")
print("Total transactions: 10000")
print(f"File saved: {output_file}")
