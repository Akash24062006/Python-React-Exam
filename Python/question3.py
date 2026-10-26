
products = {
    "Keyboard": 500,
    "Mouse": 300,
    "Bag": 600,
    "Pen": 50,
    "Notebook": 100
}

for name, price in products.items():
    print(name, ":", price)

def calculate_total(products):
    return sum(products.values())

total = calculate_total(products)

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Price:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
