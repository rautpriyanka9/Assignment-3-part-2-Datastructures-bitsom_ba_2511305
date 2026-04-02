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

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}
# ================================
# Task 1 — Explore the Menu
# ================================

print("\n===== MENU =====\n")

# get unique categories
categories = []

for item, details in menu.items():
    if details["category"] not in categories:
        categories.append(details["category"])


# print menu grouped by category
for cat in categories:
    print(f"===== {cat} =====")

    for item, details in menu.items():
        if details["category"] == cat:

            price = details["price"]

            if details["available"]:
                status = "[Available]"
            else:
                status = "[Unavailable]"

            print(f"{item:<15} ₹{price:.2f}   {status}")

    print()  # blank line


# -------- Summary Calculations --------

# total items
total_items = len(menu)

# available items
available_count = 0
for details in menu.values():
    if details["available"]:
        available_count += 1

# most expensive item
max_price = 0
exp_item = ""

for item, details in menu.items():
    if details["price"] > max_price:
        max_price = details["price"]
        exp_item = item

# items under 150
cheap_items = []
for item, details in menu.items():
    if details["price"] < 150:
        cheap_items.append((item, details["price"]))


# -------- Print Results --------

print("Total items on menu:", total_items)
print("Available items:", available_count)
print("Most expensive item:", exp_item, "- ₹", max_price)

print("\nItems under ₹150:")
for item, price in cheap_items:
    print(item, "- ₹", price)

    # ================================
# Task 2 — Cart Operations
# ================================

print("\n===== Task 2: Cart Operations =====\n")

cart = []


# -------- Add Item Function --------
def add_to_cart(item_name, qty):

    # check if item exists
    if item_name not in menu:
        print(item_name, "not found in menu")
        return

    # check availability
    if not menu[item_name]["available"]:
        print(item_name, "is currently unavailable")
        return

    # check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += qty
            print(item_name, "quantity updated to", item["quantity"])
            return

    # add new item
    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })

    print(item_name, "added to cart")


# -------- Remove Item Function --------
def remove_from_cart(item_name):

    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(item_name, "removed from cart")
            return

    print(item_name, "not found in cart")


# -------- Update Quantity --------
def update_quantity(item_name, qty):

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = qty
            print(item_name, "quantity updated to", qty)
            return

    print(item_name, "not found in cart")


# -------- Print Cart --------
def print_cart():
    print("\nCurrent Cart:")
    if not cart:
        print("Cart is empty")
        return

    for item in cart:
        print(item["item"], "x", item["quantity"])
    print()


# ================================
# Simulation Steps
# ================================

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)   # should update to 3
print_cart()

add_to_cart("Mystery Burger", 1)  # not in menu
print_cart()

add_to_cart("Chicken Wings", 1)   # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# ================================
# Order Summary
# ================================

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total

    print(f"{item['item']:<18} x{item['quantity']}   ₹{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:           ₹{subtotal:.2f}")
print(f"GST (5%):           ₹{gst:.2f}")
print(f"Total Payable:      ₹{total:.2f}")
print("====================================")