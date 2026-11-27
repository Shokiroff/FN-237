import json
def sales_analysis():
    with open("sales.json", "r", encoding="utf-8") as f:
        products = json.load(f)
    totals = {}
    for item in products:
        totals[item["product"]] = item["price"] * item["quantity"]
    for name, total in totals.items():
        print(f"{name} — {total}")
    best = max(totals, key=totals.get)
    worst = min(totals, key=totals.get)
    print()
    print(f"Eng ko'p daromad: {best} ({totals[best]})")
    print(f"Eng kam daromad: {worst} ({totals[worst]})")
    grand_total = sum(totals.values())
    print()
    print(f"Umumiy savdo: {grand_total}")
    expensive = [name for name, total in totals.items() if total > 1_000_000]
    print()
    print("1,000,000 dan yuqori:")
    print(expensive)
if __name__ == "__main__":
    sales_analysis()
