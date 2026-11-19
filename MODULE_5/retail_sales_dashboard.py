"""Retail sales dashboard built with CSV and Matplotlib."""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "data" / "retail_sales.csv"


def load_sales(file_path):
    records = []
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            quantity = int(row["Quantity"])
            unit_price = float(row["UnitPrice"])
            records.append({
                "date": row["Date"],
                "product": row["Product"],
                "category": row["Category"],
                "quantity": quantity,
                "revenue": quantity * unit_price,
            })
    if not records:
        raise ValueError("The sales CSV file contains no records.")
    return records


def show_summary(records):
    total_units = sum(row["quantity"] for row in records)
    total_revenue = sum(row["revenue"] for row in records)
    product_revenue = defaultdict(float)
    monthly_revenue = defaultdict(float)
    category_revenue = defaultdict(float)

    for row in records:
        product_revenue[row["product"]] += row["revenue"]
        monthly_revenue[row["date"][:7]] += row["revenue"]
        category_revenue[row["category"]] += row["revenue"]

    print("\n========== RETAIL SALES SUMMARY ==========")
    print(f"Total Transactions : {len(records)}")
    print(f"Units Sold         : {total_units}")
    print(f"Total Revenue      : Rs. {total_revenue:,.2f}")
    print("\nRevenue by Product:")
    for product, revenue in sorted(product_revenue.items()):
        print(f"{product:<15} Rs. {revenue:,.2f}")

    return product_revenue, monthly_revenue, category_revenue


def plot_dashboard(product_revenue, monthly_revenue, category_revenue):
    figure, axes = plt.subplots(1, 3, figsize=(16, 5))
    products = list(product_revenue.keys())
    axes[0].bar(products, product_revenue.values())
    axes[0].set_title("Revenue by Product")
    axes[0].set_ylabel("Revenue (Rs.)")
    axes[0].tick_params(axis="x", rotation=45)

    months = sorted(monthly_revenue)
    axes[1].plot(months, [monthly_revenue[m] for m in months], marker="o")
    axes[1].set_title("Monthly Revenue Trend")
    axes[1].set_ylabel("Revenue (Rs.)")
    axes[1].tick_params(axis="x", rotation=45)

    axes[2].pie(category_revenue.values(), labels=category_revenue.keys(),
                autopct="%1.1f%%", startangle=90)
    axes[2].set_title("Revenue by Category")

    figure.suptitle("Retail Sales Dashboard", fontsize=16)
    figure.tight_layout()
    plt.show()


def main():
    try:
        records = load_sales(DATA_FILE)
        products, months, categories = show_summary(records)
        plot_dashboard(products, months, categories)
    except (OSError, ValueError, KeyError) as error:
        print(f"Unable to create dashboard: {error}")


if __name__ == "__main__":
    main()
