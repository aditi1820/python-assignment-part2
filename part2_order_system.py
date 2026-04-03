# Restaurant Menu & Order System

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

print("\n===== MENU =====")

categories = ["Starters", "Mains", "Desserts"]

for category in categories:
    print(f"\n===== {category} =====")
    
    for item, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:15} ₹{details['price']:.2f}   [{status}]")

total_items = len(menu)

print("\nTotal items on menu:", total_items)

available_count = 0

for item, details in menu.items():
    if details["available"]:
        available_count += 1

print("Available items:", available_count)
max_price = 0
expensive_item = ""

for item, details in menu.items():
    if details["price"] > max_price:
        max_price = details["price"]
        expensive_item = item

print(f"Most expensive item: {expensive_item} (₹{max_price})")
print("\nItems under ₹150:")

for item, details in menu.items():
    if details["price"] < 150:
        print(f"{item} (₹{details['price']})")

# Task 2: Cart Operations

print("\n===== CART OPERATIONS =====")

cart = []

def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print("Item does not exist in menu.")
        return
    
    if not menu[item_name]["available"]:
        print("Item is currently unavailable.")
        return
    
    # check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated quantity of {item_name}")
            return
    
    # add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    
    print(f"{item_name} added to cart.")

add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1)
add_to_cart("Mystery Burger", 1)
add_to_cart("Chicken Wings", 1)

def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from cart.")
            return
    
    print("Item not found in cart.")

def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(f"{item_name} quantity updated.")
            return
    
    print("Item not found in cart.")

remove_from_cart("Gulab Jamun")
remove_from_cart("Pizza")

update_quantity("Paneer Tikka", 5)

# Order Summary / Bill

print("\n===== BILL SUMMARY =====")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    
    print(f"{item['item']} x {item['quantity']} = ₹{item_total}")

print(f"\nSubtotal: ₹{subtotal}")

# GST calculation (5%)
gst = subtotal * 0.05

print(f"GST (5%): ₹{round(gst,2)}")

total = subtotal + gst

print(f"Total Amount: ₹{round(total,2)}")