import json

def sales_analysis():
    with open("sales.json", "r", encoding="utf-8") as file:
        sales = json.load(file)
    for item in sales:
        item["total"] = item["price"] * item["quantity"]
        print(f'{item["product"]} — {item["total"]}')
    highest = max(sales, key=lambda item: item["total"])
    lowest = min(sales, key=lambda item: item["total"])
    total = sum(item["total"] for item in sales)
    filtered = [
        item["product"] for item in sales if item["total"] > 1000000
    ]
    print(f'Eng ko‘p daromad: {highest["product"]} ({highest["total"]})')
    print(f'Eng kam daromad: {lowest["product"]} ({lowest["total"]})')
    print(f"Umumiy savdo: {total}")
    print("1,000,000 dan yuqori:")
    print(filtered)

if __name__ == "__main__":
	sales_analysis()
